<template>

	<v-container>
		<v-row justify="center">
			<v-card width="1200" color="#f5f5f5" shaped :class="{ disabled: imageURL }">
				<div v-if="!(image == null)" id="cancel-image" @click="clearImage">&times;</div>

				<div id="file-input-label" @click="clickInput" :style="{ backgroundImage: 'url(' + image + ')'  }">

					<font-awesome-icon :icon="['fas', 'camera']" />	
					<h2>Choose an Image</h2>

				</div>

				<input ref="fileInput" type="file" id="file-input" accept="image/*" @change="changeImage">
			</v-card>
		</v-row>

		<v-row justify="center">
			<h3>OR</h3>
		</v-row>

		<v-row justify="center">
			<v-text-field :disabled="!(image == null)" @change="transformImageURL" clearable v-model="imageURL" ref="URLInput" label="Upload from URL">
				<v-icon slot="prepend">mdi-link</v-icon>
			</v-text-field>
		</v-row>
	</v-container>
</template>

<script>
import axios from 'axios'

export default {
	name: "ChooseFile",

	methods: {
		clickInput() {
			if(!this.imageURL){
				this.$refs.fileInput.click()
			}
		},

		changeImage() {
			this.$store.commit('changeLoadingState', true)
			if(this.$refs.fileInput.files[0]) {
				this.$store.commit('changeImage', {
					value: URL.createObjectURL(this.$refs.fileInput.files[0]),
					fileName: this.$refs.fileInput.files[0].name.split('.')[0],
					fileType: this.$refs.fileInput.files[0].type.split('/').pop()
				})
			}
			this.$store.commit('changeLoadingState', false)
		},

		clearImage() {
			this.$store.commit('clearImage')
			this.$store.commit('changeLoadingState', null)
		},

		transformImageURL() {
			this.$store.commit('changeLoadingState', true)
			if(this.$refs.URLInput.value) {
				const params = new URLSearchParams()
				params.append('url', this.$refs.URLInput.value)
				axios({
					method: 'post',
					url: 'http://localhost:8000/create/',
					data: params
				}).then(response => { this.$store.commit('updateFromURL', response), this.$store.commit('changeLoadingState', false) })
			}
		}

	},

	computed: {
		image() {
			return this.$store.getters.image
		},

		imageURL: {
			get() {
				return this.$store.getters.imageURL
			},

			set(value) {
				this.$store.commit('updateImageURL', value)
			}
		}
	}

}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css?family=Montserrat:200&display=swap');

#file-input {
	display: none;
}

#file-input-label {
	height: 150px;
	transition: all 0.2s ease-in-out;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	align-items: center;
	cursor: pointer;
	padding: 1em;
	font-family: 'Montserrat', sans-serif;
	text-transform: uppercase;
	background-size: cover;
	background-repeat: no-repeat;
	background-position: 30%;

	&:hover {
		color: rgba(0, 0, 0, 0.3);
		background-color: white;
	}

	svg {
		font-size: 36px;
	}

	h2 {
		font-size: 14px;
	}
}

.row {
	h3 {
		color: grey;
	}

	.v-card {
		margin: 2em;
		transition: all 0.4s ease-in-out;

		#cancel-image {
			position: absolute;	
			right: 5px;
			top: 5px;
			cursor: pointer;
			font-size: 18px;
			background-color: #ff5349;
			color: white;
			padding: 0 9px;
			border-radius: 50%;
			transition: all 0.2s ease-in-out;
			
			&:hover {
				transform: scale(1.1);
			}
		}
	}

	.disabled {
		opacity: 0.3;
	}
}
</style>
