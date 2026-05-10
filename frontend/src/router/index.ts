import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import NoticeList from '@/views/NoticeList.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/notices', name: 'NoticeList', component: NoticeList }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
