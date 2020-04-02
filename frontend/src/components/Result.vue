<template>
	<v-container v-if="result">
		<v-img :src="result" height="400px" contain></v-img>
	</v-container>
</template>

<script>
import download from 'downloadjs'

export default {
	name: "Result",

	computed: {
		result() {
			return this.$store.getters.result
		},

		fileName() {
			return this.$store.getters.fileName 
		},

		fileType() {
			return this.$store.getters.fileType
		},

		downloadName() {
			return this.fileName + "-cropthis." + this.fileType
		}
	},

	methods: {
		download() {
			download(this.result, this.downloadName)
		}
	}
}
</script>

<style scoped lang="scss">
</style>
