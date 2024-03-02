<template>
    <div class="sidebar fixed  w-1/6 h-screen">
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/">
          <button class="flex">
            <i class="fa fa-home pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Home Page</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/dashboard">
          <button class="flex">
            <i class="fa fa-tachometer pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Dashboard</p>
          </button>
        </router-link>
      </div> 
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/appointments">
          <button class="flex">
            <i class="fa fa-calendar pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Appointments</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/departments">
          <button class="flex">
            <i class="fa fa-building pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Departments</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/doctors">
          <button class="flex">
            <i class="fa fa-user-md pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Doctors</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/patients">
          <button class="flex">
            <i class="fa fa-universal-access pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Patients</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/staff">
          <button class="flex">
            <i class="fa fa-user-plus pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Our Staff</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/hms/lab-management">
          <button class="flex">
            <i class="fa fa-flask pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Lab Management</p>
          </button>
        </router-link>
      </div>
      

  </div>
</template>

<script>
export default{

}
</script>

<style>
.sidebar{
  z-index: 1;
}
.weblinks, .router-link-active{
  color: green
}
</style>