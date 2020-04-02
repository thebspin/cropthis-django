<template>
	<v-app>
		<v-app-bar
			app
			color="#323232"
			dark
			dense
			hide-on-scroll
		>
			<v-btn text href="/">HOME</v-btn>
		</v-app-bar>
		
		<v-content>
			<Header />
			<MetaInformation />
			<Steps />
			<Cards />
			<Footer />
		</v-content>
	</v-app>
</template>

<script>
import Header from './components/Header.vue'
import MetaInformation from './components/MetaInformation.vue'
import Steps from './components/Steps.vue'
import Cards from './components/Cards.vue'
import Footer from './components/Footer.vue'


export default {
	name: 'App',
	components: { Header, MetaInformation, Steps, Cards, Footer },

	data: () => ({
		//
	})
}
</script>


<style scoped>

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

#app {
}
</style>
