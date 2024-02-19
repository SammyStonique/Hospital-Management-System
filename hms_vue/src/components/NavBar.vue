<template>
<div class="navbar fixed flex z-30 top-0 w-full sticky-navbar bg-white border-b border-slate-300 shadow-sm shadow-slate-200 px-12 py-2">
  <div class="w-1/4 flex">
    <div class="w-12 h-12 rounded-full">
      <img src="@/assets/logo.jpeg" alt="Logo" class="">
    </div>
    <div class="ml-4">
      <h4 class="text-2xl py-2">K.H.S</h4>
    </div>               
  </div>
  <div class="w-2/4 py-2 flex">
    <div class="w-1/2">
      <h5 class="bold text-2xl">{{title}}</h5>
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
      <div class="w-3/4 pt-2 dropdown">
        <div class="flex">
          <div class="w-3/4" v-if="isAuthenticated">
            <p class="font-bold text-sm">{{this.userDetails.last_name}} {{ this.userDetails.first_name }}</p>
            <p class="text-xs">{{this.userDetails.profile}}</p>
          </div>
          <div class="w-3/4" v-else>
            <p class="font-bold text-sm">User Account</p>
            <p></p>
          </div>
          <div class="w-1/4">
            <button @click="showDropdown"><i class="fa fa-caret-down" aria-hidden="true"></i></button>
          </div>
        </div>
        <button class="fixed inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="dropdown" @click="dropdown = !dropdown"></button>
        <div class="dropdown-content mt-3 absolute rounded bg-white w-36 py-2 px-2 shadow-md shadow-slate-500" v-if="dropdown">
          <router-link to="/login"><strong>Logout</strong></router-link>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default{
  data(){
    return{
      userDetails: [],
      dropdown: false,
    }
  },
  props:['title'],
  computed:{
    isAuthenticated(){
      return this.$store.state.isAuthenticated;
    }
  },
  beforeMount(){
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  methods:{
    getUserDetails(){
      this.axios
      .get("api/v1/users/me/")
      .then((response)=>{
        this.userDetails = response.data;
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    showDropdown(){
      this.dropdown = !this.dropdown ;
    }
  },
  mounted(){
    this.getUserDetails();
  }

}
</script>

<style>
.navbar{
  z-index: 1;
}
/* .dropdown:hover .dropdown-content{
  display: block;
} */
/* .dropdown-content{
  display: none;
} */
</style>