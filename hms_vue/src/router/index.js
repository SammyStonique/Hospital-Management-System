import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/HMS/DashboardView.vue'
import AppointmentsView from '../views/HMS/AppointmentsView.vue'
import DepartmentsView from '../views/HMS/DepartmentsView.vue'
import ManagersView from '../views/HMS/ManagersView.vue'
import StaffRoomsView from '../views/HMS/StaffRoomsView.vue'
import WardsView from '../views/HMS/WardsView.vue'
import BedsView from '../views/HMS/BedsView.vue'
import DoctorsView from '../views/HMS/DoctorsView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import PatientsView from '../views/HMS/PatientsView.vue'
import EmergencyContactsView from '../views/HMS/EmergencyContactsView.vue'
import PatientsVisitsView from '../views/HMS/PatientsVisitsView.vue'
import StaffView from '../views/HMS/StaffView.vue'
import PayrollView from '../views/HR/PayrollView.vue'
import LabManagementView from '../views/HMS/LabManagementView.vue'
import MedicalFeesView from '../views/HMS/MedicalFeesView.vue'
import InventoryView from '../views/INV/InventoryView.vue'
import MyAccountView from '../views/HMS/MyAccountView.vue'
import FADashboardView from '../views/FA/FADashboardView.vue'
import ChartOfAccountsView from '../views/FA/ChartOfAccountsView.vue'
import ClientCategoryView from '../views/FA/ClientCategoryView.vue'
import JournalsView from '../views/FA/JournalsView.vue'

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
    path: '/hms/staff-rooms',
    name: 'hms-staff-rooms',
    component: StaffRoomsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/wards',
    name: 'hms-wards',
    component: WardsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/beds',
    name: 'hms-beds',
    component: BedsView,
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
    path: '/hms/emergency-contacts',
    name: 'hms-emergency-contacts',
    component: EmergencyContactsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/hms/patients-visits',
    name: 'hms-patients-visits',
    component: PatientsVisitsView,
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
    path: '/hms/medical-fees',
    name: 'hms-medical-fees',
    component: MedicalFeesView,
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
    path: '/fa/chart-of-accounts',
    name: 'fa-chart-of-accounts',
    component: ChartOfAccountsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/fa/client-categories',
    name: 'fa-client-categories',
    component: ClientCategoryView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/fa/journals',
    name: 'fa-journals',
    component: JournalsView,
    meta:{
      requireLogin: true
    }
  },
  {
    path: '/fa/dashboard',
    name: 'fa-dashboard',
    component: FADashboardView,
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
