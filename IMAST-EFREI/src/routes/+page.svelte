<!-- necessary npm install: axios -->
<script lang="ts">
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; //library to request API endpoint
	import { onMount } from 'svelte'; //hook for the API call
	import Page from './about/+page.svelte';
	import debounce from 'lodash/debounce'; //enables delayed searches
	import Doughnut from './Chart.svelte'; //Doughnut-Chart shows the results

	let search_string = '';
	let data = [];					//product details
	let loading = false; 			//loading sign for bad connection or longer calculation
	let loading_string = false;
	let ingrs = [];					//inrgedients
	let harmless = 1;				//results of ingredients check
	let harmful = 0;
	let dataComplete = false;		//variable for the doughnut chart
	let number = 0;
	
	//variables in case of error
	let err = false;				
	let msg = "";

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
	async function getResults(id, url, name) {
		ingrs = [];
		err = "";
		url = url;
		id = id;
		name = name;
		err = false;
		dataComplete = false;
		number = 0;
		//use the ids to access the other data from database or the url to use the webscraper
		try {
			loading = true;
			await axios
				.post('http://127.0.0.1:5000/products', { id: id, url: url, name: name })
				.then(function (response) {
					// handle success
					ingrs = response.data;
					console.log(ingrs)
					//results values 
					harmful = ingrs[0];
					harmless = ingrs[1];
					number = harmful + harmless;
					console.log(harmful);
					console.log(harmless);
					loading = false;
					dataComplete = true;
				})
				.catch(function (error) {
					// handle error
					loading = false;
					console.log(error);
					//error message
					msg ="Sadly, no product information could be aquired for this product. Please try a different one.";
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
{#if search_string == ""}
	<br />
	<h3>Welcome to <b> Cosmetic Checker </b>, our website that enables everyone to life live the healthiest! </h3>
	
	<p>
		This app will help you evaluate your products and check if the ingredients are healthy. Our results are based of the <a href= "https://www.sephora.fr/" > Sephora </a> website. 
		We use an API and web scraping to collect our results. Whether or not an ingredient is healthy is decided by comparing it to a list !LINK! published by the EU??.
		We than show you how many potentially harmful ingredients are included in the product you searched for so that you can choose the healthy option!
		<br /> <br />
		Further information can be found in the <a href="/about"> about </a> section of our website.


	</p>
{:else if loading_string}
	<p aria-busy=true>
		Checking for products of your choice for harmful ingredients 
	</p>
{:else}
	{#each data as row, i}
		<details>
			<!-- whenever a product is selected, the Ingredients are checked-->
			<summary on:focus={() => getResults(row.id, row.url, row.name)}>
				<b>{row.name}</b> by
				<i>{row.brand}</i>
			</summary>
			<div class="grid">  <!-- information shown when accordion is opened:-->
				<p>
					<img src={row.images.productTile.url} alt="" />
				</p>
				{#if !err}  
					{#if !dataComplete}
						<p aria-busy=true>
							Checking your products ingredients
							<br />
							- Shop the product <a href={row.url}>here</a> for {row.price.minPrice} EURO
						</p>
					{:else}
						<p>
							The product consists of <b> {number}</b> ingredients: 
							<br />
							- <b><ins> {harmless} </ins></b> harmless <br/>
							- <b><mark> {harmful} </mark></b> harmful 
							
							
							<br /><br /><br /><br />
							Shop the product <a href={row.url}>here</a> for <b>{row.price.minPrice}</b> € EURO
						</p>
					{/if}
					
					<p>
						{#if dataComplete} <!-- ansonsten await function() nehmen? Doughnut Chart is only created when the variables are updated -->
						<!--<Doughnut bind:loading bind:harmful_initial={harmful} bind:harmless_initial={harmless} />-->
						<Doughnut bind:harmful bind:harmless />
						{/if}
					</p>
				{:else} <!-- if there is an error while scraping ingredients, msg is shown-->
					<p> {msg}</p>
				{/if}
			</div>
		</details>
	{/each}
{/if}


<style>
	mark {
		color:crimson;
		background-color:white;
	}
	
	b {
		color:indigo;
	}
	a {
		color:darkmagenta;
	}

	h3 {
		text-align:center;
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