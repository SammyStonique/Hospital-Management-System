<template>
    <div class="sidebar fixed  pl-16 w-1/4 border-r-2 h-screen">
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
      <i class="fa fa-tachometer pt-2 mr-2" aria-hidden="true"></i>
      <p class="text-lg"><router-link to="/">Dashboard</router-link></p>
    </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
      <i class="fa fa-calendar pt-2 mr-2" aria-hidden="true"></i>
      <p class="text-lg"><router-link to="/appointments">Appointments</router-link></p>
    </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-building pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/departments">Departments</router-link></p>
      </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-user-md pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/doctors">Doctors</router-link></p>
      </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-universal-access pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/patients">Patients</router-link></p>
      </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-user-plus pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/staff">Our Staff</router-link></p>
      </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-cogs pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/settings">Settings</router-link></p>
      </button>
    </div>
    <div class="py-4 px-4">
      <button class="flex hover:px-6 hover:py-2 hover:bg-green-300 hover:border-2 hover:border-green-500 hover:rounded-lg">
        <i class="fa fa-sign-out pt-2 mr-2" aria-hidden="true"></i>
        <p class="text-lg"><router-link to="/logout">Log Out</router-link></p>
      </button>
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
</style>