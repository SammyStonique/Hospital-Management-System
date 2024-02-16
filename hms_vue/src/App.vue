<template>
  <nav>
  </nav>
  <router-view
  :isAuthenticated="isAuthenticated"
  :scrollToTop="scrollToTop"

  />
</template>

<script>
import axios from "axios";

export default{
  data(){
    return{
      
    }
  },
  computed:{
    isAuthenticated(){
      return this.$store.state.isAuthenticated;
    }
  },
  beforeMount(){
    this.$store.commit("initializeStore");
    this.$store.commit("reloadingPage");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted(){

  },
  methods:{
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
  }
}
</script>

<style lang="scss">

</style>
