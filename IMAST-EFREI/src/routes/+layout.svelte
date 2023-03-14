<script>
	import { page } from '$app/stores';
	
</script>

<div class="container">
	<nav>
		<ul>
			<li><strong>COSMETIC CHECKER </strong> </li>
		</ul>
		<ul>
			<li><a href="/">Home</a></li>
			<li><a href="/about">About</a></li>
			<!--
			<li><a href="/product">Ingredients Checker</a></li> -->
		</ul>
	</nav>
</div>

<main>
	<div class="container">
		<slot />
	</div>
</main>


<style>
	/* here CSS code for purple */
	:root:not([data-theme="dark"]) {
 	--primary: #8e24aa;
  	--primary-hover: #7b1fa2;
 	--primary-focus: rgba(142, 36, 170, 0.125);
  	--primary-inverse: #FFF;
	}
	nav{
		display: flex;
    	justify-content: right;
	}
	li {
		color:darkmagenta;
	}
	strong {
		color:darkmagenta;
		
	}
	a {
		color:dimgray;
	}
	
</style>