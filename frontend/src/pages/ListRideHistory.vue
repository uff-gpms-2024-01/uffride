<template>
	<q-page class="col-12 items-center">
		<div class="col-12 col-md-6 items-center">
			<div
				class="col items-center q-gutter-y-lg q-my-xl q-mx-lg q-px-lg"
			>
				<span
					class="row justify-center text-subtitle2 text-grey-9"
					>Carona em andamento</span
				>

				<span
					v-if="!rideCurrentList"
					class="row text-h1 text-grey-4"
				>
					Nada encontrado
				</span>

				<div
					class="row justify-center"
					:key="rideCurrentList.id"

				>
					<CardRideCurrent
						class="col-12 col-md-6"
						:ride="rideCurrentList"
						:rideId="rideCurrentList.id"
					/>
				</div>
			</div>

			<div
				class="col items-center col items-center q-gutter-y-lg q-my-xl q-mx-lg q-px-lg"
			>
				<span
					class="row justify-center text-subtitle2 text-grey-9"
					>Histórico</span
				>

				<span
					v-if="!rideList.length"
					class="row text-h1 text-grey-4"
				>
					Nada encontrado
				</span>

				<div
					class="row justify-center"
					v-for="ride in rideList"
					:key="ride.id"
				>
					<CardRideHistory
						:ride="ride"
						:id="4"
						class="col-12 col-md-6"
					/>
				</div>
			</div>
			<div class="q-my-md"></div>
		</div>
	</q-page>
</template>

<script setup lang="js">
import { ref, onBeforeMount } from 'vue';
import CardRideHistory from 'src/components/CardRideHistory.vue';
import CardRideCurrent from 'src/components/CardRideCurrent.vue';
import axios from 'axios';
import BASE_URL_API from 'src/constants/baseUrl';

const rideList = ref([]);
const rideCurrentList = ref([]);

/**
 * Faz requisição ao back end para pegar as corridas
 * @returns {object}
 */



 const getRideHitoryList = async () => {
	
	try {
		const response = await axios.get(BASE_URL_API + '/api/rides');
		if (response.status !== 200) {
			alert('Erro ao listar caronas');
			return;
		}
		return response.data;
	} catch (error) {
		console.error('Erro ao buscar dados:', error);
	}
};

/**
 * Faz requisição ao back end para pegar as corridas
 */
 const getRideCurrentList = async () => {
	
	try {
		const response = await axios.get(BASE_URL_API + '/api/ride/current');
		if (response.status !== 200) {
			alert('Erro ao listar caronas');
			return;
		}

		return response.data;
	} catch (error) {
		console.error('Erro ao buscar dados:', error);
	}
};

onBeforeMount( async () => {
	
  	rideList.value = await getRideHitoryList();
	rideCurrentList.value =  await getRideCurrentList();

});
</script>

<style scoped>
.bt-black {
	border-top: 0.001px solid rgba(128, 128, 128, 0.453);
}
</style>
