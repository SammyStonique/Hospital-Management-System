import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/HMS/DashboardView.vue'
import AppointmentsView from '../views/HMS/AppointmentsView.vue'
import DepartmentsView from '../views/HMS/DepartmentsView.vue'
import DoctorsView from '../views/HMS/DoctorsView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import PatientsView from '../views/HMS/PatientsView.vue'
import StaffView from '../views/HMS/StaffView.vue'
import PayrollView from '../views/HR/PayrollView.vue'
import AccountsView from '../views/FA/AccountsView.vue'
import LabManagementView from '../views/HMS/LabManagementView.vue'
import InventoryView from '../views/INV/InventoryView.vue'
import MyAccountView from '../views/HMS/MyAccountView.vue'
import ManagersView from '../views/HMS/ManagersView.vue'

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
    path: '/hms/dashboard',
    name: 'hms-dashboard',
    component: DashboardView,
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
    path: '/hms/appointments',
    name: 'hms-appointments',
    component: AppointmentsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/departments',
    name: 'hms-departments',
    component: DepartmentsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/managers',
    name: 'hms-managers',
    component: ManagersView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/doctors',
    name: 'hms-doctors',
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
    path: '/hms/patients',
    name: 'hms-patients',
    component: PatientsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/lab-management',
    name: 'hms-lab-management',
    component: LabManagementView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/staff',
    name: 'hms-staff',
    component: StaffView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hr/payroll',
    name: 'hr-payroll',
    component: PayrollView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/fa/accounts',
    name: 'fa-accounts',
    component: AccountsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/my-account',
    name: 'my-account',
    component: MyAccountView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/inv/inventory',
    name: 'inv-inventory',
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
