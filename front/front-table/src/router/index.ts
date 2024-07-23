import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import TableView from '../views/TableView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },{
    path:'/table',
    name: 'table',
    component: TableView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
