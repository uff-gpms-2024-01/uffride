<template>
  <q-layout view="lHh Lpr lFf">
    <q-header bordered class="bg-grey-3 text-primary">
      <q-toolbar>
        <q-toolbar-title class="text-center">
          UFFRide
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

defineOptions({
  name: 'MainLayout'
})

const linksList = [
  {
    title: 'Pedir carona',
    caption: 'quasar.dev',
    icon: 'location_on',
    link: 'https://quasar.dev'
  },
  {
    title: 'Oferecer carona',
    caption: 'github.com/quasarframework',
    icon: 'near_me',
    link: 'https://github.com/quasarframework'
  },
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
