<script lang="ts">
	// @ts-nocheck

	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	// variables that will be the ingredient values of the product
	export let harmful; 
	export let harmless; 

	//assessment is the doughnut chart of that product
	let assessment = document.getElementById('canvas');

	

	function createDoughnut() {
		const ctx = assessment.getContext('2d');
		// Initialize chart using default config set
		var myChart = new Chart(ctx, config);
	}

	//data includes the ingredient values for the Doughnut Chart.js Element
	const data = {
		labels: ['Harmful', 'Harmless'],
		datasets: [
			{
				label: 'Ingredients Assessment',
				data: [harmful, harmless], 		// these values will be the ingredients
				backgroundColor: ['#FF0000', '#228B22'],
				hoverOffset: 4,   
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
			cutout: '65%',			//how big the free space in doughnut is
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

	//when component is rendered, Doughnut chart is created
	onMount(createDoughnut);

</script>

<!-- the canvas object is the canvas to the doughnut-->
<canvas id="canvas" bind:this={assessment} width={300} height={300} />