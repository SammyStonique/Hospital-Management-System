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
        <router-link to="/dashboard">
          <button class="flex">
            <i class="fa fa-tachometer pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Dashboard</p>
          </button>
        </router-link>
      </div> 
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/departments">
          <button class="flex">
            <i class="fa fa-building pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Departments</p>
          </button>
        </router-link>
      </div>
      <div class="web-links py-3 px-3 pl-4 hover:bg-slate-500 hover:rounded hover:w-full">
        <router-link to="/inventory">
          <button class="flex">
            <i class="fa fa-wrench pt-2 mr-2" aria-hidden="true"></i>
            <p class="text-lg">Inventory</p>
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