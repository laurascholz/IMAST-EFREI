<!-- necessary npm install: axios -->
<script lang="ts">
	// @ts-nocheck 

	import axios, { formToJSON } from 'axios'; 	//library to request API endpoint
	import { onMount } from 'svelte'; 			//hook for the API call
	import debounce from 'lodash/debounce'; 	//enables delayed searches
	import Doughnut from './Chart.svelte'; 		//Doughnut-Chart shows the results

	let search_string = '';
	let data = []; 		//product details
	let loading = false; //loading sign for bad connection or longer calculation
	let loading_string = false;
	let ingrs = []; 	//ingredients
	let harmless = 1; 	//result values of ingredients check
	let harmful = 0;
	let dataComplete = {}; //variable for the doughnut chart
	let number = 0;		//number of total ingredients

	var ingredients = {};

	//variables in case of error
	let err = false;
	let err2 = false;
	let msg = '';	

	let colorant = "";
	let restricted = "" ;
	let perservatives = "";
	let	uv_filter = "";


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

	//Flask-API call 2: product url -> product ingredients scraping and assessment
	async function getResults(id, url, name) {
		ingrs = [];
		url = url;
		id = id;
		name = name;
		err = false;		//error while webscraping
		err2 = false;		//error: undefined values
		dataComplete[id] = false;
		number = 0;
		harmful = 0;
		colorant = "";
		restricted = "" ;
		perservatives = "";
		uv_filter ="";
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
					
					//if no values are available, show error message
					if (harmful == undefined && harmless == undefined) {
						err2 = true; 
						msg = "Sadly, the ingredients for this product couldn't be assessed. Please try another one."
					}
					//if at least one harmful ingredient is included, show categories, else all values are 0
					if (harmful > 0){
						colorant = ingrs[2];
						restricted = ingrs[3] ;
						perservatives = ingrs[4];
						uv_filter = ingrs[5];
					}


					//values of harmful and harmless ingredients are saved in a map with their id
					ingredients[id] = { number: number, harmful: harmful, harmless: harmless,
						colorant: colorant, restricted: restricted, perservatives: perservatives, uv_filter: uv_filter
					};
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

<!--      -------------------- The Main Page of the Website -----------------------         -->

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
<!-- home page is shown with information about our website when no search string was entered-->
	<br />
	<hgroup>
		<h1>Welcome to <b> Cosmetic Checker!</b></h1>
		<h2>We will show you up to 10 results and check their ingredients</h2>
	</hgroup>

	<h5>
		This website will help you evaluate your cosmetic products and check if the ingredients are healthy. <br />
		Our results are based of the <a href="https://www.sephora.fr/"> Sephora </a> website. We use an API
		and web scraping to collect our results. Whether or not an ingredient is healthy is decided by
		comparing it to the <a href="https://ec.europa.eu/growth/tools-databases/cosing/index.cfm">  CosIng Database </a> published by the European Commission. 
		We then show you how many potentially harmful ingredients are included in the product you searched for and to which category they count. At the end, you can choose the
		healthy option!
		<br /> <br />
		Further information about our website, our business model and the sources can be found in the <a href="/about"> about </a> section of our website.
	</h5>
{:else if loading_string}
<!-- after a search string is entered, a loading message is shown-->
	<p aria-busy="true">Checking products of your choice for harmful ingredients</p>
{:else}
<!-- after the search string has completely loaded, the results are shown-->
	{#each data as row, i}
		<details>
			
			<!-- whenever a product is selected, the Ingredients are checked-->
			<summary on:focus={() => getResults(row.id, row.url, row.name)}>
				<!-- Title of product:-->
				<b>{row.name}</b> by  <i>{row.brand}</i>
			</summary>

			<!-- further information of a product is shown in divs, when the accordion is opened-->
			<div class="grid">
				
				{#if err}
					<!-- if there is an error while scraping ingredients, msg is shown-->
					<p>{msg}</p>
				{/if}
				
				<!-- loading screen when the ingredient values are not yet calculated-->
				{#if dataComplete[row.id] == false}
					<p aria-busy="true">
						Checking your product's ingredients ...
					</p>
				{/if}
				
				<!-- when the values are returned from the Flask API-->
				{#if ingredients[row.id] != null}
					
					<p>
						<img src={row.images.productTile.url} alt="" />
					</p>
					{#if err2}
					<!-- if the ingredients values are undefined, msg is shown-->
						<p>{msg}</p>
					{:else }
					<p>
						The product consists of <b> {ingredients[row.id].number}</b> ingredients:
						<br />
						- <b><ins> {ingredients[row.id].harmless} </ins></b> harmless <br />
						- <b><mark> {ingredients[row.id].harmful} </mark></b> harmful
						
						<br /> <br />
						<!-- if the product contains at least one harmful ingredient, a list of the numbers per categories is shown-->
						{#if ingredients[row.id].harmful != 0}
							<details open>
								<summary>The product includes ...</summary>
								<ul>
								{#if ingredients[row.id].colorant != ""} <li> {ingredients[row.id].colorant} <b>colorants</b></li> {/if}
								{#if ingredients[row.id].restricted != ""} <li> {ingredients[row.id].restricted} <b>restricted ingredients</b></li> {/if}
								{#if ingredients[row.id].perservatives != ""} <li>{ingredients[row.id].perservatives} <b>perservatives</b></li> {/if}
								{#if ingredients[row.id].uv_filter != ""} <li>{ingredients[row.id].uv_filter} <b>UV filter</b></li> {/if}
								</ul>
							</details>
						{/if}

						<br />
						Shop the product <a href={row.url}>here</a> for <b>{row.price.minPrice}</b> €
					</p>
					<!-- doughnut chart which illustrates the ingredient values-->
					<p>
						<Doughnut
							bind:harmful={ingredients[row.id].harmful}
							bind:harmless={ingredients[row.id].harmless}
						/>
					</p>
					{/if}
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
	h5 {
		text-align: center;
		font-weight:normal;
	}
	
</style>
