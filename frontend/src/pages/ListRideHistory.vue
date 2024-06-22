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
					v-if="!rideCurrentList.length"
					class="row text-h1 text-grey-4"
				>
					Nada encontrado
				</span>

				<div
					class="row justify-center"
					v-for="ride in rideCurrentList"
					:key="ride.id"
				>
					<CardRideCurrent
						class="col-12 col-md-6"
						:ride="ride"
						:rideId="ride.id"
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

const rideList = ref([]);
const rideCurrentList = ref([]);

/**
 * Faz requisição ao back end para pegar as corridas
 * @returns {object}
 */
 const getRideHitoryList = () => {
  // axios.get('https://webhook.site/9b8728f1-c752-4950-b85c-6042ac7833dd')
  //   .then(response => {
  //     riceList = response.data;
  //   })
  //   .catch(error => {
  //     console.error(error);
  //   });
    const esperado = `{
  "data": [
    {
      "id": 1,
      "name": "Afredo",
      "where": "***",
      "toWhere": "***",
			"userRating": 2,
      "rating": 5,
      "ratingQuantity": 15,
      "availablePlaces": 4,
      "places": 4,
			"date" : "13-01-2001",
			"hour": "09:30"
    },
    {
      "id": 2,
      "name": "Juberto",
      "where": "***",
      "toWhere": "***",
			"userRating": 4,
      "rating": 3,
      "ratingQuantity": 50,
      "availablePlaces": 3,
      "places": 4,
			"date" : "13-01-2001",
			"hour": "09:30"
    }
  ]
}`;
  return JSON.parse(esperado);
};

/**
 * Faz requisição ao back end para pegar as corridas
 * @returns {object}
 */
 const getRideCurrentList = () => {
  // axios.get('https://webhook.site/9b8728f1-c752-4950-b85c-6042ac7833dd')
  //   .then(response => {
  //     riceList = response.data;
  //   })
  //   .catch(error => {
  //     console.error(error);
  //   });
    const esperado = `{
  "data": [
    {
      "id": 1,
      "name": "Afredo",
      "where": "***",
      "toWhere": "***",
      "rating": 5,
      "ratingQuantity": 15,
      "availablePlaces": 4,
      "places": 4,
			"date" : "13-02-2025",
			"hour": "09:30"
    }
  ]
}`;
  return JSON.parse(esperado);
};

onBeforeMount(() => {
  rideList.value = getRideHitoryList().data;
	rideCurrentList.value = getRideCurrentList().data;
});
</script>

<style scoped>
.bt-black {
	border-top: 0.001px solid rgba(128, 128, 128, 0.453);
}
</style>
