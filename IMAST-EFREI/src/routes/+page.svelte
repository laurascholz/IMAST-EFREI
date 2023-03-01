<!-- necessary npm installs: axios -->
<script>
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; 	//library to request API endpoint
	import { onMount } from 'svelte'; 			//hook for the API call
	import Page from './about/+page.svelte';
	import { goto } from '$app/navigation';
	import { redirect } from '@sveltejs/kit';
	import debounce from 'lodash/debounce'		//enables delayed searches

	let search_string = '';
	let data = [];
	let loading = false;			//loading sign for bad connection or longer calculation
	let info = [];
	
	//getData function is called for every change of search_string
	$: getData(search_string);
	$: if(search_string == "") data=[];

	//delay for automatic search when typing in the search_string
	const handleInput = debounce((e) => {
		search_string = e.target.value;
	}, 300);

	//Flask-API call 1: search_string -> product ids and information without the ingredients and score
	async function getData() {
		try {
			if(search_string == "") return
			loading = true
			await axios
				.get('http://127.0.0.1:5000/?search=' + search_string)    //<string:search_string>
				.then(function (response) {
					// handle success
					loading = false
					data = response.data;
				})
				.catch(function (error) {
					// handle error
					loading = false

					console.log(error);
				})
				.finally(function () {
					loading = false

					// always executed
				});
		} catch (err) {
			console.log(err);
		}
	}


	//Flask-API call 2: product ids -> product ingresdients scraping and score calculation
	async function getScore(id) {
		console.log("Active")
		info = [];
		//use the ids to access the other data from database or website
		try {
			await axios
				.get('http://127.0.0.1:5000/products/?id=' + id)    //("/<int:api_id>")
				.then(function (response) {
					// handle success
					//map angucken und damit machen
					//product id = map id unten im code
					info = response.data;
					console.log(info)
				})
				.catch(function (error) {
					// handle error
					console.log(error);
				})
				.finally(function () {
					// always executed
				});
		} catch (err) {
			console.log(err);
		}
	}
</script>

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
	<p aria-busy={loading}>Check products of your choice for harmful ingredients by adding their name in the searchbar</p>
{:else}
{#each data as row, i}
	<details>
		<summary on:focus={() => getScore(row.id)}>
			<b>{row.name}</b> by
			<i>{row.brand}</i>
		</summary>
		<p>
			<img src={row.images.productTile.url} alt="" />
			The Score of this product is {i}
			- Shop the product <a href={row.url}>here</a> for
			{row.price.minPrice} EURO, id: {row.id}
			{info}
		</p>
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