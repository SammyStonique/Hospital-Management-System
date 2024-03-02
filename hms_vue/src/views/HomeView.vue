<template>
  <div class="home">
      <div class="w-full h-screen bg-slate-500 grid grid-cols-4 gap-4 py-12 px-12">
        <div class="">
          <div class="pl-3"> 
            <div class="rounded-full w-24 h-24 overflow-hidden mb-2">
              <img src="@/assets/hospital_icon.png" alt="HMS Icon" class="w-full h-full object-cover">
            </div>
          </div>
          <div> 
            <router-link to="/hms/dashboard" class="underline">Hospital Management</router-link>
          </div>
        </div>
        <div class="">
          <div class="pl-3"> 
            <div class="rounded-full w-24 h-24 overflow-hidden mb-2">
              <img src="@/assets/accounts.png" alt="HMS Icon" class="w-full h-full object-cover">
            </div>
          </div>
          <div>
            <router-link to="/fa/dashboard" class="underline">Financial Accounts</router-link>
          </div>
        </div>
        <div class="">
          <div class="pl-3"> 
            <div class="rounded-full w-24 h-24 overflow-hidden mb-2">
              <img src="@/assets/human-resource.jpg" alt="HMS Icon" class="w-full h-full object-cover">
            </div>
          </div>
          <div>
            <router-link to="/hr/dashboard" class="underline">Human Resource</router-link>
          </div>
        </div>
        <div class="">
          <div class="pl-3"> 
            <div class="rounded-full w-24 h-24 overflow-hidden mb-2">
              <img src="@/assets/inventory.png" alt="HMS Icon" class="w-full h-full object-cover">
            </div>
          </div>
          <div>
            <router-link to="/inv/dashboard" class="underline">Inventory Management</router-link>
          </div>
        </div>
      </div>
  </div>

</template>

<script>

export default{
  data(){
    return{
      companyID: ""
    }
  },
  methods:{
    setCompanyID(){
      let formData ={
        company_id: this.companyID
      }
    }

  },
  mounted(){
    this.companyID = localStorage.getItem("company_id");
  }
}
</script>

<style>
</style>