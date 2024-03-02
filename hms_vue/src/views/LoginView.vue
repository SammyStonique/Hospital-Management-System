<template>
    <div class="login">
        <div class="w-full h-screen bg-slate-700 grid place-items-center">
            <div class="w-1/2 h-100 bg-white p-4 rounded-lg">
                <div class="text-center grid place-items-center">
                    <div class="flex w-36">
                    <div class="w-1/2 rounded-full">
                        <img src="@/assets/logo.jpeg" alt="Logo" class="">
                    </div>
                    <div class="w-1/2 pl-2">
                        <h4 class="text-2xl py-4">K.H.S</h4>
                    </div>
                </div>
                </div>
                <div class="py-6 px-8">
                    <form @submit.prevent="login" action="">
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Username:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="text" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg" v-model="email">
                            </div>
                        </div>
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Password:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="password" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg" v-model="password">
                            </div>
                        </div>
                        <div class="col-md-12 notification is-danger" v-if="errors.length">
                            <p style="color: red;" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                        <div class="mt-3 grid justify-items-end">
                            <div class="pr-24">
                                <button class="bg-green-300 px-6 py-2 rounded-lg w-32">Login</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'LoginView',
  data(){
    return{
        email: '',
        password: '',
        errors: []
    }
  },
  components: {
    
  },
  methods:{
    login(){
        if (this.email != "" && this.password != ""){
            const formData = {
                email: this.email,
                password: this.password
            }
            this.axios
            .post("/api/v1/token/login/", formData)
            .then((response)=>{
                const token = response.data.auth_token;        
                this.$store.commit('setToken', token);
                axios.defaults.headers.common['Authorization'] = "Token " + token
                localStorage.setItem('token',token)
            })    
            .catch((error)=>{
                if (error.response) {
                    this.$toast.error('Invalid Login Credentials!',{
                        duration:5000
                    })
                    console.log(error.message);
                } else if (error.message) {
                    this.errors.push('Something went wrong. Please try again');
                    console.log(JSON.stringify(error))
                }
            })
            .finally(()=>{
                this.axios
                .get("/api/v1/users/me/")
                .then((response)=>{
                    const company_id = response.data.allowed_company;
                    this.$store.commit('fetchCompanyID', company_id);
                    localStorage.setItem('company_id', company_id)
                    this.$router.push('/')
                })
            })

        }else{
            this.$toast.error('Please Enter your Login Credentials!',{
                        duration:5000
                    })
        }
    }
  },
  mounted(){
    this.$store.commit('removeToken');
    this.$store.commit('removeCompanyID');
  }
}
</script>