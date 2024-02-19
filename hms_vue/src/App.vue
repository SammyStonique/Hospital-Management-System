<template>
  <nav>
  </nav>
  <router-view
  :isAuthenticated="isAuthenticated"
  :scrollToTop="scrollToTop"
  :loader="loader"
  :showLoader="showLoader"
  :hideLoader="hideLoader"
  />
</template>

<script>
import axios from "axios";

export default{
  data(){
    return{
      loader: "none",
      loaderIndex: 1,
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
    // Loader Methods
    showLoader(){
        this.loader = "block";
        this.loaderIndex = -1;
    },
    hideLoader(){
        this.loader = "none";
        this.loaderIndex = 1;
    },
  }
}
</script>

<style lang="scss">

</style>
