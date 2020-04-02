<template>
	<v-container>
		<div class="image-container">
			<img ref="image" :src="source">
		</div>
	
		<v-row justify="space-around" class="mt-5">
			<v-btn @click="reset" title="Reset" fab><v-icon>mdi-power</v-icon></v-btn>
			<v-btn @click="rotateCounterClockwise" title="Rotate Left" fab><v-icon>mdi-rotate-left</v-icon></v-btn>
			<v-btn @click="rotateClockwise" title="Rotate Right" fab><v-icon>mdi-rotate-right</v-icon></v-btn>
			<v-btn @click="flipX" title="Flip Horizontally" fab><v-icon>mdi-flip-horizontal</v-icon></v-btn>
			<v-btn @click="flipY" title="Flip Vertically" fab><v-icon>mdi-flip-vertical</v-icon></v-btn>
		</v-row>
	</v-container>
</template>

<script>
import Cropper from 'cropperjs'
import 'cropperjs/dist/cropper.css'

export default {
	name: "ImageCropper",
	data() {
		return {
			cropper: null,
			imageElement: null
		}
	},

	mounted() {
		this.imageElement = this.$refs.image
		this.cropper = new Cropper(this.imageElement, {
				zoomable: true,
				scalable: true,
				background: true,
				aspectRatio: 0,
		})

	},

	computed: {
		source() {
			return this.$store.getters.image
		},

		fileType() {
			return this.$store.getters.fileType
		}
	},

	methods: {
		rotateClockwise() {
			this.cropper.rotate(10)
		},

		rotateCounterClockwise() {
			this.cropper.rotate(-10)
		},

		reset() {
			this.cropper.reset()
		},

		flipX() {
			this.cropper.scaleX(this.cropper.getImageData().scaleX === 1 ? -1 : 1)
		},

		flipY() {
			this.cropper.scaleY(this.cropper.getImageData().scaleY === 1 ? -1 : 1)
		},

		setResult() {
			this.$store.commit('changeResult', this.cropper.getCroppedCanvas().toDataURL(this.fileType))
		}
	}
}
</script>

<style lang="scss">
.image-container {

	img {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
}

.v-btn {
	margin-bottom: 5px;
}
</style>
