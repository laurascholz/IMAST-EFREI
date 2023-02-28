<script>
	$: website = `https://utopia.de/ratgeber/die-schlimmsten-inhaltsstoffe-in-kosmetik/`;
    //product/<int:api_id></int:api_id>


    import axios from 'axios';     				//library to request API endpoint
	import { onMount } from 'svelte';			//hook for the API call
	import { page } from '$app/stores';

	let data = [];
	let search_string = '';  //searchstring from other svelte page

	$: getData(search_string); 

	//get search_string with query parameter
    //wenn das nicht klappt, dann mit load function

    
    search_string = $page.url.searchParams.get('search_string')
	//const search_string = url.searchParams.get('search_string')
    search_string = 'parfume';

    //getData function is used as API caller function
	async function getData(search_string) {
		console.log(search_string);     //debug  --delete later!
		data = [];
		try {
			//API call:
			//   --here the flask API code will be inserted !!!!

			//const res = await axios.get(`https://api.quotable.io/random`, {});
			//localhost/q=nyxlippenstift  ->how the api url should look, get request: parameters are saved with the url
			//data = res.data;
			//const res = await axios.get('C:\Users\laura\OneDrive\Dokumente\GitHub\IMAST-EFREI\Flask API\__caller__.py', /<string:search_string>);  //localhost ist die Flaskseite zur webscraper datei, hier richtiges einfuegen
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

			console.log(data);
		} catch (err) {
			console.log(err);
		}
	}

</script>

<hgroup>
	<h1>Results</h1>
	<p>This page shows the search results for the search for <strong>{search_string}</strong> .</p>
	<p>On this page, there will be the webscraper results as well as the scores</p>
</hgroup>

<!-- ggf als Grid anordnen fuer Uebersichtlickeit?
<div class="grid">
	<div>1</div>
	<div>2</div>
	<div>3</div>
	<div>4</div>
</div>
-->


{#each data as row, i}
	<article>
		<!-- ggf accordion nehmen-->
		{row.product}

		{#each row.details as detail, i}
			{detail.name}
			{detail.price}
		{/each}
	</article>
{/each}

<footer>
	<p>
		Further information about the bad ingredients can be found <a href={website}> here</a>.
	</p>
</footer>
