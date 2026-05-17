import { createRouter, createWebHistory } from 'vue-router'
import NoticeList from './components/NoticeList.vue'
import NoticeDetail from './components/NoticeDetail.vue'

const routes = [
  { path: '/', name: 'NoticeList', component: NoticeList },
  { path: '/notice/:id', name: 'NoticeDetail', component: NoticeDetail, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
