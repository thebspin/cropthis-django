<template>
	<v-parallax min-height="333" :src="parallax">
		<v-content>
			<v-row resize="callback" justify="space-around">
				<v-col>
					<v-img :src="logo" height="80" contain></v-img>
					<div id="title">
						<h1>Free, easy to use online image cropping tool</h1>
					</div>
				</v-col>

				<v-col class="hidden-md-and-down">
					<video autoplay muted loop>
						<source src="/video.mp4">
					</video>
				</v-col>
			</v-row>
		</v-content>
	</v-parallax>
</template>

<script>
export default {
	name: "Header",

	data() {
		return {
			logo: require('../../public/logo.png'),
			parallax: require('../../public/parallax.png')
		}
	},

	methods: {
		callback() {
			console.log("a")
		}
	}
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat:100&display=swap');


#title {
	text-align: center;
	font-family: 'Montserrat', sans-serif;
	padding: 5em;
	font-size: 13px;
}

video {
	height: 270px;
	width: 540px;
	background-color: #242424; 
	padding: 1em;
}
</style>
