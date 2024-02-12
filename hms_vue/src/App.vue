<template>
  <nav>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </nav>
  <router-view
  :isAuthenticated="isAuthenticated"
  />
</template>

<script>
import axios from "axios";

export default{
  data(){
    return{
      // isAuthenticated: false,
    }
  },
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
    // this.isAuthenticated = this.$store.state.isAuthenticated;
  },
  mounted(){

  }
}
</script>

<style lang="scss">

</style>
