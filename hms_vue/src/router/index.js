import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AppointmentsView from '../views/AppointmentsView.vue'
import DepartmentsView from '../views/DepartmentsView.vue'
import DoctorsView from '../views/DoctorsView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import PatientsView from '../views/PatientsView.vue'
import SettingsView from '../views/SettingsView.vue'
import StaffView from '../views/StaffView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/appointments',
    name: 'appointments',
    component: AppointmentsView
  },
  {
    path: '/departments',
    name: 'departments',
    component: DepartmentsView
  },
  {
    path: '/doctors',
    name: 'doctors',
    component: DoctorsView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/patients',
    name: 'patients',
    component: PatientsView
  },
  {
    path: '/settings',
    name: 'settings',
    component: SettingsView
  },
  {
    path: '/staff',
    name: 'staff',
    component: StaffView
  },
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
