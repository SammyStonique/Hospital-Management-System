<template>
    <Loader
    :loader="loader"
    :showLoader="showLoader"
    :hideLoader="hideLoader"
    />
    <NavBar
    :title="title"
    />
    <SideBarHMS />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection rounded bg-white p-3">
        <h2 class="text-center font-bold mb-12">My Account</h2>
        <div class="flex">
            <div class="basis-1/4 mr-2 px-3">
                <div class="flex pt-24 items-end mb-8">
                    <div class="basis-1/4 mr-2">
                        <div class="rounded-full w-24 h-24 overflow-hidden">
                            <img :src="`${this.userDetails.image}`" alt="Profile Pic" class="w-full h-full object-cover">
                        </div>
                    </div>
                    <div class="basis-3/4">
                        <p class="font-bold">{{ userDetails.last_name }} {{ userDetails.first_name }}</p>
                        <p class="font-bold">{{ userDetails.email }}</p>
                    </div>
                </div>
                <div class="rounded bg-gray-100 w-full py-8">
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showDashboard">
                            <p class="text-lg">My Dashboard</p>
                        </button>
                    </div> 
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showAccountDetails">
                            <p class="text-lg">Account Details</p>
                        </button>
                    </div>
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showAppointments">
                            <p class="text-lg">My Appointments</p>
                        </button>
                    </div>
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showPatients">
                            <p class="text-lg">My Patients</p>
                        </button>
                    </div>
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showPayslips">
                            <p class="text-lg">My Payslips</p>
                        </button>
                    </div>
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showProfileChange">
                            <p class="text-lg">Change Profile Picture</p>
                        </button>
                    </div>
                    <div class="web-links py-2 px-3 pl-4 hover:bg-slate-300 hover:rounded hover:w-full">
                        <button class="flex" @click="showPasswordChange">
                            <p class="text-lg">Change Passsword</p>
                        </button>
                    </div>
                </div>
            </div>
            <div class="rounded basis-3/4 bg-gray-100 py-4 px-4">
                <div class="account-tabs rounded bg-white px-4 py-4">
                    <div id="" v-if="this.showDash">
                        <p class="font-bold mb-8 text-center">My Dashboard</p>
                        <div class="w-full rounded-lg py-3 px-2 bg-white mr-2">
                            <h1 class="font-bold mb-2">Activity Overview</h1>
                            <div class="flex w-full mb-3">
                            <div class="w-1/2 rounded-lg h-16 border-2 p-2 mr-4">
                                <div class="w-full flex">
                                <div class="w-1/4 rounded-lg bg-cyan-600 h-10 grid place-items-center">
                                    <i class="fa fa-calendar" aria-hidden="true"></i>
                                </div>
                                <div class="w-3/4 px-2">
                                    <p class="font-bold">500</p>
                                    <p class="font-light text-sm">Appointments</p>
                                </div>
                                </div>
                            </div>
                            <div class="w-1/2 rounded-lg h-16 border-2 p-2">
                                <div class="w-full flex">
                                <div class="w-1/4 rounded-lg bg-orange-400 h-10 grid place-items-center">
                                    <i class="fa fa-scissors" aria-hidden="true"></i>
                                </div>
                                <div class="w-3/4 px-2">
                                    <p class="font-bold">400</p>
                                    <p class="font-light text-sm">Operations</p>
                                </div>
                                </div>
                            </div>
                            </div>
                            <div class="flex w-full mb-3">
                            <div class="w-1/2 rounded-lg h-16 border-2 p-2 mr-4">
                                <div class="w-full flex">
                                <div class="w-1/4 rounded-lg bg-indigo-600 h-10 grid place-items-center">
                                    <i class="fa fa-bed" aria-hidden="true"></i>
                                </div>
                                <div class="w-3/4 px-2">
                                    <p class="font-bold">150</p>
                                    <p class="font-light text-sm">New Patients</p>
                                </div>
                                </div>
                            </div>
                            <div class="w-1/2 rounded-lg h-16 border-2 p-2">
                                <div class="w-full flex">
                                <div class="w-1/4 rounded-lg bg-rose-600 h-10 grid place-items-center">
                                    <i class="fa fa-user-md" aria-hidden="true"></i>
                                </div>
                                <div class="w-3/4 px-2">
                                    <p class="font-bold">60</p>
                                    <p class="font-light text-sm">Doctors</p>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div id="" v-if="this.showAcc">
                        <p class="font-bold mb-8 text-center">Account Details</p>
                        <form action="" @submit.prevent="">
                            <div class="flex mb-6">
                                <div class="basis-1/2">
                                    <label for="">First Name<em>*</em></label><br />
                                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="first_name">
                                </div>
                                <div class="basis-1/2">
                                    <label for="">Last Name<em>*</em></label><br />
                                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="last_name">
                                </div>
                            </div>
                            <div class="flex mb-6">
                                <div class="basis-1/2">
                                    <label for="">Email<em>*</em></label><br />
                                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" v-model="email">
                                </div>
                                <div class="basis-1/2">
                                    <label for="">ID Number<em>*</em></label><br />
                                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" v-model="id_number">
                                </div>
                            </div>
                            <div class="flex mb-6">
                                <div class="basis-1/2">
                                    <label for="">Phone Number<em>*</em></label><br />
                                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" placeholder="e.g 07XXXX" v-model="phone_number">
                                </div>
                                <div class="basis-1/2">
                                    <label for="">Date of Birth<em>*</em></label><br />
                                    <datepicker  placeholder="Date of Birth...." v-model="dob" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                            </div>
                            <div class="flex mb-6">
                                <div class="basis-1/2 mr-4">
                                    <label for="">Profile<em>*</em></label><br />
                                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" placeholder="Profile" v-model="profile">
                                </div>
                                <div class="basis-1/2">
                                <label for="">Gender<em>*</em></label><br />
                                <select class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" placeholder="Select Gender" v-model="gender">
                                    <option value="" selected disabled>---Select Gender---</option>
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                    <option value="Other">Other</option>
                                </select>
                                </div>
                            </div>
                            <div class="flex mb-6">
                                <div class="basis-1/2 mr-4">
                                    <label for="">Department<em>*</em></label><br />
                                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" placeholder="Department" v-model="department">
                                </div>
                            </div>
                            <div class="text-center">
                                <button class="rounded border bg-green-400 mt-3 w-52 py-2 px-4 text-white text-lg" @click="updateDetails()">Update Details</button>
                            </div>
                        </form>
                    </div>
                    <div v-if="this.showApp">
                        <p class="font-bold mb-8 text-center">My Appointments</p>
                    </div>
                    <div v-if="this.showPat">
                        <p class="font-bold mb-8 text-center">My Patients</p>
                    </div>
                    <div v-if="this.showPay">
                        <p class="font-bold mb-8 text-center">My Payslips</p>
                    </div>
                    <div v-if="this.showPicChange" class="pl-12">
                        <p class="font-bold mb-10 text-center">Change Profile Pic</p>
                        <div class="flex pt-24 items-end mb-8">
                            <div class="basis-1/4 mr-2">
                                <div class="rounded-full w-36 h-36 overflow-hidden">
                                    <img :src="`${this.userDetails.image}`" alt="Profile Pic" class="w-full h-full object-cover">
                                </div>
                            </div>
                            <div class="basis-3/4">
                                <p class="font-bold mb-3">Currently: <a :href="`${this.userDetails.image}`" target="blank" class="text-blue-500">{{ this.imgName }}</a></p>
                                <label for="" class="mb-2 font-bold">Choose New Picture(jpg, jpeg or png only):</label><br />
                                <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg" >
                            </div>
                        </div>
                        <div class="text-center">
                            <button class="rounded border bg-green-400 mt-3 w-52 py-2 px-4 text-white text-lg" @click="changeProfilePic()">Upload Image</button>
                        </div>
                    </div>
                    <div v-if="this.showPassChange" class="px-12">
                        <p class="font-bold mb-10 text-center">Password Change</p>
                        <div class="mb-6">
                            <label for="">New Password:<em>*</em></label><br />
                            <input :type="passType ? 'text' : 'password'" class="rounded border border-gray-600 text-lg pl-2" v-model="new_password">
                            <button type="button" class="show-password" @click="showPassword()">
                                <i class="fa fa-eye" v-if="!passType"></i>
                                <i class="fa fa-eye-slash" v-else></i>
                            </button><br />
                            <span v-if="watcherMsg.new_password" :style="{color: pStyle, fontSize:12 + 'px' }">{{watcherMsg.new_password}}</span>
                        </div>
                        <div class="mb-6"> 
                            <label for="">Confirm Password:<em>*</em></label><br />
                            <input :type="pass2Type ? 'text' : 'password'" class="rounded border border-gray-600 text-lg pl-2" v-model="new_password2">
                            <button type="button" class="show-password" @click="showPassword2()">
                                <i class="fa fa-eye" v-if="!pass2Type"></i>
                                <i class="fa fa-eye-slash" v-else></i>
                            </button><br />
                            <span v-if="watcherMsg.new_password2" :style="{color: passStyle , fontSize:12 + 'px' }">{{watcherMsg.new_password2}}</span>
                        </div>
                        <div class="text-center">
                            <button class="rounded border bg-green-400 mt-3 w-52 py-2 px-4 text-white text-lg" @click="changePassword()">Change Password</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>

</template>

<script>

import Loader from '@/components/Loader.vue'
import NavBar from '@/components/NavBar.vue'
import SideBarHMS from '@/components/SideBarHMS.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'
import Datepicker from 'vuejs3-datepicker';

export default{
    name: 'MyAccountView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ My Account',
            userDetails: [],
            first_name: "",
            last_name: "",
            email: "",
            phone_number: "",
            profile: "",
            depID: 0,
            department: "",
            gender: "",
            id_number: "",
            dob: null,
            imgName: "",
            image: "",
            userID: 0,
            companyID: "",
            new_password: "",
            new_password2: "",
            is_staff: true,
            showAcc: false,
            showDash:true,
            showApp:false,
            showPat:false,
            showPay:false,
            showPassChange: false,
            shwPicChange: false,
            watcherMsg:[],
            pStyle: null,
            passStyle: null,
            passType: false,
            pass2Type: false,
            showPass: false,
            showPass2: false,
        }
    },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker
    },
    watch:{
        new_password(value){
            this.new_password = value;
            this.validatePassword(value)
        },
        new_password2(value){
            this.new_password2 = value;
            this.validatePasswordConfirmation(value)
        }
    },
    methods:{
        formatDate(dateString) {
            const date = new Date(dateString);
            const year = date.getFullYear().toString()
            const month = ('0' + (date.getMonth() + 1)).slice(-2);
            const day = ('0' + date.getDate()).slice(-2);
            return `${year}-${month}-${day}`;
        },
        fetchUserAccount(){
            this.axios
            .get("api/v1/users/me/")
            .then((response)=>{
                this.userDetails = response.data;
                this.first_name = this.userDetails.first_name;
                this.last_name = this.userDetails.last_name;
                this.email = this.userDetails.email;
                this.id_number = this.userDetails.identification_no;
                this.gender = this.userDetails.gender;
                this.profile = this.userDetails.profile;
                this.depID = this.userDetails.user_department;
                this.phone_number = this.userDetails.phone_number;
                this.dob = this.userDetails.birth_date;
                this.imgName = this.userDetails.image;
                this.userID = this.userDetails.user_id;
            })
            .catch((error)=>{
                console.log(error)
            })
            .finally(()=>{
                this.axios
                .get(`api/v1/department-details/${this.depID}/`)
                .then((response)=>{
                    this.department = response.data.name;
                })
                .catch((error)=>{
                    console.log(error.message);
                })
            })
        },
        onFileChange(e){
            this.image = e.target.files[0];
            console.log(this.image)
        },
        showDashboard(){
            this.showAcc = false,
            this.showDash = true,
            this.showApp = false,
            this.showPat = false,
            this.showPay = false,
            this.showPassChange =  false,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        showAccountDetails(){
            this.showAcc = true,
            this.showDash = false,
            this.showApp = false,
            this.showPat = false,
            this.showPay = false,
            this.showPassChange =  false,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        showAppointments(){
            this.showAcc = false,
            this.showDash = false,
            this.showApp = true,
            this.showPat = false,
            this.showPay = false,
            this.showPassChange =  false,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        showPatients(){
            this.showAcc = false,
            this.showDash = false,
            this.showApp = false,
            this.showPat = true,
            this.showPay = false,
            this.showPassChange =  false,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        showPayslips(){
            this.showAcc = false,
            this.showDash = false,
            this.showApp = false,
            this.showPat = false,
            this.showPay = true,
            this.showPassChange =  false,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        showProfileChange(){
            this.showAcc = false,
            this.showDash = false,
            this.showApp = false,
            this.showPat = false,
            this.showPay = false,
            this.showPassChange =  false,
            this.showPicChange =  true,
            this.scrollToTop();
        },
        showPasswordChange(){
            this.showAcc = false,
            this.showDash = false,
            this.showApp = false,
            this.showPat = false,
            this.showPay = false,
            this.showPassChange =  true,
            this.showPicChange =  false,
            this.scrollToTop();
        },
        updateDetails(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.id_number === '' ||
            this.gender === '' || this.profile === '' || this.dob === '' || this.phone_number === '' || this.department === '' ){
                this.$toast.error("Please Enter Your Details",{
                    duration: 5000,
                    dismissible: true
                })
                this.hideLoader();
            }else{
                let new_first_name = this.first_name[0].toUpperCase() + this.first_name.slice(1).toLowerCase();
                let new_last_name = this.last_name[0].toUpperCase() + this.last_name.slice(1).toLowerCase();
                let formData = new FormData();
                formData.append('first_name', new_first_name);
                formData.append('email', this.email);
                formData.append('last_name', new_last_name);
                formData.append('identification_no', this.id_number);
                formData.append('birth_date', this.formatDate(this.dob));
                formData.append('gender', this.gender);
                formData.append('phone_number', this.phone_number);
                formData.append('profile', this.profile);
                formData.append('is_staff', this.is_staff);
                formData.append('is_active', this.is_staff);
                formData.append('user_department', this.depID);
                formData.append('allowed_company', this.companyID);
                this.axios
                .put("api/v1/users/me/", formData)
                .then((response)=>{
                    this.$toast.success("Yours Details Are Succesfully Updated",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.$store.commit('reloadingPage');
                })
            }
            
        },
        changeProfilePic(){
            this.showLoader();
            if (this.image === ""){
                this.$toast.error("No Picture Selected",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData();
                formData.append('first_name', this.first_name);
                formData.append('email', this.email);
                formData.append('last_name', this.last_name);
                formData.append('identification_no', this.id_number);
                formData.append('birth_date', this.formatDate(this.dob));
                formData.append('gender', this.gender);
                formData.append('phone_number', this.phone_number);
                formData.append('profile', this.profile);
                formData.append('is_staff', this.is_staff);
                formData.append('is_active', this.is_staff);
                formData.append('user_department', this.depID);
                formData.append('image', this.image);
                formData.append('allowed_company', this.companyID);
                this.axios
                .put("api/v1/users/me/", formData)
                .then((response)=>{
                    this.$toast.success("Profile Picture Succesfully Uploaded",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.$store.commit('reloadingPage');
                })
            }
        },
        changePassword(){
            this.showLoader();
            if(this.new_password === "" || this.new_password2 === ""){
                this.$toast.error("Please Enter New Password",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }else if(this.watcherMsg.new_password || this.watcherMsg.new_password2){
                this.$toast.error("Invalid Password Entered",{
                    duration: 3000,
                    dismissible: true
                })
            }else{
                if(this.new_password == this.new_password2){
                    let formData = {
                        new_password : this.new_password,
                    }
                    this.axios
                    .post(`api/v1/reset-password/${this.userID}/`, formData)
                    .then((response)=>{
                        this.$toast.success("Password Succesfully Changed",{
                            duration: 3000,
                            dismissible: true
                        })
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        this.hideLoader();
                        this.new_password = "";
                        this.new_password2 = "";
                        this.$router.push('/login')
                    })
                }    
            }
        },
        validatePassword(value){
            if (value.length > 0 && value.length < 8){
                this.watcherMsg['new_password'] = 'Must be a minimum of 8 characters!'
                this.pStyle = 'red'
                this.bWidth = 2
            }else{
                if(value.length == 0){
                   this.watcherMsg['new_password'] = ''
                   this.pStyle = ''
                }
            else{
                    this.pStyle = 'green'
                    this.watcherMsg['new_password'] = ''
                    this.bWidth = 2
                }
            }
        },
        validatePasswordConfirmation(value){
            if (value === this.new_password){
                this.passStyle = 'green'
                this.watcherMsg['new_password2'] = ''
                this.bWidth = 2
            }else{
                this.watcherMsg['new_password2'] = 'The passwords do not match'
                this.passStyle = 'red'
                this.bWidth = 2
            }
        },
        showPassword(){
            if(!this.showPass){
                this.showPass = true;
                this.passType = true;
            }
            else{
                this.showPass = false;
                this.passType = false;
            }
        }, 
        showPassword2(){
            if(!this.showPass2){
                this.showPass2 = true;
                this.pass2Type = true;
                console.log("ShowPass PassType",this.showPass2);
            }
            else{
                this.showPass2 = false;
                this.pass2Type = false;
                console.log("ShowPass PassType",this.showPass2);
            }
        },
    },
    mounted(){
        this.companyID = localStorage.getItem('company_id')
        this.fetchUserAccount();
    }
}
</script>

<style>
.main-content{
  z-index: -1;
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
.account-tabs{
    min-height: 100vh;
}
em{
  color: red;
}
.show-password{
    float: right;
    /* margin-top: -50px; */
    margin-left: -30px;
    position: absolute;
    z-index: 1;
    cursor:pointer;
    height: 35px;
    border:0px;
    background-color: inherit;
    color:grey;
}
.show-password:focus{
    outline: none;
}
.show-password:hover{
    color: black !important;
}
</style>