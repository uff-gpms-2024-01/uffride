<template>
	<q-page class="flex column">
		<div class="row justify-center full-width map">
			<div
				class="row justify-center q-gutter-y-lg q-my-xl q-mx-lg"
			>
				<span class="text-subtitle2 text-grey-9"
					>Carona em andamento</span
				>

				<span
					v-if="!rideCurrentList.length"
					class="text-h1 text-grey-4"
				>
					Nada encontrado
				</span>

				<div
					class="row full-width"
					v-for="ride in rideCurrentList"
					:key="ride.id"
				>
					<CardRideCurrent :ride="ride" :rideId="ride.id" />
				</div>
			</div>

			<div
				class="row justify-center q-gutter-y-lg q-my-xl q-mx-lg"
			>
				<span class="text-subtitle2 text-grey-9"
					>Histórico</span
				>

				<span
					v-if="!rideList.length"
					class="text-h1 text-grey-4"
				>
					Nada encontrado
				</span>

				<div
					class="row full-width"
					v-for="ride in rideList"
					:key="ride.id"
				>
					<CardRideHistory :ride="ride" />
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
