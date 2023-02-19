<script>
	// @ts-nocheck

	import axios from 'axios';
	import { onMount } from 'svelte';
	import Page from './about/+page.svelte';

	let data = [];
	let search = '';

	$: getData(search);

	async function getData(search) {
		console.log(search);
		data = [];
		try {
			//const res = await axios.get(`https://api.quotable.io/random`, {});
			//data = res.data;

			data = [
				{
					product: 1,
					details: [{ name: 'NXY', price: '14.29' }]
				},
				{ product: 2, details: [{ name: 'Maybeline', price: '24.29' }] }
			];
			console.log(data);
		} catch (err) {
			console.log(err);
		}
	}
</script>

<!-- navigation between home and about page as practice-->

<div class="grid">
	<div>
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

<div>
	<button type="submit" on:click={getData}>Search for the product</button>
</div>

{#each data as row, i}
	<article>
		{row.product}

		{#each row.details as detail, i}
			{detail.name}
			{detail.price}
		{/each}
	</article>
{/each}

<style>
	/* here CSS code */
</style>
