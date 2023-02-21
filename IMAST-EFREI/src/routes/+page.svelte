<!-- necessary npm installs: axios, -->


<script>
	// @ts-nocheck

	import axios from 'axios';     				//library to request API endpoint
	import { onMount } from 'svelte';			//hook for the API call
	import Page from './about/+page.svelte';

	let data = [];
	let search = '';

	$: getData(search); 

	//getData function is used as API caller function
	
	async function getData(search) {
		console.log(search);     //debug  --delete later!
		data = [];
		try {
			//API call:
			//   --here the flask API code will be inserted !!!!

			//const res = await axios.get(`https://api.quotable.io/random`, {});
			//localhost/q=nyxlippenstift  ->how the api url should look
			//data = res.data;


			//the following is test data
			data = [
				{
					product: 1,
					details: [{ name: 'NXY', price: '14.29' }]
				},
				{ 
					product: 2, 
					details: [{ name: 'Maybeline', price: '24.29' }] 
				},
				{ 
					product: 3, 
					details: [{ name: 'Lancome', price: '69.99' }] 
				},
				{ 
					product: 4, 
					details: [{ name: 'Chanel Lipstick', price: '35.69' }] 
				}
			];
			//console.log(data);
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
				bind:value={search}		 
				placeholder="Search your product here..."
				required
			/>  
		</label>
	</div>
</div>

<!--else:  when clicking on the button, the API request will be sent with the onMount function-->
<div>
	<button type="submit" on:click={getData}>Search for the product</button>
</div>

<!-- results beneath the search bar-->

{#each data as row, i}
	<article>  <!-- ggf accordion nehmen-->
		{row.product}

		{#each row.details as detail, i}
			{detail.name}
			{detail.price}
		{/each}
	</article>
{/each}


