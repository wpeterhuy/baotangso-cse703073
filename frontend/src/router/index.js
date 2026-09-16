import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
  { path: '/bao-tang', name: 'museum-list', component: () => import('../views/MuseumList.vue') },
  { path: '/bao-tang/:slug', name: 'museum-detail', component: () => import('../views/MuseumDetail.vue'), props: true },
  { path: '/tham-quan/:sceneId', name: 'panorama', component: () => import('../views/PanoramaViewer.vue'), props: true },
  { path: '/tour/:slug', name: 'tour-guide', component: () => import('../views/TourGuide.vue'), props: true },
  { path: '/luu-but', name: 'guestbook', component: () => import('../views/GuestbookView.vue') },
  { path: '/bo-suu-tap', name: 'collection', component: () => import('../views/CollectionView.vue'), meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', name: '404', component: () => import('../views/NotFound.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: () => ({ top: 0 }),
})

router.beforeEach(async (to) => {
  if (!to.meta.requiresAuth) return true
  try {
    const res = await fetch('/api/v1/me', { credentials: 'same-origin' })
    return res.ok ? true : { name: 'home', query: { canh_bao: 'can_dang_nhap' } }
  } catch {
    return { name: 'home', query: { canh_bao: 'can_dang_nhap' } }
  }
})

export default router
