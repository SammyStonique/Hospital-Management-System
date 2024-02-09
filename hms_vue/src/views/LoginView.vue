<template>
    <div class="login">
        <div class="w-full h-screen bg-slate-700 grid place-items-center">
            <div class="w-1/2 h-80 bg-white p-4 rounded-lg">
                <div class="text-center grid place-items-center">
                    <div class="flex w-36">
                    <div class="w-1/2 rounded-full">
                        <img src="@/assets/download.png" alt="Logo" class="">
                    </div>
                    <div class="w-1/2 pl-2">
                        <h4 class="text-2xl py-4">K.H.S</h4>
                    </div>
                </div>
                </div>
                <div class="py-4 px-8">
                    <form @submit.prevent="" action="">
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Username:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="text" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg">
                            </div>
                        </div>
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Password:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="password" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg">
                            </div>
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
        password: ''
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
            .post("/api/v1/tokens/login/", formData)
            .then((response)=>{
                const token = response.data.auth_token;        
                this.$store.commit('setToken', token);
                axios.defaults.headers.common['Authorization'] = "Token " + token
                localStorage.setItem('token',token)
                this.$toast.success('Login Succesful',{
                    duration: 5000
                })
                this.$router.push('/')
                // this.$store.commit('reloadingPage')
            })    
            .catch((error)=>{
                if (error.response) {
                    for (const property in error.response.data) {
                        this.errors.push(`${error.response.data[property]}`)
                    }
                    console.log(JSON.stringify(error.response.data))
                    this.$toast.error('Invalid Login Credentials!',{
                        duration:5000
                    })
                } else if (error.message) {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(JSON.stringify(error))
                }
            })

        }
    }
  }
}
</script>