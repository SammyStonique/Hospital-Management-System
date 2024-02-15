<template>
  <nav>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </nav>
  <router-view
  :isAuthenticated="isAuthenticated"
  :scrollToTop="scrollToTop"
  :depList="depList"
  :fetchDepartments="fetchDepartments"
  />
</template>

<script>
import axios from "axios";

export default{
  data(){
    return{
      depList: []
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
    fetchDepartments(){
      this.axios
      .get("api/v1/department-list/")
      .then((response)=>{
          this.depList = response.data;
      })
      .catch((error)=>{
          console.log(error.message);
      })
      .finally(()=>{

      })
    },
  }
}
</script>

<style lang="scss">

</style>
