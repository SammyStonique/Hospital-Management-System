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
        <h2 class="text-center font-bold">Staff</h2>
        <div class="md:px-4 pt-4 pb-1 w-full border-b-2 border-gray-300 mb-6">
          <div class="mb-4 flex items-end h-24">
            <div class="basis-1/6 pl-3">
              <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Staff</button>
            </div>
            <div class="basis-3/4">
              <div class="flex mb-3">
                <div class="basis-1/3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="name" id="" placeholder="Name...." v-model="search_name" @keyup.enter="searchStaff">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="id_number" id="" placeholder="ID Number...." v-model="search_id_number"  @keyup.enter="searchStaff">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                  <select name="" id="" class="rounded border border-gray-200 text-lg bg-white pl-2 pt-2 w-52" placeholder="Profile...." v-model="search_profile">
                    <option value="" selected disabled>Profile</option>
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
              </div>
              <div class="flex">
                <div class="basis-1/3 items-center">
                  <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-2 pt-2 w-52" placeholder="Status...." v-model="status">
                    <option value="" selected disabled  class="status-placeholder">Status</option>
                    <option value="True">Active</option>
                    <option value="False">Inactive</option>
                  </select>
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="Department" id="" placeholder="Department...." v-model="search_user_department" @keyup.enter="searchStaff">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="Phone Number" id="" placeholder="Phone Number...." v-model="search_phone_number" @keyup.enter="searchStaff">
                </div>
              </div>
            </div>
            <div class="basis-1/8 pl-3 items-center w-36">
                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchStaff"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
            </div>
            <div class="basis-1/8 pl-3 w-36">
                <div class="print-dropdown">
                    <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                    <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                </div>
                <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                    <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                    <button @click="exportStaffPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                    <button @click="exportStaffExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                    <button @click="exportStaffCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                </div>
            </div>
          </div>
        </div>
        <!-- MODAL component for adding a new user -->
        <Modal v-show="isModalVisible" @close="closeModal">
            <template v-slot:header> User Details </template>
            <template v-slot:body>
              <form action="" @submit.prevent="">
                <div class="flex mb-6">
                  <div class="basis-1/2">
                    <label for="">First Name<em>*</em></label>
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="first_name" required>
                  </div>
                  <div class="basis-1/2">
                    <label for="">Last Name<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="last_name" required>
                  </div>
              </div>
              <div class="flex mb-6">
                  <div class="basis-1/2" v-if="isEditing">
                    <label for="">Email<em>*</em></label><br />
                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" v-model="email" required>
                  </div>
                  <div class="basis-1/2" v-else>
                    <label for="">Email<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none" v-model="email" :style="{borderColor: eStyle,borderWidth: bWidth+'px' }" required><br />
                    <span v-if="watcherMsg.email" :style="{color: eStyle, fontSize:10 + 'px'}">{{watcherMsg.email}}</span>
                  </div>
                  <div class="basis-1/2">
                    <label for="">ID Number<em>*</em></label>
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="id_number" required>
                  </div>
              </div>
              <div class="flex mb-6">
                <div class="basis-1/2">
                    <label for="">Phone Number<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none" placeholder="e.g 07XXXX" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px' }" required><br />
                    <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                  </div>
                  <div class="basis-1/2">
                    <label for="">Date of Birth<em>*</em></label><br />
                    <datepicker  placeholder="Date of Birth...." v-model="dob" clearable :clear-button="clearButton">
                    </datepicker>
                  </div>
              </div>
              <div class="flex mb-6">
                <div class="basis-1/2">
                  <label for="">Profile<em>*</em></label><br />
                  <select name="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" placeholder="Select Profile" v-model="profile" required>
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
                  <select class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" placeholder="Select Gender" v-model="gender" required>
                    <option value="" selected disabled>---Select Gender---</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>
              <div class="flex mb-6">
                <div class="basis-1/2">
                  <label for="">Department<em>*</em></label><br />
                  <select name="departmentUpdate" ref="departmentUpdateSelect" id="selectUpdateDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateDepartmentID" onfocus="this.selectedIndex = -1;" v-model="departmentEditing" v-if="isEditing">
                      <option v-for="dep in departmentsArray" :key="dep.department_id" :value="dep.name" :label="dep.name" :selected="dep.name===departmentEditing">({{dep.code}}) - {{ dep.name }}</option> 
                  </select>
                  <select name="department" ref="departmentSelect" id="selectDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setDepartmentID" onfocus="this.selectedIndex = -1;" v-model="department" required v-else>
                      <option value="" disabled selected>--Select Department--</option>
                      <option v-for="dep in departmentsArray" >({{dep.code}}) - {{ dep.name }}</option> 
                  </select>
                </div>
                <!-- <div class="basis-1/2 relative">
                  <label for="">Department Search<em>*</em></label><br />
                  <SearchableDropdown
                  />
                </div> -->
              </div>
              <div class="text-center" v-if="isEditing">
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateStaff(index)">Update</button>
              </div>
              <div class="text-center" v-else>
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createStaff">Save</button>
              </div>
              </form>
            </template>
            <template v-slot:footer> We Value Your Partnership </template>
        </Modal>


        <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
          <table class="min-w-full bg-white"> 
            <thead class="bg-gray-800 text-white">
              <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                <th class="text-left py-3 px-2">#</th>
                <th class="text-left py-3 px-2">Name</th>
                <th class="text-left py-3 px-2">Email</th>
                <th class="text-left py-3 px-2">Phone Number</th>
                <th class="text-left py-3 px-2">ID Number</th>
                <th class="text-left py-3 px-2">Profile</th>
                <th class="text-left py-3 px-2">Department</th>
                <th class="text-left py-3 px-2">Status</th>
                <th class="text-left py-3 px-2">Actions</th>
              </tr>
            </thead>
            <tbody>
        
              <tr v-for="(staff,index) in staffList" :key="staff.user_id" class="even:bg-gray-100">
                <td class="text-left py-3 px-2">{{ index + 1 }}</td>
                <td class="text-left py-3 px-2">{{ staff.first_name }} {{ staff.last_name }}</td>
                <td class="text-left py-3 px-2">{{ staff.email }}</td>
                <td class="text-left py-3 px-2">{{ staff.phone_number }}</td>
                <td class="text-left py-3 px-2">{{ staff.identification_no }}</td>
                <td class="text-left py-3 px-2">{{ staff.profile }}</td>
                <td class="text-left py-3 px-2">{{ staff.user_department }}</td>
                <td v-if="staff.is_active" class="text-left py-3 px-2">Active</td>
                <td v-else class="text-left py-3 px-2">Inactive</td>
                <td>
                    <div class="flex">
                        <div class="basis-1/3">
                            <button @click="editStaff(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                        </div>
                        <div class="basis-1/3">
                            <button v-if="staff.is_active" @click="lockStaff(index)"><i class="fa fa-unlock" aria-hidden="true" title="Lock Staff"></i></button>
                            <button v-else @click="unlockStaff(index)"><i class="fa fa-lock" aria-hidden="true" title="Unlock Staff"></i></button>
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
        <div class="pagination row-span-2">
          <MyPagination 
          :count="staffCount"
          :currentPage="currentPage"
          :result="staffArrLen"
          @loadPrev="loadPrev"
          @loadNext="loadNext"
          @firstPage="firstPage"
          @lastPage="lastPage"
          :showNextBtn="showNextBtn"
          :showPreviousBtn="showPreviousBtn"
          />
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
import SearchableDropdown from '@/components/SearchableDropdown.vue';

export default{
    name: 'StaffView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
      title: 'Hospital Management/ Staff',
      isModalVisible: false,
      first_name: '',
      search_name: '',
      last_name: '',
      email: '',
      search_user_department: '',
      image:null,
      imgName: "",
      phone_number: '',
      search_phone_number: '',
      profile: '',
      search_profile: '',
      dob: null,
      gender: '',
      id_number: '',
      search_id_number: '',
      userDetails: [],
      staffList: [],
      department: '',
      department_name: "",
      departmentEditing: '',
      payroll_number: '',
      specialization: '',
      temporary_password: '',
      is_staff: true,
      is_active: false,
      status: "",
      isEditing: false,
      isSearching: false,
      staffID: 0,
      companyID: "",
      currentPage: 1,
      staffCount: 0,
      staffArrLen: 0,
      staffResults: [],
      pageCount: 0,
      showNextBtn: false,
      showPreviousBtn: false,
      showOptions: false,
      departmentsArray: [],
      selectedDep: 0,
      selectedUpdateDep: 0,
      depID: 0,
      department_id: "",
      depName: "",
      depUpdateID: 0,
      depUpdateName: "",
      watcherMsg: [],
      eStyle: null, nStyle:null, bWidth: null,
    }
  },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker,
        SearchableDropdown
    },
    watch:{
      email(value){
        // binding this to the data value in the email input  
        this.email = value; 
        this.validateEmail(value);
        },
        phone_number(value){
            this.phone_number = value;
            this.validatePhoneNumber(value)
        },
    },
    methods:{
      formatDate(dateString) {
          const date = new Date(dateString);
          const year = date.getFullYear().toString()
          const month = ('0' + (date.getMonth() + 1)).slice(-2);
          const day = ('0' + date.getDate()).slice(-2);
          return `${year}-${month}-${day}`;
      },
      validateEmail(value){  
          if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value)){ 
              this.watcherMsg['email'] = '';
              this.eStyle = 'green';
              this.bWidth = 2

          } else{
              if(value == ''){
                  this.watcherMsg['email'] = ''; 
                  this.eStyle = ''

              }
              else{
                  this.watcherMsg['email'] = 'Invalid Email Address'; 
                  this.eStyle = 'red'
                  this.bWidth = 2
              }
          }  
      },
      validatePhoneNumber(value){
          if ((/^(?:254|\+254|0)?((?:(?:7(?:(?:[01249][0-9])|(?:5[789])|(?:6[89])))|(?:1(?:[1][0-5])))[0-9]{6})$/.test(value))|| (/^(?:254|\+254|0)?((?:(?:7(?:(?:3[0-9])|(?:5[0-6])|(8[5-9])))|(?:1(?:[0][0-2])))[0-9]{6})$/.test(value))){
                  this.nStyle = 'green';
                  this.watcherMsg['phone_number'] = ''
                  this.bWidth = 2

          }else{
              if(value == ''){
                  this.nStyle = '';
                  this.watcherMsg['phone_number'] = ''                        
              }
              else{
                  this.nStyle = 'red';
                  this.watcherMsg['phone_number'] = 'Invalid Phone Number'
                  this.bWidth = 2
              }
          }
      },
      fetchDepartments(){
        this.axios
        .get("api/v1/department-list/")
        .then((response)=>{
          this.departmentsArray = response.data.results;
        })
        .catch((error)=>{
          console.log(error.message)
        })
        .finally(()=>{
          
        })
      },
      setDepartmentID(){
        this.depID = 0;
        if(this.$refs.departmentSelect.selectedIndex > 0){
            this.selectedDep = this.$refs.departmentSelect.selectedIndex - 1;
            this.depID = this.departmentsArray[this.selectedDep].department_id;
        }
      },
      setUpdateDepartmentID(){
        this.depUpdateID = 0;
        if(this.$refs.departmentUpdateSelect.selectedIndex >= 0){
            this.selectedUpdateDep = this.$refs.departmentUpdateSelect.selectedIndex;
            this.depUpdateID = this.departmentsArray[this.selectedUpdateDep].department_id;
            this.depUpdateName = this.departmentsArray[this.selectedUpdateDep].name;
        }
      },
      onFileChange(e){
        this.image = e.target.files[0];
        console.log(this.image)
      },
      showModal(){
        if(this.isEditing == false){
          this.first_name = "";
          this.last_name = "";
          this.email = "";
          this.id_number = "";
          this.dob = "";
          this.gender = "";
          this.phone_number = "";
          this.department = "";
          this.profile = "";
        }
        this.isModalVisible = !this.isModalVisible;
        this.fetchDepartments();
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
      },
      createStaff(){

        this.showLoader();
        if(this.first_name === '' || this.last_name === '' || this.email === '' || this.id_number === '' ||
        this.gender === '' || this.profile === '' || this.dob === '' || this.phone_number === '' || this.department === '' ){
          this.$toast.error("Please Enter User Details",{
            duration: 5000,
            dismissible: true
          })
          this.hideLoader();
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
            let new_first_name = this.first_name[0].toUpperCase() + this.first_name.slice(1).toLowerCase();
            let new_last_name = this.last_name[0].toUpperCase() + this.last_name.slice(1).toLowerCase();
            let new_email = this.email.toLowerCase();
            let formData = new FormData();
            formData.append('first_name', new_first_name);
            formData.append('email', new_email);
            formData.append('last_name', new_last_name);
            formData.append('identification_no', this.id_number);
            formData.append('birth_date', this.formatDate(this.dob));
            formData.append('gender', this.gender);
            formData.append('phone_number', this.phone_number);
            formData.append('profile', this.profile);
            formData.append('password', this.temporary_password);
            formData.append('is_staff', this.is_staff);
            formData.append('is_active', this.is_staff);
            formData.append('user_department', this.depID);
            formData.append('allowed_company', this.companyID);
              
            this.axios
            .post("api/v1/users/", formData)
            .then((response)=>{
                this.userDetails = response.data;
                console.log("The user details are ",this.userDetails);
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
              .post(`api/v1/user-credentials/${this.userDetails.user_id}/`, formData)
              .then((response)=>{
              })
              .catch((error)=>{
                console.log(error.message);
              })
              .finally(()=>{
                let formData = {
                  company: this.companyID,
                  department: this.userDetails.user_department
                }
                this.axios
                .post("api/v1/fetch-departments/", formData)
                .then((response)=>{
                    this.department_name = response.data.name;
                })
                .catch((error)=>{
                  console.log(error.message);
                })
                .finally(()=>{
                  let formData = {
                    user_department_name: this.department_name,
                    phone_number: this.userDetails.phone_number,
                    birth_date: this.userDetails.birth_date,
                    allowed_company: this.userDetails.allowed_company,
                    user_department: this.userDetails.user_department
                  }
                  this.axios
                  .put(`api/v1/users/${this.userDetails.user_id}/`, formData)
                  .then((response)=>{
                    console.log(response.data);
                  })
                  .catch((error)=>{
                    console.log(error.message);
                  }).finally(()=>{
                    this.first_name = "";
                    this.last_name = "";
                    this.email = "";
                    this.id_number = "";
                    this.dob = "";
                    this.gender = "";
                    this.phone_number = "";
                    this.department = "";
                    this.profile = "";
                    this.image = null,
                    this.hideLoader();
                    this.$store.commit('reloadingPage')
                  })
                })
              })
            })

          })
        }
      },
      fetchStaff(){
        this.showNextBtn = false;
        this.showPreviousBtn = false;
        this.axios
        .get(`api/v1/systemusers/?page=${this.currentPage}`)
        .then((response)=>{
          for(let i=0; i<response.data.results.length; i++){
            if(response.data.results[i].profile != "Super Admin" && response.data.results[i].profile != "Patient"){
              this.staffList.push(response.data.results[i]);
            }
          }
          this.staffResults = response.data;
          this.staffArrLen = this.staffList.length;
          this.staffCount = this.staffResults.count;
          this.pageCount = Math.ceil(this.staffCount / 10);

          if(response.data.next){
              this.showNextBtn = true;
          }
          if(response.data.previous){
              this.showPreviousBtn = true;
          }
          
        })
        .catch((error)=>{
          console.log(error);
        })
      },
      editStaff(){
        this.isEditing = true;
        let selectedStaff = arguments[0];
        this.staffID = this.staffList[selectedStaff].user_id;
        this.axios
        .get(`api/v1/systemusers/${this.staffID}/`)
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
            this.departmentEditing = response.data.user_department_name;
            this.department_id = response.data.user_department;
        })
        .catch((error)=>{
            console.log(error.message);
        })
        .finally(()=>{
            this.scrollToTop();
            this.showModal();
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
                this.hideLoader();
            }
            else{
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
              formData.append('password', this.temporary_password);
              formData.append('is_staff', this.is_staff);
              formData.append('is_active', this.is_staff);
              console.log("The depUpdateID is ",this.depUpdateID);
              if(this.depUpdateID != 0){
                formData.append('user_department', this.depUpdateID);
                formData.append('user_department_name', this.depUpdateName);
              }else{
                formData.append('user_department', this.department_id);
                formData.append('user_department_name', this.departmentEditing);
              }
              formData.append('allowed_company', this.companyID);

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
                this.first_name = "";
                this.last_name = "";
                this.email = "";
                this.id_number = "";
                this.dob = "";
                this.gender = "";
                this.phone_number = "";
                this.profile = "";
                this.image = null,
                this.hideLoader();
                this.closeModal();
                this.$store.commit('reloadingPage');
              })
            }
        },
        lockStaff(){
          this.is_active = false;
          let selectedStaff = arguments[0];
          this.staffID = this.staffList[selectedStaff].user_id;
          this.$swal({
                title: "Are you sure?",
                text: `Do you wish to lock ${this.staffList[selectedStaff].first_name}'s account?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes, Lock it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
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
                      this.depID = response.data.user_department;
                  })
                  .catch((error)=>{
                      console.log(error.message);
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
                    formData.append('is_active', this.is_active);
                    formData.append('user_department', this.depID);
                    formData.append('allowed_company', this.companyID);
                    this.axios
                    .put("api/v1/users/"+ this.staffID+ "/", formData)
                    .then((response)=>{
                      this.$swal("Account Locked Successfully", {
                        icon: "success",
                      });
                    })
                    .catch((error)=>{
                      console.log(error.message);
                    })
                    .finally(()=>{
                      this.$store.commit("reloadingPage");
                    })
                  })
                
                } else {
                    this.$swal(`${this.staffList[selectedStaff].first_name} has not been locked!`);
                    this.is_active = false;
                }
            });
          
        },
        unlockStaff(){
          this.is_active = true;
          let selectedStaff = arguments[0];
          this.staffID = this.staffList[selectedStaff].user_id;
          this.$swal({
                title: "Are you sure?",
                text: `Do you wish to unlock ${this.staffList[selectedStaff].first_name}'s account?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes, Unlock it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
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
                      this.depID = response.data.user_department;
                  })
                  .catch((error)=>{
                      console.log(error.message);
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
                    formData.append('is_active', this.is_active);
                    formData.append('user_department', this.depID);
                    formData.append('allowed_company', this.companyID);
                    this.axios
                    .put("api/v1/users/"+ this.staffID+ "/", formData)
                    .then((response)=>{
                      this.$swal("Account Unlocked Successfully", {
                        icon: "success",
                      });
                    })
                    .catch((error)=>{
                      console.log(error.message);
                    })
                    .finally(()=>{
                      this.$store.commit("reloadingPage");
                    })
                  })
                
                } else {
                    this.$swal(`${this.staffList[selectedStaff].first_name} has not been unlocked!`);
                    this.is_active = false;
                }
            });
          
        },
        removeStaff(){
          let selectedStaff = arguments[0];
          this.staffID = this.staffList[selectedStaff].user_id;
          this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.staffList[selectedStaff].first_name}'s account?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes, Delete it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                  this.axios
                  .delete("api/v1/user-details/"+ this.staffID+ "/")
                  .then((response)=>{
                    this.$swal("Account Deleted Successfully", {
                      icon: "success",
                    });
                  })
                  .catch((error)=>{
                    console.log(error.message);
                  })
                  .finally(()=>{
                    this.$store.commit("reloadingPage");
                  })
                } 
                else {
                    this.$swal(`${this.staffList[selectedStaff].first_name} has not been deleted!`);
                    this.is_active = false;
                }
            });
          
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            this.searchStaff();
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            this.searchStaff();
        },
        firstPage(){
            if(this.pageCount > 1){
              this.currentPage = 1;
              this.searchStaff();
            }
        },
        lastPage(){
            if(this.pageCount > 1){
              this.currentPage = this.pageCount;
              this.searchStaff();
            }
        },
        searchStaff(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            this.staffList = [];
            let formData = {
              user_department: this.search_user_department,
              name: this.search_name,
              is_active: this.status,
              identification_no: this.search_id_number,
              profile: this.search_profile,
              phone_number: this.search_phone_number,
              company_id: this.companyID,
            }
            this.axios
            .post(`api/v1/staff-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.staffList = response.data.results;
                this.staffResults = response.data;
                this.staffArrLen = this.staffList.length;
                this.staffCount = this.staffResults.count;
                this.pageCount = Math.ceil(this.staffCount / 10);

                if(response.data.next){
                    this.showNextBtn = true;
                }
                if(response.data.previous){
                    this.showPreviousBtn = true;
                }
            })
            .catch((error)=>{
                console.log(error);
            })
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportStaffPDF(){
            this.showLoader();
            let formData = {
              user_department: this.search_user_department,
              name: this.search_name,
              is_active: this.status,
              identification_no: this.search_id_number,
              profile: this.search_profile,
              phone_number: this.search_phone_number,
              company_id: this.companyID,
            }
            this.axios
            .post(`api/v1/export-staff-pdf/?page=${this.currentPage}`, formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff.pdf');
                  document.body.appendChild(link);
                  link.click();
                }
            })
            .catch((error)=>{
                console.log(error);
            })
            .finally(()=>{
                this.hideLoader();
            })
        },
        exportStaffExcel(){
            this.showLoader();
            let formData = {
              user_department: this.search_user_department,
              name: this.search_name,
              is_active: this.status,
              identification_no: this.search_id_number,
              profile: this.search_profile,
              phone_number: this.search_phone_number,
              company_id: this.companyID,
            }
            this.axios
            .post(`api/v1/export-staff-excel/?page=${this.currentPage}`, formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff.xls');
                  document.body.appendChild(link);
                  link.click();
                }
            })
            .catch((error)=>{
                console.log(error);
            })
            .finally(()=>{
                this.hideLoader();
            })
        },
        exportStaffCSV(){
            this.showLoader();
            let formData = {
              user_department: this.search_user_department,
              name: this.search_name,
              is_active: this.status,
              identification_no: this.search_id_number,
              profile: this.search_profile,
              phone_number: this.search_phone_number,
              company_id: this.companyID,
            }
            this.axios
            .post(`api/v1/export-staff-csv/?page=${this.currentPage}`, formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff.csv');
                  document.body.appendChild(link);
                  link.click();
                }
            })
            .catch((error)=>{
                console.log(error);
            })
            .finally(()=>{
                this.hideLoader();
            })
        },
        
    },
    mounted(){
      this.companyID = localStorage.getItem("company_id")
      this.searchStaff();
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