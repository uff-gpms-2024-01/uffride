<template>
	<q-layout view="lHh Lpr lFf">
		<q-header bordered class="bg-grey-3 text-primary">
			<q-toolbar>
				<q-btn
					flat
					dense
					round
					icon="menu"
					aria-label="Menu"
					@click="toggleLeftDrawer"
				/>

				<q-toolbar-title class="text-center">
					<RouterLink to="/">UFF Ride</RouterLink>
				</q-toolbar-title>
			</q-toolbar>
		</q-header>

		<q-drawer
			v-model="leftDrawerOpen"
			show-if-above
			bordered
			class="flex justify-between column"
		>
			<q-list>
				<q-item-label header> Menu </q-item-label>

				<EssentialLink
					v-for="link in linksList"
					:key="link.title"
					v-bind="link"
				/>
			</q-list>

			<q-list>
				<EssentialLink
					v-for="link in settingsList"
					:key="link.title"
					v-bind="link"
				/>
			</q-list>
		</q-drawer>

		<q-page-container>
			<router-view />
		</q-page-container>
	</q-layout>
</template>

<script setup>
import { ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';

defineOptions({
	name: 'MainLayout',
});

const linksList = [
	{
		title: 'Pedir carona',
		caption: 'quasar.dev',
		icon: 'location_on',
		link: '/',
	},
	{
		title: 'Oferecer carona',
		caption: 'github.com/quasarframework',
		icon: 'near_me',
		link: '#/oferecer-carona',
	},
];

const settingsList = [
	{
		title: 'Histórico de caronas',
		caption: 'github.com/quasarframework',
		icon: 'history',
		link: '#/carona/lista/history',
	},
	{
		title: 'Meu perfil',
		caption: '',
		icon: 'account_circle',
		link: '#/profile',
	},
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
	leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>

<style>
a {
	color: unset;
	text-decoration: none;
}
.space {
	margin-top: auto;
}
</style>
