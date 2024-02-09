<template>
<div class="navbar fixed flex z-30 top-0 w-full sticky-navbar bg-white border-b border-slate-300 shadow-sm shadow-slate-200 px-12 py-2">
  <div class="w-1/4 flex">
    <div class="w-12 h-12 rounded-full">
      <img src="@/assets/download.png" alt="Logo" class="">
    </div>
    <div class="ml-4">
      <h4 class="text-2xl py-2">K.H.S</h4>
    </div>               
  </div>
  <div class="w-2/4 py-2 flex">
    <div class="w-1/2">
      <h5 class="bold text-2xl">Dashboard</h5>
    </div>
    <div class="relative w-1/2 grid justify-items-center">   
      <input type="search" name="" id="" class="relative rounded-sm w-full text-xs border border-gray-300 px-8 h-8 bg-gray-100" placeholder="Search here..">
      <i class="fa fa-search absolute left-0 p-2" aria-hidden="true"></i>
    </div>
  </div>
  <div class="w-1/4 flex">
    <div class="w-1/4 grid justify-items-center py-2">
      <i class="fa fa-bell text-2xl" aria-hidden="true"></i>
    </div>
    <div class="w-3/4 flex">
      <div class="w-1/4 grid justify-items-end">
        <div class="rounded-full h-11 pb-5 w-11  mr-3 overflow-hidden border-2 border-white hover:border-2 hover:border-blue-400 hover:opacity-50 hover:shadow-2 hover:shadow-2xl">
            <button>
              <img src="./../assets/profile.jpg" alt="Profile Pic" class="w-full h-full object-cover"/>
            </button>
        </div>
      </div>
      <div class="w-3/4 pt-2 flex">
        <div class="w-3/4">
          <p class="font-bold text-sm">Otieno Samuel</p>
          <p class="text-xs">Admin</p>
        </div>
        <div class="w-1/4">
          <i class="fa fa-caret-down" aria-hidden="true"></i>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default{

}
</script>

<style>
.navbar{
  z-index: 1;
}
</style>