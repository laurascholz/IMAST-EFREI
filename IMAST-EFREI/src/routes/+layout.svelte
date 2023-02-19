<script>
	import { page } from '$app/stores';
</script>

<div class="container">
	<nav>
		<ul>
			<li><strong>Cosmetic Checker</strong></li>
		</ul>
		<ul>
			<li><a href="/">Home</a></li>
			<li><a href="/about">About</a></li>
			<li><a href="/check">Ingredients Checker</a></li>
		</ul>
	</nav>
</div>

<main>
	<div class="container">
		<slot />
	</div>
</main>
