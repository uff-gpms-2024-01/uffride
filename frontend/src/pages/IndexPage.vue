<template>
	<q-page class="flex flex-center column">
		<h1 class="text-h4">Pedir carona</h1>
		<div class="row justify-center full-width map">
			<iframe
				width="425"
				height="350"
				src="https://www.openstreetmap.org/export/embed.html?bbox=-43.13751697540283%2C-22.91748813005501%2C-43.08155536651611%2C-22.886494722426438&amp;layer=mapnik"
				style="border: 1px solid black"
			></iframe>
		</div>

		<q-form
			@submit="handleOnSubmit"
			class="q-gutter-md full-width q-mt-sm"
		>
			<div class="row justify-center">
				<q-select
					rounded
					outlined
					v-model="fromWhere"
					use-input
					hide-selected
					fill-input
					input-debounce="0"
					label="De onde?"
					:options="locateOptions"
					@filter="filterFn"
					behavior="menu"
					:rules="[
						(val) => !!val || 'Campo não pode está vazio',
					]"
				>
					<template v-slot:prepend>
						<q-icon name="adjust" />
					</template>

					<template v-slot:append>
						<q-icon
							name="close"
							@click="text = ''"
							class="cursor-pointer"
						/>
					</template>

					<template v-slot:no-option>
						<q-item>
							<q-item-section class="text-grey">
								No results
							</q-item-section>
						</q-item>
					</template>
				</q-select>
			</div>

			<div class="row justify-center">
				<q-select
					rounded
					outlined
					v-model="toWhere"
					use-input
					input-debounce="0"
					label="Para onde?"
					:options="locateOptions"
					@filter="filterFn"
					behavior="menu"
					:rules="[
						(val) => !!val || 'Campo não pode está vazio',
					]"
				>
					<template v-slot:prepend>
						<q-icon name="location_on" />
					</template>

					<template v-slot:append>
						<q-icon
							name="close"
							@click="text = ''"
							class="cursor-pointer"
						/>
					</template>

					<template v-slot:no-option>
						<q-item>
							<q-item-section class="text-grey">
								No results
							</q-item-section>
						</q-item>
					</template>
				</q-select>
			</div>

			<div class="row justify-center">
				<q-input
					rounded
					outlined
					v-model="rideDate"
					:disable="nowRice"
					class="w-100"
				>
					<template v-slot:prepend>
						<q-icon name="event" class="cursor-pointer">
							<q-popup-proxy
								cover
								transition-show="scale"
								transition-hide="scale"
							>
								<q-date
									v-model="rideDate"
									mask="DD/MM/YYYY HH:mm"
									:options="optionsFn"
								>
									<div class="row items-center justify-end">
										<q-btn
											v-close-popup
											label="Close"
											color="primary"
											flat
										/>
									</div>
								</q-date>
							</q-popup-proxy>
						</q-icon>
					</template>

					<template v-slot:append>
						<q-icon
							name="access_time"
							class="cursor-pointer"
						>
							<q-popup-proxy
								cover
								transition-show="scale"
								transition-hide="scale"
							>
								<q-time
									v-model="rideDate"
									mask="DD/MM/YYYY HH:mm"
									format24h
									:hour-options="hourOptionsTime1"
									:minute-options="minuteOptionsTime1"
									:second-options="secondOptionsTime1"
								>
									<div class="row items-center justify-end">
										<q-btn
											v-close-popup
											label="Close"
											color="primary"
											flat
										/>
									</div>
								</q-time>
							</q-popup-proxy>
						</q-icon>
					</template>
				</q-input>
			</div>

			<div class="row justify-center">
				<q-toggle v-model="nowRice" label="Para agora?" />
			</div>

			<div class="row justify-center">
				<div class="col-3 col-md-1">
					<span>Selecione a quantidade de passageiros:</span>
					<q-slider
									v-model="passengersNumber"
									marker-labels
									:min="1"
									:max="4"
								/>
								<q-btn
						label="Continuar"
						type="submit"
						color="primary"
						class="full-width"
					/>
				</div>
			</div>
		</q-form>
	</q-page>
</template>

<script setup>
import { ref } from 'vue';
import { useRideRequestStore } from 'src/stores/RideRequestStore';
import { useRouter } from 'vue-router';
import axios from 'axios';
import LOCALS from 'src/constants/locals';
import baseUrl from 'src/constants/baseUrl';

defineOptions({
	name: 'IndexPage',
});

const router = useRouter();
const fromWhere = ref('');
const toWhere = ref('');
const stepNext = ref(false);
/**
 * Carona para agora?
 */
const nowRice = ref(false);
const passengersNumber = ref(1);
const currentDate = new Date();

const locateOptions = ref(LOCALS.map((local) => local.name));
const setModel = ref('');

const formattedCurrentDate = `${currentDate.getDate()}/${currentDate.getMonth()}/${currentDate.getFullYear()}`;

const rideDate = ref(formattedCurrentDate + ' 09:00');
const hourOptionsTime1 = [9, 10, 11, 12, 13, 14, 15, 16];
const minuteOptionsTime1 = [0, 15, 30, 45];

/**
 *
 * Pega as opções de data
 * @param {*} date
 */
const optionsFn = (date) => {
	const selectedDate = new Date(date);
	const currentDate = new Date();

	const isSameYear =
		selectedDate.getFullYear() ===
		currentDate.getFullYear();
	const isSameMonth =
		selectedDate.getMonth() === currentDate.getMonth();

	if (isSameYear && isSameMonth) {
		return selectedDate.getDate() >= currentDate.getDate();
	} else if (
		isSameYear &&
		selectedDate.getMonth() > currentDate.getMonth()
	) {
		return true;
	} else {
		return false;
	}
};


const handleOnSubmit = () => {
let data = {
	where_address: fromWhere.value,
	where_lat: LOCALS.find((local) => local.name === fromWhere.value).latitude,
	where_long: LOCALS.find((local) => local.name === fromWhere.value).longitude,
	to_where_address: toWhere.value,
	to_where_lat: LOCALS.find((local) => local.name === toWhere.value).latitude,
	to_where_long: LOCALS.find((local) => local.name === toWhere.value).longitude,
	number_of_passengers: passengersNumber.value,
	user_id: window.localStorage.getItem("user_id")
};
requestRide(data);

};
const requestRide = async (data) => {
try {
	const response = await axios.post(baseUrl + '/api/ride/request', data);
	if (response.status !== 201) {
		alert('Erro ao requisitar carona');
		return;
	}
	alert('Carona requisitada com sucesso!');
	router.push('/carona/lista/history');
} catch (error) {
	console.error('Erro ao buscar dados:', error);
}
};

</script>

<style>
.map {
	height: 40vh;
}

.w-100 {
	padding: 0px 30px 0px 30px;
}
</style>
