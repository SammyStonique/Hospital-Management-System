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
              <form action="" @submit.prevent="">
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
                <div class="basis-1/2" v-if="isEditing">
                    <label for="">Image</label>
                    <p class="text-sm">Currently: <a :href="`${this.image}`" target="blank" class="text-blue-500">{{ this.imgName }}</a></p>
                    <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg" >
                </div>
                <div class="basis-1/2" v-else>
                    <label for="">Image</label>
                    <input type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg">
                </div>
              </div>
              <div class="text-center" v-if="isEditing">
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateStaff(index)">Update</button>
              </div>
              <div class="text-center" v-else>
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createStaff">Save</button>
              </div>
              </form>
            </template>
            <template v-slot:footer> HMS. </template>
        </Modal>


        <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
          <table class="min-w-full bg-white"> 
            <thead class="bg-gray-800 text-white">
              <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                <th class="text-left py-3 px-4">#</th>
                <th class="text-left py-3 px-4">Name</th>
                <th class="text-left py-3 px-4">Email</th>
                <th class="text-left py-3 px-4">Phone Number</th>
                <th class="text-left py-3 px-4">ID Number</th>
                <th class="text-left py-3 px-4">Profile</th>
                <th class="text-left py-3 px-4">Status</th>
                <th class="text-left py-3 px-4">Actions</th>
              </tr>
            </thead>
            <tbody>
        
              <tr v-for="(staff,index) in staffList" :key="staff.id" class="even:bg-gray-100">
                <td class="text-left py-3 px-4">{{ index + 1 }}</td>
                <td class="text-left py-3 px-4">{{ staff.first_name }} {{ staff.last_name }}</td>
                <td class="text-left py-3 px-4">{{ staff.email }}</td>
                <td class="text-left py-3 px-4">{{ staff.phone_number }}</td>
                <td class="text-left py-3 px-4">{{ staff.identification_no }}</td>
                <td class="text-left py-3 px-4">{{ staff.profile }}</td>
                <td v-if="staff.is_active" class="text-left py-3 px-4">Active</td>
                <td v-else class="text-left py-3 px-4">Inactive</td>
                <td>
                    <div class="flex">
                        <div class="basis-1/3">
                            <button @click="editStaff(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                        </div>
                        <div class="basis-1/3">
                            <button v-if="staff.is_active"><i class="fa fa-unlock" aria-hidden="true" title="Lock Staff"></i></button>
                            <button v-else><i class="fa fa-lock" aria-hidden="true" title="Unlock Staff"></i></button>
                        </div>
                        <div class="basis-1/3">
                            <button @click="removeStaff(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                        </div>
                    </div>
                </td>
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
      imgName: "",
      phone_number: '',
      profile: '',
      dob: '',
      gender: '',
      id_number: '',
      userDetails: [],
      staffList: [],
      department: '',
      payroll_number: '',
      specialization: '',
      temporary_password: '',
      is_staff: true,
      isEditing: false,
      staffID: 0,
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
          this.axios
          .get("api/v1/pass-gen/")
          .then((response)=>{
            this.temporary_password = response.data;
          })
          .catch((error)=>{
            console.log(error.message)
          })
          .finally(()=>{
            let formData = new FormData();
            formData.append('first_name', this.first_name);
            formData.append('email', this.email);
            formData.append('last_name', this.last_name);
            formData.append('identification_no', this.id_number);
            formData.append('birth_date', this.dob);
            formData.append('gender', this.gender);
            formData.append('phone_number', this.phone_number);
            formData.append('profile', this.profile);
            formData.append('password', this.temporary_password);
            formData.append('is_staff', this.is_staff);
            formData.append('image', this.image);
              
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
            .catch((error)=>{
              console.log(error.message);
            })
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
                this.image = null,
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
              this.staffList.push(response.data.results[i]);
            }
          }
          
        })
        .catch((error)=>{
          console.log(error);
        })
      },
      editStaff(){
        this.isEditing = true;
        let selectedStaff = arguments[0];
        this.staffID = this.staffList[selectedStaff].id;
        this.axios
        .get(`api/v1/users/${this.staffID}/`)
        .then((response)=>{
            this.first_name = response.data.first_name;
            this.last_name = response.data.last_name;
            this.email = response.data.email;
            this.id_number = response.data.identification_no;
            this.dob = response.data.birth_date;
            this.phone_number = response.data.phone_number;
            this.profile = response.data.profile;
            this.gender = response.data.gender;
            this.image = response.data.image;
        })
        .catch((error)=>{
            console.log(error.message);
        })
        .finally(()=>{
            this.scrollToTop();
            this.showModal();
            this.axios
            .get(`api/v1/user-image/${this.staffID}/`)
            .then((response)=>{
              this.imgName = response.data;
            })
            .catch((error)=>{
              console.log(error.message)
            })
        })

      },
      updateStaff(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.id_number === '' ||
              this.gender === '' || this.profile === '' || this.dob === '' || this.phone_number === '' ){
                this.$toast.error("Please Enter Staff Details",{
                    duration:5000,
                    dismissible: true
                })
            }
            else{

              let formData = new FormData();
              formData.append('first_name', this.first_name);
              formData.append('email', this.email);
              formData.append('last_name', this.last_name);
              formData.append('identification_no', this.id_number);
              formData.append('birth_date', this.dob);
              formData.append('gender', this.gender);
              formData.append('phone_number', this.phone_number);
              formData.append('profile', this.profile);
              formData.append('password', this.temporary_password);
              formData.append('is_staff', this.is_staff);
              formData.append('is_active', this.is_staff);
              formData.append('image', this.image);

              this.axios
              .put("api/v1/users/"+this.staffID+"/", formData)
              .then((response)=>{
                  this.$toast.success("Staff Succesfully Updated",{
                      duration:5000,
                      dismissible: true
                  })
              })
              .catch((error)=>{
                  console.log(error.message);
              })
              .finally(()=>{
                  this.hideLoader();
                  this.closeModal();
                  this.$store.commit('reloadingPage');
              })
            }
        },
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