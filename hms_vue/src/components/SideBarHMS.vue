<template>
    <div class="sidebar fixed  w-1/6 h-screen">
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/">
          <button class="flex">
            <i class="fa fa-home pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Home Page</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/dashboard">
          <button class="flex">
            <i class="fa fa-tachometer pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Dashboard</p>
          </button>
        </router-link>
      </div> 
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/appointments">
          <button class="flex">
            <i class="fa fa-calendar pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Appointments</p>
          </button>
        </router-link>
      </div>
      <div class="web-links dropdown">
        <div class="py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
          <button class="flex" @click="showDepartmentDropdown">
              <i class="fa fa-building pt-2 mr-2" aria-hidden="true"></i>
              <p class="text-lg">Departments</p>
          </button>
        </div>
        <div class="dropdown-content pl-4" v-if="department_dropdown">
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/departments">
              <button class="flex text-sm">
                <i class="fa fa-building pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Departments List</p>
              </button>
              </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/managers">
              <button class="flex text-sm">
                <i class="fa fa-id-badge pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Department Managers</p>
              </button>
            </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/staff-rooms">
              <button class="flex text-sm">
                <i class="fa fa-cubes pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Staff Rooms</p>
              </button>
              </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/wards">
              <button class="flex text-sm">
                <i class="fa fa-university pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Wards</p>
              </button>
              </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/beds">
              <button class="flex text-sm">
                <i class="fa fa-bed pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Beds</p>
              </button>
              </router-link>
          </div>
        </div>
      </div>
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/doctors">
          <button class="flex">
            <i class="fa fa-user-md pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Doctors</p>
          </button>
        </router-link>
      </div>
      <div class="web-links dropdown">
        <div class="py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
          <button class="flex" @click="showPatientsDropdown">
              <i class="fa fa-universal-access pt-2 mr-2" aria-hidden="true"></i>
              <p class="text-lg">Patients</p>
          </button>
        </div>
        <div class="dropdown-content pl-4" v-if="patients_dropdown">
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/patients">
              <button class="flex text-sm">
                <i class="fa fa-universal-access pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Patients List</p>
              </button>
              </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/emergency-contacts">
              <button class="flex text-sm">
                <i class="fa fa-address-card pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Emergency Contacts</p>
              </button>
            </router-link>
          </div>
          <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
            <router-link to="/hms/patients-visits">
              <button class="flex text-sm">
                <i class="fa fa-address-book-o pt-2 mr-2" aria-hidden="true"></i>
                <p class="">Patient Visits</p>
              </button>
            </router-link>
          </div>
        </div>
      </div>
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/staff">
          <button class="flex">
            <i class="fa fa-user-plus pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Our Staff</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/lab-management">
          <button class="flex">
            <i class="fa fa-flask pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Lab Management</p>
          </button>
        </router-link>
      </div>
      <div class="web-links dropdown">
        <div class="py-2 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
            <button class="flex" @click="showFinancialsDropdown">
                <i class="fa fa-money pt-2 mr-2" aria-hidden="true"></i>
                <p class="text-lg">Financials</p>
            </button>
          </div>
          <div class="dropdown-content pl-4" v-if="financials_dropdown">
            <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
              <router-link to="/hms/medical-fees">
                <button class="flex text-sm">
                  <i class="fa fa-money pt-2 mr-2" aria-hidden="true"></i>
                  <p class="">Fees & Charges</p>
                </button>
              </router-link>
            </div>
            <div class="py-2 px-3 pl-4 bg-slate-400 w-full text-white hover:bg-slate-500 hover:w-full hover:text-black">
              <router-link to="/hms/invoices">
                <button class="flex text-sm">
                  <i class="fa fa-object-ungroup pt-2 mr-2" aria-hidden="true"></i>
                  <p class="">Invoices</p>
                </button>
              </router-link>
            </div>
          </div>
      </div>
      
      

  </div>
</template>

<script>

export default{
  data(){
    return{
      department_dropdown: false,
      patients_dropdown: false,
      financials_dropdown: false
    }
  },
  methods:{
    showDepartmentDropdown(){
      this.patients_dropdown = false;
      this.financials_dropdown = false;
      this.department_dropdown = !this.department_dropdown;
    },
    showPatientsDropdown(){
      this.department_dropdown = false;
      this.financials_dropdown = false;
      this.patients_dropdown = !this.patients_dropdown;
    },
    showFinancialsDropdown(){
      this.department_dropdown = false;
      this.patients_dropdown = false;
      this.financials_dropdown = !this.financials_dropdown;
    }
  }

}
</script>

<style>
.sidebar{
  z-index: 1;
  overflow-y: scroll;
}
.weblinks, .router-link-active{
  color: green
}
</style>