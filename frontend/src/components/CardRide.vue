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
				Saída:
				Data <span class="text-bold">{{ ride.date }}</span>
				|
				Hora <span class="text-bold">{{ ride.hour }}</span>
			</div>
		</q-card-section>

		<q-separator />
		<q-card-actions>
			<q-btn
				flat
				color="primary"
				@click="dialogReserver = true"
			>
				Reservar carona
			</q-btn>
			<q-dialog v-model="dialogReserver">
				<q-card>
					<q-card-section>
						<div class="text-h6">
							Deseja reservar essa carona?
						</div>
					</q-card-section>

					<q-card-actions align="right">
						<q-btn
							flat
							label="Não"
							color="primary"
							v-close-popup
						/>
						<q-btn
							flat
							label="Sim"
							color="primary"
							@click="reserver"
						/>
					</q-card-actions>
				</q-card>
			</q-dialog>

			<q-dialog v-model="dialogConfirmReserver">
				<q-card>
					<q-card-section>
						<div class="text-h6">Reserva confirmada!</div>
					</q-card-section>

					<q-card-actions align="right">
						<q-btn
							flat
							label="OK"
							color="primary"
							:to="'/'"
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
const props = defineProps({
	ride: {
		type: Object,
		required: true,
	},
	rideId: {
		type: Number,
		required: true
	}
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
</script>
