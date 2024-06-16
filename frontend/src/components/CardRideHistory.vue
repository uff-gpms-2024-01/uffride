<template>
	<q-card class="col" flat bordered>
		<q-card-section>
			<div class="text-h6 q-mb-xs">
				{{ ride.name }}
			</div>
			<div class="row no-wrap items-center">
				<q-rating
					size="18px"
					:model-value="ride.rating"
					:max="5"
					color="primary"
					readonly
				/>
				<span class="text-caption text-grey q-ml-sm"
					>{{ ride.rating }} ({{
						ride.ratingQuantity
					}})</span
				>
			</div>
		</q-card-section>

		<div class="row justify-center">
			<iframe
				class="col"
				width="825"
				height="350"
				src="https://www.openstreetmap.org/export/embed.html?bbox=-43.13751697540283%2C-22.91748813005501%2C-43.08155536651611%2C-22.886494722426438&amp;layer=mapnik"
				style="border: 1px solid black"
			></iframe>
		</div>

		<q-card-section class="q-pt-none q-mt-sm">
			<div class="text-subtitle1">
				De: {{ ride.where }}・ Para:
				{{ ride.toWhere }}
			</div>
			<div class="text">
				Lugares disponíveis:
				<span class="text-bold"
					>{{ ride.availablePlaces }}/{{
						ride.places
					}}</span
				>
			</div>
			<div class="text">
				Saída: Data
				<span claszs="text-bold">{{ ride.date }}</span> |
				Hora <span class="text-bold">{{ ride.hour }}</span>
			</div>
		</q-card-section>

		<q-card-actions class="justify-center">
			<q-btn flat color="primary" @click="assess = true">
				Avaliar
			</q-btn>
			<q-dialog v-model="assess" persistent>
				<q-card style="min-width: 350px">
					<q-card-section>
						<div class="text-h6">
							O que você achou da corrida?
						</div>
					</q-card-section>

					<q-card-section
						class="q-pt-none row justify-center"
					>
						<q-rating
							size="40px"
							v-model="userRating"
							:max="5"
							color="primary"
						/>
					</q-card-section>

					<q-card-actions
						align="right"
						class="text-primary"
					>
						<q-btn
							flat
							label="Avaliar"
							@click="toAssess"
							v-close-popup
						/>
					</q-card-actions>
				</q-card>
			</q-dialog>
		</q-card-actions>
	</q-card>
</template>

<script setup>
import { defineProps, ref } from 'vue';
import axios from 'axios';

const dialogReserver = ref(false);
const dialogConfirmReserver = ref(false);
const rideRequestDialog = ref(null);
const dialogDriveProfile = ref(null);
const assess = ref(0);
const userRating = ref('');
const props = defineProps({
	ride: {
		type: Object,
		required: true,
	},
	id: {
		type: Number,
		required: true,
	},
});

/**
 *
 * Fazer reserva
 * @param {*} element
 */
const reserver = (element) => {
	// @TODO chamar a api para fazer a reserva
	// axios.get('https://webhook.site/9b8728f1-c752-4950-b85c-6042ac7833dd')
	//   .then(response => {
	//     riceList = response.data;
	//   })
	//   .catch(error => {
	//     console.error(error);
	//   });
	dialogReserver.value = false;
	dialogConfirmReserver.value = true;
	// router.push("/");
};

const toAssess = (userRating) => {
	// @TODO chamar a api para guarda a avaliação
	// axios.get('https://webhook.site/9b8728f1-c752-4950-b85c-6042ac7833dd')
	//   .then(response => {
	//     ride.userRating = userRating;
	//   })
	//   .catch(error => {
	//     console.error(error);
	//   });
};
</script>
