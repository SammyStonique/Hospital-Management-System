<template>
    <Loader
    :loader="loader"
    :showLoader="showLoader"
    :hideLoader="hideLoader"
    />
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection rounded bg-white p-3">
        <h2 class="text-center font-bold">Staff</h2>
        <div class="md:px-8 py-8 mb-4">
          <button class="rounded border bg-green-400 text-white p-3" @click="showModal"> + New Staff</button>
        </div>

        <!-- MODAL component for adding a new user -->
        <Modal v-show="isModalVisible" @close="closeModal">
            <template v-slot:header> User Details </template>
            <template v-slot:body>
              <form action="" @submit.prevent="createStaff">
                <div class="flex mb-4">
                  <div class="basis-1/2">
                    <label for="">First Name<em>*</em></label>
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="first_name">
                  </div>
                  <div class="basis-1/2">
                    <label for="">Last Name<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="last_name">
                  </div>
              </div>
              <div class="flex mb-4">
                  <div class="basis-1/2">
                    <label for="">Email<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="email">
                  </div>
                  <div class="basis-1/2">
                    <label for="">ID Number<em>*</em></label>
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="id_number">
                  </div>
              </div>
              <div class="flex mb-4">
                <div class="basis-1/2">
                    <label for="">Phone Number<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" placeholder="e.g 07XXXX" v-model="phone_number">
                  </div>
                  <div class="basis-1/2">
                    <label for="">Date of Birth<em>*</em></label><br />
                    <input type="date" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="dob">
                  </div>
              </div>
              <div class="flex mb-4">
                <div class="basis-1/2">
                  <label for="">Profile<em>*</em></label><br />
                  <select name="" id="" class="rounded border border-gray-600 text-lg pl-2 pt-2" placeholder="Select Profile" v-model="profile">
                    <option value="" selected disabled>---Select Profile---</option>
                    <option value="Admin">Admin</option>
                    <option value="Doctor">Doctor</option>
                    <option value="Clinical Officer">Clinical Officer</option>
                    <option value="Accountant">Accountant</option>
                    <option value="Human Resource">Human Resource</option>
                    <option value="Nurse">Nurse</option>
                    <option value="Lab Technician">Lab Technician</option>
                    <option value="Office Clerk">Office Clerk</option>
                  </select>
                </div>
                <div class="basis-1/2">
                  <label for="">Gender<em>*</em></label><br />
                  <select class="rounded border border-gray-600 text-lg pl-2 pt-2" placeholder="Select Gender" v-model="gender">
                    <option value="" selected disabled>---Select Gender--</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>
              <div class="flex">
                <div class="basis-1/2">
                    <label for="">Image</label>
                    <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg">
                </div>
              </div>
              <div class="text-center">
                <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg">Save</button>
              </div>
              </form>
            </template>
            <template v-slot:footer> HMS. </template>
        </Modal>


        <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
          <table class="min-w-full bg-white"> 
            <thead class="bg-gray-800 text-white">
              <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                <th class="text-left py-3 px-4">Name</th>
                <th class="text-left py-3 px-4">Email</th>
                <th class="text-left py-3 px-4">Phone Number</th>
                <th class="text-left py-3 px-4">ID Number</th>
                <th class="text-left py-3 px-4">Profile</th>
                <th class="text-left py-3 px-4">Status</th>
              </tr>
            </thead>
            <tbody>
        
              <tr v-for="staff in staffDetails" class="even:bg-gray-100">
                <td class="text-left py-3 px-4">{{ staff.first_name }} {{ staff.last_name }}</td>
                <td class="text-left py-3 px-4">{{ staff.email }}</td>
                <td class="text-left py-3 px-4">{{ staff.phone_number }}</td>
                <td class="text-left py-3 px-4">{{ staff.identification_no }}</td>
                <td class="text-left py-3 px-4">{{ staff.profile }}</td>
                <td v-if="staff.is_active" class="text-left py-3 px-4">Active</td>
                <td v-else class="text-left py-3 px-4">Inactive</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>

<script>

import Loader from '@/components/Loader.vue'
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'

export default{
    name: 'StaffView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
      title: 'Staff',
      isModalVisible: false,
      first_name: '',
      last_name: '',
      email: '',
      image:null,
      phone_number: '',
      profile: '',
      dob: '',
      gender: '',
      id_number: '',
      userDetails: [],
      staffDetails: [],
      department: '',
      payroll_number: '',
      specialization: '',
      temporary_password: '',
      is_staff: false
    }
  },
    components: {
        NavBar,
        SideBar,
        Modal,
        Loader
    },
    methods:{
      onFileChange(e){
        this.image = e.target.files[0];
        console.log(this.image)
      },
      showModal(){
        this.isModalVisible = !this.isModalVisible;
      },
      closeModal(){
        this.isModalVisible = false;
      },
      createStaff(){
        this.showLoader();
        if(this.first_name === '' || this.last_name === '' || this.email === '' || this.id_number === '' ||
        this.gender === '' || this.profile === '' || this.dob === '' || this.phone_number === '' ){
          this.$toast.error("Please Enter User Details",{
            duration: 5000,
            dismissible: true
          })
        }
        else{
          this.is_staff = true;
          this.axios
          .get("api/v1/pass-gen/")
          .then((response)=>{
            this.temporary_password = response.data;
          })
          .catch((error)=>{
            console.log(error.message)
          })
          .finally(()=>{
                let formData = {
                email: this.email,
                first_name: this.first_name,
                last_name: this.last_name,
                identification_no: this.id_number,
                birth_date: this.dob,
                gender: this.gender,
                phone_number: this.phone_number,
                profile: this.profile,
                password: this.temporary_password,
                is_staff: this.is_staff,
              }
              this.axios
              .post("api/v1/users/", formData)
              .then((response)=>{
                  this.userDetails = response.data;
                  console.log("The temporary password is ", this.temporary_password);
                  this.$toast.success("User Created Succesfully",{
                    duration: 5000,
                    dismissible: true
                  })
              })
              .catch((error)=>[
                console.log(error.message)
              ])
              .finally(()=>{
                let formData ={
                  temporary_password: this.temporary_password,
                }
                this.axios
                .post(`api/v1/user-credentials/${this.userDetails.id}/`, formData)
                .then((response)=>{
                })
                .catch((error)=>{
                  console.log(error);
               })
               .finally(()=>{
                  this.first_name = "";
                  this.last_name = "";
                  this.email = "";
                  this.id_number = "";
                  this.dob = "";
                  this.gender = "";
                  this.phone_number = "";
                  this.profile = "";
                  this.is_staff = false;
                  this.hideLoader();
                  this.$router.push("/staff")
               })
              })

          })
        }
      },
      fetchStaff(){
        this.axios
        .get("api/v1/users/")
        .then((response)=>{
          for(let i=0; i<response.data.results.length; i++){
            if(response.data.results[i].profile != "Admin" && response.data.results[i].profile != "Patient"){
              this.staffDetails.push(response.data.results[i]);
            }
          }
          
        })
        .catch((error)=>{
          console.log(error);
        })
      }
    },
    mounted(){
      this.fetchStaff();
    }
}
</script>

<style scoped>
.main-content{
  z-index: -1;
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
em{
  color: red;
}
</style>