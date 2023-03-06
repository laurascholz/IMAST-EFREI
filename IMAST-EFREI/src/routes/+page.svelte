<!-- necessary npm install: axios -->
<script lang="ts">
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; //library to request API endpoint
	import { onMount } from 'svelte'; //hook for the API call
	import Page from './about/+page.svelte';
	import { goto } from '$app/navigation';
	import { redirect } from '@sveltejs/kit';
	import debounce from 'lodash/debounce'; //enables delayed searches
	import Chart from 'chart.js/auto';
	//import Chart from './Chart.svelte';
	//import { Colors } from 'chart.js';
	//import { browser } from '$app/environment';
	//import { FY2021 as satisfactionData2021 } from '$lib/data/satisfaction.json';

	//import Chart from 'chart.js/auto/auto.js';

	let assessment;

	//let barChartElement: HTMLCanvasElement;
	let search_string = '';
	let data = [];
	let loading = false; //loading sign for bad connection or longer calculation
	let info = [];

	//getData function is called for every change of search_string
	$: getData(search_string);
	$: if (search_string == '') data = [];

	//delay for automatic search when typing in the search_string
	const handleInput = debounce((e) => {
		search_string = e.target.value;
	}, 800);

	//Flask-API call 1: search_string -> product ids and information without the ingredients and score
	async function getData() {
		try {
			if (search_string == '') return;
			loading = true;
			await axios
				.get('http://127.0.0.1:5000/?search=' + search_string)
				.then(function (response) {
					// handle success
					loading = false;
					data = response.data;
				})
				.catch(function (error) {
					// handle error
					loading = false;
					console.log(error);
				})
				.finally(function () {
					loading = false;
					// always executed
				});
		} catch (err) {
			console.log(err);
		}
	}

	//Flask-API call 2: product ids -> check if product in database
	//		ELSE 		product url -> product ingredients scraping and score calculation
	async function getScore(id, url, name) {
		//console.log("Active")
		info = [];
		url = url;
		id = id;
		name = name;
		//use the ids to access the other data from database or the url to use the webscraper
		try {
			loading = true;
			await axios
				.post('http://127.0.0.1:5000/products', { id: id, url: url, name: name })
				.then(function (response) {
					// handle success
					loading = false;
					info = response.data;
					//const ctx = assessment.getContext('2d');
					// Initialize chart using default config set
					//var myChart = new Chart(ctx, config);
				})
				.catch(function (error) {
					// handle error
					loading = false;
					console.log(error);
					info =
						'Sadly, no product information could be aquired for this product. Please try a different one.';
				})
				.finally(function () {
					// always executed
					loading = false;
				});
		} catch (err) {
			console.log(err);
		}
	}

	//the doughnut element illustrates the assessment of the ingredients
	//data2 has the data to the Doughnut Chart.js Element
	const data2 = {
		labels: ['Harmful', 'Harmless'],
		datasets: [
			{
				label: 'Ingredients Assessment',
				data: [100, 300], // these values will be the ingredients
				backgroundColor: ['#FF0000', '#00ff00'],
				//hoverOffset: 4,    keine ahnung was das macht
				borderWidth: 0
			}
		]
	};
	const config = {
		//config defines the type of chart, here doughnut
		type: 'doughnut',
		data: data2,
		options: {
			borderRadius: '30',
			responsive: true,
			cutout: '65%',
			spacing: 2,
			plugins: {
				legend: {
					position: 'bottom',
					display: true,
					labels: {
						usePointStyle: true,
						padding: 20,
						font: {
							size: 14
						}
					}
				},
				title: {
					display: true,
					text: 'My Personal Portfolio'
				}
			}
		}
	};
	onMount(()=> {
        const ctx = assessment.getContext('2d');
        // Initialize chart using default config set
        var myChart = new Chart(ctx, config);
      })
</script>

<!--                              The Main Page of the Website                            -->

<!-- searchbar: search_string is saved delayed -->
<div class="grid">
	<div>
		<input
			type="search"
			id="search"
			name="search"
			on:input={handleInput}
			placeholder="Search for a product, a category or a brand"
			required
		/>
	</div>
</div>

<!-- chart example: <canvas bind:this={assessment} width={3} height={3} />
	https://dev.to/wesleymutwiri/create-beautiful-charts-with-svelte-and-chart-js-512n -->
	<canvas bind:this={assessment} width={3} height={3} />

<!-- results within accordions-->
{#if search_string == ''}
	<p aria-busy={loading}>
		Check products of your choice for harmful ingredients by adding their name in the searchbar
	</p>
{:else}
	{#each data as row, i}
		<details>
			<summary on:focus={() => getScore(row.id, row.url, row.name)}>
				<!-- whenever a product is selected, the Score is calculated and shown-->
				<b>{row.name}</b> by
				<i>{row.brand}</i>
			</summary>
			<div class="grid">
				<p>
					<img src={row.images.productTile.url} alt="" />
					<br />
					- Shop the product <a href={row.url}>here</a> for {row.price.minPrice} EURO
				</p>
				<p aria-busy={loading}>
					Insert GRAPHIC here
					
					<br />
					The product includes <b><mark> XX </mark></b> harmful and <b><ins> YY </ins></b> harmless
					ingredients.
					<br />
					The Score of this product is {i}
				</p>
				<br />
				{info}
			</div>
		</details>
	{/each}
{/if}

<!--else:  when clicking on the button, the API request will be sent with the onMount function-->
<!--
<div>
	<button type="submit" on:click={() => getData()}>Search for the product</button>
</div>
-->
<!-- results beneath the search bar  
goto(url: "C:\Users\laura\OneDrive\Dokumente\GitHub\IMAST-EFREI\IMAST-EFREI\src\routes\product")
, redirect("/product")  
immer Fehlermeldung identifier expected-->

<!--<div>
		<p>              </p>
		<a href="/product" role="button" type="submit" on:click={getData()}>Search for the product</a>
	</div> -->
