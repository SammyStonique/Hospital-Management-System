import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import AppointmentsView from '../views/AppointmentsView.vue'
import DepartmentsView from '../views/DepartmentsView.vue'
import DoctorsView from '../views/DoctorsView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import PatientsView from '../views/PatientsView.vue'
import StaffView from '../views/StaffView.vue'
import PayrollView from '../views/PayrollView.vue'
import AccountsView from '../views/AccountsView.vue'
import LabManagementView from '../views/LabManagementView.vue'
import InventoryView from '../views/InventoryView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/appointments',
    name: 'appointments',
    component: AppointmentsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/departments',
    name: 'departments',
    component: DepartmentsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/doctors',
    name: 'doctors',
    component: DoctorsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/patients',
    name: 'patients',
    component: PatientsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/lab-management',
    name: 'lab-management',
    component: LabManagementView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/staff',
    name: 'staff',
    component: StaffView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/payroll',
    name: 'payroll',
    component: PayrollView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/accounts',
    name: 'accounts',
    component: AccountsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/inventory',
    name: 'inventory',
    component: InventoryView,
    meta:{
      requireLogin: true
    }
  },
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
