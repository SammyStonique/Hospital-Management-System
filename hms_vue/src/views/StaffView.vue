<template>
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
              <div class="text-center">
                <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg">Save</button>
              </div>
              </form>
            </template>
            <template v-slot:footer> HMS. </template>
        </Modal>


        <div>
          <table class="w-full"> 
            <thead>

            </thead>
            <tbody>
              <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                <th class="text-left py-3 px-4">Name</th>
                <th class="text-left py-3 px-4">Email</th>
                <th class="text-left py-3 px-4">Phone Number</th>
                <th class="text-left py-3 px-4">ID Number</th>
                <th class="text-left py-3 px-4">Profile</th>
                <th class="text-left py-3 px-4">Status</th>
              </tr>
              <tr>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'

export default{
    name: 'StaffView',
    data(){
    return{
      title: 'Staff',
      isModalVisible: false,
      first_name: '',
      last_name: '',
      email: '',
      phone_number: '',
      profile: '',
      dob: '',
      gender: '',
      id_number: '',
      userDetails: [],
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
        Modal
    },
    methods:{
      showModal(){
        this.isModalVisible = !this.isModalVisible;
      },
      closeModal(){
        this.isModalVisible = false;
      },
      createStaff(){
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
                  console.log("The user details are ", this.userDetails);
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
                this.first_name = "";
                this.last_name = "";
                this.email = "";
                this.id_number = "";
                this.dob = "";
                this.gender = "";
                this.phone_number = "";
                this.profile = "";
                this.is_staff = false;
                this.$router.push("/staff")
                
                // if(this.userDetails.profile === "Doctor"){
                //   let formData = {
                //     first_name: this.userDetails.first_name,
                //     last_name: this.userDetails.last_name,
                //     email: this.userDetails.email,
                //     phone_number: this.userDetails.phone_number,
                //     department: this.department,
                //     payroll_number: this.payroll_number,
                //     specialization: this.specialization,
                //   }
                //   this.axios
                //   .post("api/v1/doctor-list/", formData)
                //   .then((response)=>[

                //   ])
                //   .catch((error)=>{
                //     console.log(error.message);
                //   })
                // }
              })

          })
        }
      }
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