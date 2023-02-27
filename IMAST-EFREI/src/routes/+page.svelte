<!-- necessary npm installs: axios, -->
<script>
	// @ts-nocheck

	import axios, { formToJSON } from 'axios'; //library to request API endpoint
	import { onMount } from 'svelte'; //hook for the API call
	import Page from './about/+page.svelte';
	import { goto } from '$app/navigation';
	import { redirect } from '@sveltejs/kit';

	let data = [];
	let search_string = "";
	let zahl = '0';

	//$: getData(search_string);

	//getData function is used as API caller function

	async function getData() {
		//console.log(search_string); //debug  --delete later!
		data = [];
		try {
			//const res = await axios.get(`https://api.quotable.io/random`, {});
			//localhost/q=nyxlippenstift  ->how the api url should look, get request: parameters are saved with the url
			//data = res.data;

			//Flask-API call 1: search_string -> product ids
			await axios
				.get('http://127.0.0.1:5000/?search=' + search_string)
				.then(function (response) {
					// handle success
					zahl = response.data;
					console.log(zahl)
				})
				.catch(function (error) {
					// handle error
					console.log(error);
				})
				.finally(function () {
					// always executed
				});
			//data = res.ids;	<string:search_string>			-> das ergebnis muesste ein feld von ids sein, ist dann const der richtige Datentyp
			//Flask-API call 2: product ids -> product details and score
			//use the ids to access the other data from database or website
			//const info = await axios.get("/<int:api_id>")
			//const info.data


			//the following is test data
			data = [
				{
					id: 527973,
					details: [
						{
							brand: 'RARE BEAUTY',
							name: 'Soft Pinch - Blush liquide',
							price: '23',
							url: 'https://www.sephora.fr/p/soft-pinch---liquid-blush-527973.html',
							image:
								'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dw22da3356/images/hi-res/SKU/SKU_2383/527973_swatch.jpg?sw=240&sh=240&sm=fit'
						}
					]
				},
				{
					id: 206220,
					details: [
						{
							brand: 'SEPHORA COLLECTION',
							name: 'Cream Lip Stain Mat - Rouge À Lèvres Mat',
							price: '12.99',
							url: 'https://www.sephora.fr/p/cream-lip-stain-mat---rouge-a-levres-mat-206220.html',
							image:
								'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dw7f5398c3/images/hi-res/SKU/SKU_1/206220_swatch.jpg?sw=240&sh=240&sm=fit'
						}
					]
				},
				{
					id: 446306,
					details: [
						{
							brand: 'TOO FACED',
							name: 'Born This Way Super Coverage Concealer - Correcteur anticernes',
							price: '32',
							url: 'https://www.sephora.fr/p/born-this-way-super-coverage-concealer---correcteur-anti-cernes-446306.html',
							image:
								'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dwd44c6475/images/hi-res/SKU/SKU_6/446306_swatch.jpg?sw=240&sh=240&sm=fit'
						}
					]
				},
				{
					id: 502359,
					details: [
						{
							brand: 'SEPHORA COLLECTION',
							name: 'Best Skin Ever Anticernes - Anticernes haute couvrance fini naturel',
							price: '14.99',
							url: 'https://www.sephora.fr/p/best-skin-ever-anticernes---anticernes-haute-couvrance-fini-naturel-502359.html',
							image:
								'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dwe0790338/images/hi-res/SKU/SKU_2013/502359_swatch.jpg?sw=240&sh=240&sm=fit'
						}
					]
				},
				{
					id: 451695,
					details: [
						{
							brand: 'TARTE',
							name: 'shape tape - Anticernes',
							price: '28',
							url: 'https://www.sephora.fr/p/shape-tape-contour-concealer---anticernes-matte-451695.html',
							image:
								'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/-/Sites-masterCatalog_Sephora/default/dwe7008f6c/images/hi-res/SKU/SKU_672/451695_swatch.jpg?sw=240&sh=240&sm=fit'
						}
					]
				}
			];
			console.log(data);
			console.log(zahl);
		} catch (err) {
			console.log(err);
		}
	}
</script>

<!-- searchbar with submit button - search string can be entered either with pressing enter oder pressing submit -->
<!-- search string is saved in variable search and bind: updates the value with every character change-->
<div class="grid">
	<div>
		<!-- the API caller function is used by the search bar when pressing enter-->
		<label for="search">
			Add a product, a category or a brand:
			<input
				type="search"
				id="search"
				name="search"
				bind:value={search_string}
				placeholder="Search your product here..."
				required
			/>
		</label>
	</div>
	<!--<div>
		<p>              </p>
		<a href="/product" role="button" type="submit" on:click={getData()}>Search for the product</a>
	</div> -->
</div>

<!--else:  when clicking on the button, the API request will be sent with the onMount function-->
<div>
	<button type="submit" on:click={() => getData()}>Search for the product</button>
	<p>{zahl}</p>
</div>

<!-- results beneath the search bar  
goto(url: "C:\Users\laura\OneDrive\Dokumente\GitHub\IMAST-EFREI\IMAST-EFREI\src\routes\product")
, redirect("/product")  
immer Fehlermeldung identifier expected-->

{#each data as row, i}
	<details>
		{#each row.details as detail, i}
			<summary>
				<b>{detail.name}</b> by
				<i>{detail.brand}</i>
				- The Score of this product is <b>XXXX</b>
			</summary>
			<p>
				<img src={detail.image} alt="" />
				Shop the product <a href={detail.url}>here</a> for
				{detail.price} EURO, id: {row.id}
			</p>
		{/each}
	</details>
{/each}
