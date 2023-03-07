<!-- necessary npm install: axios -->
<script lang="ts">
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; //library to request API endpoint
	import { onMount } from 'svelte'; //hook for the API call
	import Page from './about/+page.svelte';
	import debounce from 'lodash/debounce'; //enables delayed searches
	import Doughnut from './Chart.svelte'; //Doughnut-Chart shows the results

	let search_string = '';
	let data = [];
	let loading = false; //loading sign for bad connection or longer calculation
	let loading_string = false;
	let info = [];
	//let harmful = [];
	let harmless = 10;
	let harmful = 28;

	//getData function is called for every change of search_string
	$: getData(search_string);
	$: if (search_string == '') data = [];

	//delay for automatic search when typing in the search_string
	const handleInput = debounce((e) => {
		search_string = e.target.value;
	}, 500);

	//Flask-API call 1: search_string -> product ids and information without the ingredients and score
	async function getData() {
		try {
			if (search_string == '') return;
			loading_string = true;
			await axios
				.get('http://127.0.0.1:5000/?search=' + search_string)
				.then(function (response) {
					// handle success
					loading_string = false;
					data = response.data;
				})
				.catch(function (error) {
					// handle error
					loading_string = false;
					console.log(error);
				})
				.finally(function () {
					loading_string = false;
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
					info = response.data;
					//harmful[0] = "12";
					harmful = 15;
					harmless = 100;
					loading = false;
				})
				.catch(function (error) {
					// handle error
					loading = false;
					console.log(error);
					//das hier einbinden fuer spaeter
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

<!-- results within accordions-->
{#if loading_string}
	<p aria-busy=true>
		Checking for products of your choice for harmful ingredients 
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
				</p>
				<p>
					The product includes <b><mark> XX </mark></b> harmful and <b><ins> YY </ins></b> harmless
					ingredients.
					<br />
					- Shop the product <a href={row.url}>here</a> for {row.price.minPrice} EURO
				</p>
				<p>
						<Doughnut bind:loading bind:harmful_initial={harmful} bind:harmless_initial={harmless} />
				</p>
			</div>
		</details>
	{/each}
{/if}
