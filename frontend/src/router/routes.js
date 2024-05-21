const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/profile', component: () => import('pages/ProfilePage.vue') },
      { path: '/hitch-ride', component: () => import('pages/HitchRide.vue') },
      { path: '/lista-caronas', component: () => import('pages/ListRidePage.vue') }
    ]
  },

  {
    path: '/login',
    component: () => import('layouts/AuthenticateLayout.vue'),
    children: [
      { path: '', component: () => import('pages/LoginPage.vue') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  },
  {
    path: '/login',
    component: () => import('pages/LoginPage.vue')
  }
]

export default routes
