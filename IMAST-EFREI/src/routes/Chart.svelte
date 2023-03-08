<script lang="ts">
	// @ts-nocheck

	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	//export let harmful_initial; //= ["0"];
	//export let harmless_initial; //= ["1"];
	export let harmful; //= ["0"];
	export let harmless; //= ["1"];
	//export let loading;

	let loaded = false;

	//let harmful = harmful_initial;
	//let harmless = harmless_initial;

	/*$: if (loading == false && loaded == false) {
		loaded = true;
		harmful = harmful_initial;
		harmless = harmless_initial;
	}*/


	let portfolio = document.getElementById('canvas');

	//the doughnut element illustrates the portfolio of the ingredients
	//data has the data to the Doughnut Chart.js Element

	function createDoughnut() {
		const ctx = portfolio.getContext('2d');
		// Initialize chart using default config set
		var myChart = new Chart(ctx, config);
	}

	const data = {
		labels: ['Harmful', 'Harmless'],
		datasets: [
			{
				label: 'Ingredients Assessment',
				data: [harmful, harmless], // these values will be the ingredients
				backgroundColor: ['#FF0000', '#00ff00'],
				//hoverOffset: 4,    keine ahnung was das macht
				borderWidth: 0
			}
		]
	};
	const config = {
		//config defines the type of chart, here doughnut
		type: 'doughnut',
		data: data,
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
					text: 'Ingredients Assessment'
				}
			}
		}
	};

	onMount(createDoughnut);
</script>

<!--{#if loaded == false}
	<p aria-busy="true" />
{:else}
	<canvas id="canvas" bind:this={portfolio} width={3} height={3} />
{/if}-->

<canvas id="canvas" bind:this={portfolio} width={3} height={3} />