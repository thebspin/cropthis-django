<template>
	<v-stepper v-model="e1">
		<v-stepper-header>
			<v-stepper-step :complete="e1 > 1" step="1">Choose a File</v-stepper-step>

			<v-divider></v-divider>

			<v-stepper-step :complete="e1 > 2" step="2">Choose Area</v-stepper-step>

			<v-divider></v-divider>

			<v-stepper-step step="3">Finalize</v-stepper-step>
		</v-stepper-header>

		<v-stepper-items>

			<v-stepper-content step="1">
				<ChooseFile />
				<v-btn :disabled="loading === null || loading === true" :loading="loading === true" color="primary" @click="e1 = 2; toggleReady()">Continue</v-btn>
			</v-stepper-content>

			<v-stepper-content step="2">
				<ImageCropper ref="imageCropper" v-if="ready" />
				<v-btn color="primary" @click="getResult(); e1 = 3">Crop Selection</v-btn>
			</v-stepper-content>

			<v-stepper-content step="3">
					<Result ref="result" />
					<v-btn color="primary" @click="download">Download</v-btn>
			</v-stepper-content>

		</v-stepper-items>

	</v-stepper>
</template>

<script>
import ChooseFile from './ChooseFile.vue'
import ImageCropper from './ImageCropper.vue'
import Result from './Result.vue'

export default {
	name: "Steps",
	components: { ChooseFile, ImageCropper, Result },

	data() {
		return {
			e1: 1
		}
	},

	methods: {
		toggleReady() {
			this.$store.commit('toggleReady')
		},

		getResult() {
			this.$refs.imageCropper.setResult()
		},

		download() {
			this.$refs.result.download()
		}
	},

	computed: {
		image() {
			return this.$store.getters.image
		},

		imageURL() {
			return this.$store.getters.imageURL
		},

		ready() {
			return this.$store.getters.ready
		},

		loading() {
			return this.$store.getters.loading
		}
	}
}
</script>

<style scoped lang="scss">
.v-stepper {
	width: 90%;
	margin: 5em auto;
	margin-bottom: 0;
}
</style>
