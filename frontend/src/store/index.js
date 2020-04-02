import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		image: null,
		imageURL: null,
		fileName: null,
		fileType: null,
		ready: false,
		loading: null,
		result: null
	},

	mutations: {
		changeImage(state, object) {
			state.image = object.value 
			state.fileName = object.fileName
			state.fileType = object.fileType
		},

		updateFromURL(state, object) {
			state.image = object.data.media
			state.fileName = object.data.filename
			state.fileType = object.data.filetype
		},

		updateImageURL(state, value) {
			state.imageURL = value
		},

		clearImage(state) {
			state.image = null
			state.imageURL = null
		},

		toggleReady(state) {
			state.ready = true
		},

		changeResult(state, value) {
			state.result = value
		},

		changeLoadingState(state, value) {
			state.loading = value
		}
	},

	actions: {
	},

	modules: {
	},

	getters: {
		image: state => state.image,
		imageURL: state => state.imageURL,
		ready: state => state.ready,
		result: state => state.result,
		loading: state => state.loading, 
		fileName: state => state.fileName,
		fileType: state => state.fileType
	}
})
