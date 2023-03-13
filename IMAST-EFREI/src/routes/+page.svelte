<!-- necessary npm install: axios -->
<script lang="ts">
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; //library to request API endpoint
	import { onMount } from 'svelte'; //hook for the API call
	import Page from './about/+page.svelte';
	import debounce from 'lodash/debounce'; //enables delayed searches
	import Doughnut from './Chart.svelte'; //Doughnut-Chart shows the results

	let search_string = '';
	let data = []; //product details
	let loading = false; //loading sign for bad connection or longer calculation
	let loading_string = false;
	let ingrs = []; //inrgedients
	let harmless = 1; //results of ingredients check
	let harmful = 0;
	let dataComplete = {}; //variable for the doughnut chart
	let number = 0;

	var ingredients = {};

	//variables in case of error
	let err = false;
	let msg = '';	

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
			dataComplete = {};
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
					// always executed
					loading_string = false;
					
				});
		} catch (err) {
			console.log(err);
		}
	}

	//Flask-API call 2: product ids -> check if product in database
	//		ELSE 		product url -> product ingredients scraping and score calculation
	async function getResults(id, url, name, i) {
		ingrs = [];
		err = '';
		url = url;
		id = id;
		name = name;
		err = false;
		dataComplete[id] = false;
		number = 0;
		i = i; 
		try {
			loading = true;
			await axios
				.post('http://127.0.0.1:5000/products', { id: id, url: url, name: name })
				.then(function (response) {
					// handle success
					ingrs = response.data;
					harmful = ingrs[0];
					harmless = ingrs[1];
					number = harmful + harmless;
					ingredients[id] = { number: number, harmful: harmful, harmless: harmless };
					
					//console.log(ingredients);
					
					loading = false;
					dataComplete[id] = true;
				})
				.catch(function (error) {
					// handle error
					loading = false;
					console.log(error);
					//error message
					msg =
						'Sadly, no product information could be aquired for this product. Please try a different one.';
					err = true;
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
{#if search_string == ''}
	<br />
	<hgroup>
		<h1>Welcome to <b> Cosmetic Checker!</b></h1>
		<h2>We will show you up to 10 results and check their ingredients</h2>
	</hgroup>

	<p>
		This website will help you evaluate your cosmetic products and check if the ingredients are healthy. Our
		results are based of the <a href="https://www.sephora.fr/"> Sephora </a> website. We use an API
		and web scraping to collect our results. Whether or not an ingredient is healthy is decided by
		comparing it to the <a href="https://ec.europa.eu/growth/tools-databases/cosing/index.cfm">  CosIng Database </a> published by the European Commission. We then show you how many potentially
		harmful ingredients are included in the product you searched for. At the end, you can choose the
		healthy option!
		<br /> <br />
		Further information about our website, our vision and the sources can be found in the <a href="/about"> about </a> section of our website.
	</p>
{:else if loading_string}
	<p aria-busy="true">Checking for products of your choice for harmful ingredients</p>
{:else}
	{#each data as row, i}
		<details>
			<!-- whenever a product is selected, the Ingredients are checked-->
			<summary on:focus={() => getResults(row.id, row.url, row.name, i)}>
				<b>{row.name}</b> by
				<i>{row.brand}</i>
			</summary>
			<div class="grid">
				{#if dataComplete[row.id] == false}
					<p aria-busy="true">
						Checking your products ingredients
						<br />
						- Shop the product <a href={row.url}>here</a> for {row.price.minPrice} EURO
					</p>
				{/if}
				{#if ingredients[row.id] != null}
					<!-- information shown when accordion is opened:-->
					<p>
						<img src={row.images.productTile.url} alt="" />
					</p>

					
					<p>
						The product consists of <b> {ingredients[row.id].number}</b> ingredients:
						<br />
						- <b><ins> {ingredients[row.id].harmless} </ins></b> harmless <br />
						- <b><mark> {ingredients[row.id].harmful} </mark></b> harmful

						<br /><br /><br />
						Shop the product <a href={row.url}>here</a> for <b>{row.price.minPrice}</b> € EURO
					</p>
					<p>
						<Doughnut
							bind:harmful={ingredients[row.id].harmful}
							bind:harmless={ingredients[row.id].harmless}
						/>
					</p>
				{/if}
				{#if err}
					<!-- if there is an error while scraping ingredients, msg is shown-->
					<p>{msg}</p>
				{/if}
			</div>
		</details>
	{/each}
{/if}

<style>
	mark {
		color: crimson;
		background-color: white;
	}

	b {
		color: indigo;
	}
	a {
		color: darkmagenta;
		font-weight: bold;
	}

	h1 {
		text-align: center;
	}
	h2 {
		text-align: center;
	}
	/*
	p {
		
		background-color:honeydew;
		border: 2px solid cadetblue;
	
	}
	summary {
		color:darkslateblue;
	}
	
	mark {
		color:crimson;
		background-color:white;
	}
	p {
		border-bottom: 2px solid limegreen;
		padding: 10px;
	}*/

	/*button {
		color: hotpink;
		font-size: 20px;
		font-weight: bold;
		background-color: black;
	}*/
</style>
