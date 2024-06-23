const routes = [
	{
		path: '/',
		component: () => import('layouts/MainLayout.vue'),
		children: [
			{ path: '', component: () => import('pages/IndexPage.vue') },
			{ path: '/profile', component: () => import('pages/ProfilePage.vue') },
			{ path: '/oferecer-carona', component: () => import('pages/RideOffer.vue') },
			{ path: '/lista-caronas', component: () => import('pages/ListRidePage.vue') },
			{ path: '/carona/lista/oferecer', component: () => import('pages/ListOfferRide.vue') },
			{ path: '/carona/lista/history', component: () => import('pages/ListRideHistory.vue') }
		],
		meta: { requiresAuth: true }
	},

	{
		path: '/login',
		component: () => import('layouts/AuthenticateLayout.vue'),
		children: [
			{ path: '', component: () => import('pages/LoginPage.vue') }
		],

	},

	{
		path: '/cadastro',
		component: () => import('layouts/AuthenticateLayout.vue'),
		children: [
			{ path: '', component: () => import('pages/RegistroPage.vue') }
		],
	},

	// Always leave this as last one,
	// but you can also remove it
	{
		path: '/:catchAll(.*)*',
		component: () => import('pages/ErrorNotFound.vue')
	},
];

export default routes;
