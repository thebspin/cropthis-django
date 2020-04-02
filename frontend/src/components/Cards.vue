<template>
	<v-row justify="space-around" class="ma-10">

		<v-card width="350px" class="pa-4" outlined>
			<v-list-item-group>
				<v-card-subtitle>Advice Bumblebee</v-card-subtitle>
				<v-divider></v-divider>
				<v-list-item>
					<v-list-item-avatar>
						<v-img src="/bee.png"></v-img>
					</v-list-item-avatar>
					<v-list-item-content>Use your mouse wheel to zoom in/out of the image</v-list-item-content>
				</v-list-item>
			</v-list-item-group>
		</v-card>

		<v-card width="350px" class="pa-4" outlined>
			<v-list-item-group>
				<v-card-subtitle>More Tips</v-card-subtitle>
				<v-divider></v-divider>
				<v-list-item>
					<v-list-item-content>
						Hold shift key while resizing to keep the aspect ratio fixed. 
					</v-list-item-content>
				</v-list-item>
				<v-list-item>
					<v-list-item-content>
						Double click the image to move it around
					</v-list-item-content>
				</v-list-item>
			</v-list-item-group>
		</v-card>

		<v-card width="350px" class="pa-4" outlined>
			<v-list-item-group>
				<v-card-subtitle>Shill Frog</v-card-subtitle>
				<v-divider></v-divider>
				<v-list-item>
					<v-list-item-avatar>
						<v-img src="/shill.png"></v-img>
					</v-list-item-avatar>

					<v-list-item-content>
						Cropthis is a great online image cropping tool that focuses on speed and efficiency without sacrificing quality.
					</v-list-item-content>
				</v-list-item>
			</v-list-item-group>
		</v-card>



	</v-row>
</template>


<style scoped lang="scss">
.v-card {
	margin: 1em; 
}
</style>
