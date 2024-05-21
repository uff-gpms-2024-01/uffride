<template>
  <q-page class="flex column">
    <div class="row justify-center full-width map">
      <div class="row justify-center q-mt-sm q-gutter-x-sm">
        <div class="col">
          <q-select
            rounded
            outlined
            v-model="where"
            use-input
            input-debounce="0"
            label="De onde?"
            :options="options"
            @filter="filterFn"
            behavior="menu"
          >
            <template v-slot:prepend>
              <q-icon name="adjust" />
            </template>

            <template v-slot:append>
              <q-icon name="close" @click="text = ''" class="cursor-pointer" />
            </template>

            <template v-slot:no-option>
              <q-item>
                <q-item-section class="text-grey"> No results </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <div class="col">
          <q-select
            rounded
            outlined
            v-model="toWhere"
            use-input
            input-debounce="0"
            label="Para onde?"
            :options="options"
            @filter="filterFn"
            behavior="menu"
          >
            <template v-slot:prepend>
              <q-icon name="location_on" />
            </template>

            <template v-slot:append>
              <q-icon name="close" @click="text = ''" class="cursor-pointer" />
            </template>

            <template v-slot:no-option>
              <q-item>
                <q-item-section class="text-grey"> No results </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <div class="col">
          <q-input rounded outlined v-model="rideDate" :disable="nowRice">
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
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
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
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>

        <div class="col-2 content-center">
          <q-toggle v-model="nowRice" label="Para agora?" />
        </div>
      </div>

      <div class="row justify-center q-gutter-y-lg q-my-xl">
        <div class="row full-width" v-for="ride in rideList" :key="ride.id">
          <q-card class="col" flat bordered>
            <q-card-section>
              <div class="text-h6 q-mb-xs">{{ ride.name }}</div>
              <div class="row no-wrap items-center">
                <q-rating
                  size="18px"
                  v-model="ride.rating"
                  :max="5"
                  color="primary"
                  readonly
                />
                <span class="text-caption text-grey q-ml-sm"
                  >{{ ride.rating }} ({{ ride.ratingQuantity }})</span
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
                De: {{ ride.where }}・ Para: {{ ride.toWhere }}
              </div>
              <div class="text">
                Lugares disponíveis:
                <span class="text-bold"
                  >{{ ride.availablePlaces }}/{{ ride.places }}</span
                >
              </div>
            </q-card-section>

            <q-separator />
            <q-card-actions>
              <q-btn flat color="primary" @click="dialogReserver = true"> Reservar carona </q-btn>
              <q-dialog v-model="dialogReserver">
                <q-card>
                  <q-card-section>
                    <div class="text-h6">Deseja reservar essa carona?</div>
                  </q-card-section>

                  <q-card-actions align="right">
                    <q-btn flat label="Não" color="primary" v-close-popup />
                    <q-btn flat label="Sim" color="primary" @click="reserver" />
                  </q-card-actions>
                </q-card>
              </q-dialog>

              <q-dialog v-model="dialogConfirmReserver">
                <q-card>
                  <q-card-section>
                    <div class="text-h6">Reserva confirmada!</div>
                  </q-card-section>

                  <q-card-actions align="right">
                    <q-btn flat label="OK" color="primary" :to="'/'" />
                  </q-card-actions>
                </q-card>
              </q-dialog>
            </q-card-actions>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="js">
import { ref, onMounted, onBeforeMount } from 'vue';
import { useRideRequestStore } from 'src/stores/RideRequestStore';
import {  useRouter } from "vue-router";

import axios from 'axios';

const router = useRouter();
const rideRequestStore = ref(useRideRequestStore());
const nowRice = ref(rideRequestStore.value.nowRice);
const rideDate = ref(rideRequestStore.value.rideDate);
const toWhere = ref(rideRequestStore.value.toWhere);
const where = ref(rideRequestStore.value.where);
const rideList = ref([]);
const dialogReserver = ref(false);
const dialogConfirmReserver = ref(false);

/**
 * Faz requisição ao back end para pegar as corridas
 * @returns {object}
 */
const getRideList = () => {
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
      "places": 4
    },
    {
      "id": 2,
      "name": "Juberto",
      "where": "***",
      "toWhere": "***",
      "rating": 5,
      "ratingQuantity": 50,
      "availablePlaces": 3,
      "places": 4
    }
  ]
}`;
  return JSON.parse(esperado);
};


const reserver = (element) => {
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

onBeforeMount(() => {
  rideList.value = getRideList().data;
});
</script>
