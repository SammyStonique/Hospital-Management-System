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
        <h2 class="text-center font-bold">Doctors Register</h2>
        <div class="md:px-4 pt-4 pb-1 w-full border-b-2 border-gray-300 mb-6">
          <div class="mb-4 flex items-end h-24">
            <div class="basis-1/6 pl-3">
              <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Doctor</button>
            </div>
            <div class="basis-3/4">
              <div class="flex mb-3">
                <div class="basis-1/3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="first_name" id="" placeholder="First Name...." v-model="search_first_name" @keyup.enter="searchDoctor">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="last_name" id="" placeholder="Last Name...." v-model="search_last_name"  @keyup.enter="searchDoctor">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                  <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="specialization" id="" placeholder="Specialization...." v-model="search_specialization"  @keyup.enter="searchDoctor">
                </div>
              </div>
              <div class="flex">
                <div class="basis-1/3 items-center">
                  <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="payroll_number" id="" placeholder="Payroll Number...." v-model="search_payroll_number"  @keyup.enter="searchDoctor">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="Department" id="" placeholder="Department...." v-model="search_doctor_department" @keyup.enter="searchDoctor">
                </div>
                <div class="basis-1/3 pl-3 items-center">
                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="Phone Number" id="" placeholder="Phone Number...." v-model="search_phone_number" @keyup.enter="searchDoctor">
                </div>
              </div>
            </div>
            <div class="basis-1/8 pl-3 items-center w-36">
                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchDoctor"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
            </div>
            <div class="basis-1/8 pl-3 w-36">
                <div class="print-dropdown">
                    <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                    <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                </div>
                <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                    <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                    <button @click="exportDoctorPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                    <button @click="exportDoctorExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                    <button @click="exportDoctorCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                </div>
            </div>
          </div>
        </div>
        <!-- MODAL component for adding a new doctor -->
        <Modal v-show="isModalVisible" @close="closeModal">
            <template v-slot:header> Doctor Details </template>
            <template v-slot:body>
              <form action="" @submit.prevent="">
                <div class="flex mb-6">
                  <div class="basis-1/2 mr-6">
                    <label for="">First Name<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="first_name" required>
                  </div>
                  <div class="basis-1/2">
                    <label for="">Last Name<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="last_name" required>
                  </div>
              </div>
              <div class="flex mb-6">
                  <div class="basis-1/2 mr-6" v-if="isEditing">
                    <label for="">Email<em>*</em></label><br />
                    <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2 w-60" v-model="email" required>
                  </div>
                  <div class="basis-1/2 mr-6" v-else>
                    <label for="">Email<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" v-model="email" :style="{borderColor: eStyle,borderWidth: bWidth+'px' }" required><br />
                    <span v-if="watcherMsg.email" :style="{color: eStyle, fontSize:10 + 'px'}">{{watcherMsg.email}}</span>
                  </div>
                  <div class="basis-1/2">
                    <label for="">Phone Number<em>*</em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" placeholder="e.g 07XXXX" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px' }" required><br />
                    <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                  </div>
              </div>
              <div class="flex mb-6">
                <div class="basis-1/2 mr-6">
                    <label for="">Payroll Number<em></em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="payroll_number">
                </div>
                <div class="basis-1/2">
                    <label for="">Specialization<em></em></label><br />
                    <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="specialization">
                </div>
              </div>
              <div class="flex mb-6">
                <div class="basis-1/2">
                  <label for="">Department<em>*</em></label><br />
                  <select name="departmentUpdate" ref="departmentUpdateSelect" id="selectUpdateDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateDepartmentID" onfocus="this.selectedIndex = -1;" v-model="departmentEditing" v-if="isEditing">
                      <option v-for="dep in departmentsArray" :key="dep.id" :value="dep.name" :label="dep.name" :selected="dep.name===departmentEditing">({{dep.code}}) - {{ dep.name }}</option> 
                  </select>
                  <select name="department" ref="departmentSelect" id="selectDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setDepartmentID" onfocus="this.selectedIndex = -1;" v-model="department" required v-else>
                      <option value="" disabled selected>--Select Department--</option>
                      <option v-for="dep in departmentsArray" >({{dep.code}}) - {{ dep.name }}</option> 
                  </select>
                </div>
                <div class="basis-1/2" v-if="!isEditing">
                  <label for="">User<em>*</em></label><br />
                  <select name="user" ref="userSelect" id="selectUser" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUserID" onfocus="this.selectedIndex = -1;" v-model="user" required>
                      <option value="" disabled selected>--Select User--</option>
                      <option v-for="doc in doctorsArray" >({{doc.first_name}}) {{ doc.last_name }} - #{{ doc.identification_no }}</option> 
                  </select>
                </div>
              </div>
              <div class="text-center" v-if="isEditing">
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateDoctor(index)">Update</button>
              </div>
              <div class="text-center" v-else>
                  <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createDoctor">Save</button>
              </div>
              </form>
            </template>
            <template v-slot:footer> We Value Your Partnership </template>
        </Modal>


        <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
          <table class="min-w-full bg-white"> 
            <thead class="bg-gray-800 text-white">
              <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                <th class="text-left py-3 px-4">#</th>
                <th class="text-left py-3 px-4">F. Name</th>
                <th class="text-left py-3 px-4">L. Name</th>
                <th class="text-left py-3 px-4">Email</th>
                <th class="text-left py-3 px-4">Phone No.</th>
                <th class="text-left py-3 px-4">P.R No.</th>
                <th class="text-left py-3 px-4">Department</th>
                <th class="text-left py-3 px-4">Specialization</th>
                <th class="text-left py-3 px-4">Actions</th>
              </tr>
            </thead>
            <tbody>
        
              <tr v-for="(doct,index) in doctorsList" :key="doct.id" class="even:bg-gray-100">
                <td class="text-left py-3 px-2">{{ index + 1 }}</td>
                <td class="text-left py-3 px-2">{{ doct.first_name }}</td>
                <td class="text-left py-3 px-2">{{ doct.last_name }}</td>
                <td class="text-left py-3 px-2">{{ doct.email }}</td>
                <td class="text-left py-3 px-2">{{ doct.phone_number }}</td>
                <td class="text-left py-3 px-2">{{ doct.payroll_number}}</td>
                <td class="text-left py-3 px-2">{{ doct.department}}</td>
                <td class="text-left py-3 px-2">{{ doct.specialization }}</td>
                <td>
                    <div class="flex">
                        <div class="basis-1/2 text-center">
                            <button @click="editDoctor(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                        </div>
                        <div class="basis-1/2 text-center">
                            <button @click="removeDoctor(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                        </div>
                    </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="pagination row-span-2">
          <MyPagination 
          :count="doctCount"
          :currentPage="currentPage"
          :result="doctArrLen"
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

export default{
    name: 'DoctorsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
      title: 'Hospital Management/ Doctors',
      user: "",
      isModalVisible: false,
      first_name: '',
      search_first_name: '',
      last_name: '',
      search_last_name: '',
      email: '',
      search_doctor_department: '',
      phone_number: '',
      search_phone_number: '',
      id_number: '',
      userDetails: [],
      doctorsList: [],
      newDoctorsList: [],
      departmentList: [],
      department: '',
      department_id: "",
      departmentEditing: '',
      payroll_number: '',
      search_payroll_number: '',
      specialization: '',
      search_specialization: '',
      isEditing: false,
      doctID: "",
      userID: "",
      doctName: '',
      currentPage: 1,
      doctCount: 0,
      doctArrLen: 0,
      doctResults: [],
      pageCount: 0,
      showNextBtn: false,
      showPreviousBtn: false,
      showOptions: false,
      departmentsArray: [],
      doctorsArray: [],
      selectedDep: 0,
      selectedUser: 0,
      selectedUpdateDep: 0,
      depID: "",
      depUpdateID: "",
      isSearching: false,
      watcherMsg: [],
      eStyle: null, nStyle:null, bWidth: null,
    }
  },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination
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
        let formData = {
          company: this.hospID
        }
        this.axios
        .post("api/v1/fetch-departments/", formData)
        .then((response)=>{
          this.departmentsArray = response.data;
        })
        .catch((error)=>{
          console.log(error.message)
        })
        .finally(()=>{
          
        })
      },
      setDepartmentID(){
        this.depID = "";
        if(this.$refs.departmentSelect.selectedIndex > 0){
            this.selectedDep = this.$refs.departmentSelect.selectedIndex - 1;
            this.depID = this.departmentsArray[this.selectedDep].department_id;
            let depName = this.departmentsArray[this.selectedDep].name;
        }
        this.fetchDoctorUsers();
      },
      setUpdateDepartmentID(){
        this.depUpdateID = "";
        if(this.$refs.departmentUpdateSelect.selectedIndex >= 0){
            this.selectedUpdateDep = this.$refs.departmentUpdateSelect.selectedIndex;
            this.depUpdateID = this.departmentsArray[this.selectedUpdateDep].department_id;
            let depName = this.departmentsArray[this.selectedUpdateDep].name;
        }
      },
      setUserID(){
        this.userID = "";
        if(this.$refs.userSelect.selectedIndex > 0){
            this.selectedUser = this.$refs.userSelect.selectedIndex - 1;
            this.userID = this.doctorsArray[this.selectedUser].user_id;
            let doctName = this.doctorsArray[this.selectedUser].first_name;
        }
      },
      fetchDoctorUsers(){
        let formData = {
          company: this.hospID,
          department: this.depID
        }
        this.axios
        .post("api/v1/department-staff-list/", formData)
        .then((response)=>{
          this.doctorsArray = response.data;
        })
        .catch((error)=>{
          console.log(error.message)
        })
        .finally(()=>{
          
        })
      },
      showModal(){
        if(this.isEditing == false){
          this.first_name = "";
          this.last_name = "";
          this.email = "";
          this.payroll_number = "";
          this.specialization = "";
          this.phone_number = "";
          this.department = "";
          this.user = "";
        }
        this.isModalVisible = !this.isModalVisible;
        this.fetchDepartments();
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
      },
      createDoctor(){
        this.showLoader();
        if(this.first_name === '' || this.last_name === '' || this.email === '' || this.payroll_number === '' ||
         this.phone_number === '' || this.department === '' || this.specialization === '' || this.user === '' ){
          this.$toast.error("Please Enter Doctor Details",{
            duration: 5000,
            dismissible: true
          })
          this.hideLoader();
        }else{
          let new_first_name = this.first_name[0].toUpperCase() + this.first_name.slice(1).toLowerCase();
          let new_last_name = this.last_name[0].toUpperCase() + this.last_name.slice(1).toLowerCase();
          let new_email = this.email.toLowerCase();
          let new_specialization = "";
          let x = this.specialization.split(" ");
          for(let i=0; i<x.length; i++){
              new_specialization += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
          }
          let formData = {
            user: this.userID,
            payroll_number: this.payroll_number,
            first_name: new_first_name,
            last_name: new_last_name,
            email: new_email,
            department: this.depID,
            specialization: new_specialization,
            phone_number: this.phone_number,
            hospital: this.hospID
          }
          this.axios
          .post("api/v1/create-department-doctor/", formData)
          .then((response)=>{
            this.$toast.success("Doctor Created Succesfully",{
              duration: 3000,
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
            this.user = "";
            this.specialization = "";
            this.payroll_number = "";
            this.phone_number = "";
            this.department = "";
            this.hideLoader();
          })
        }
      }, 
      editDoctor(){
        this.isEditing = true;
        let selectedDoctor = arguments[0];
        this.doctID = this.doctorsList[selectedDoctor].doctor_id;
        this.depID = this.doctorsList[selectedDoctor].department_id;
        let formData = {
          hospital: this.hospID,
          doctor: this.doctID,
          department: this.depID
        }
        this.axios
        .post("api/v1/get-department-doctors/", formData)
        .then((response)=>{
            this.first_name = response.data.first_name;
            this.last_name = response.data.last_name;
            this.email = response.data.email;
            this.payroll_number = response.data.payroll_number;
            this.phone_number = response.data.phone_number;
            this.departmentEditing = response.data.department;
            this.department_id = response.data.department;
            this.specialization = response.data.specialization;
            this.user = response.data.user;
        })
        .catch((error)=>{
            console.log(error.message);
        })
        .finally(()=>{
          let formData = {
            department: this.departmentEditing,
            company: this.hospID
          }
          this.axios
          .post("api/v1/fetch-departments/", formData)
          .then((response)=>{
            this.departmentEditing = response.data.name;
          })
          .catch((error)=>{
            console.log(error.message);
          })
          .finally(()=>{
            this.scrollToTop();
            this.showModal();
          })
            
        })

      },
      updateDoctor(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === ''
               || this.departmentEditing === '' || this.phone_number === '' ){
                this.$toast.error("Please Enter Doctor Details",{
                    duration:5000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
              let new_first_name = this.first_name[0].toUpperCase() + this.first_name.slice(1).toLowerCase();
              let new_last_name = this.last_name[0].toUpperCase() + this.last_name.slice(1).toLowerCase();
              let new_email = this.email.toLowerCase();
              let new_specialization = "";
              let x = this.specialization.split(" ");
              for(let i=0; i<x.length; i++){
                  new_specialization += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
              }
              let formData = new FormData();
              formData.append('doctor', this.doctID);
              formData.append('first_name', new_first_name);
              formData.append('email', new_email);
              formData.append('last_name', new_last_name);
              formData.append('payroll_number', this.payroll_number);
              formData.append('phone_number', this.phone_number);
              formData.append('specialization', new_specialization);
              if(this.depUpdateID != 0){
                formData.append('department', this.depUpdateID);
              }else{
                formData.append('department', this.department_id);
              }
              formData.append('hospital', this.hospID);

              this.axios
              .put("api/v1/update-department-doctor/", formData)
              .then((response)=>{
                  this.$toast.success("Doctor Succesfully Updated",{
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
                this.payroll_number = "";
                this.specialization = "";
                this.departmentEditing = "";
                this.phone_number = "";
                this.user = "";
                this.hideLoader();
                this.closeModal();
                this.$store.commit('reloadingPage');
              })
            }
        },
        removeDoctor() {
            let selectedItem = arguments[0];
            this.doctID = this.doctorsList[selectedItem].doctor_id;
            this.depID = this.doctorsList[selectedItem].department_id;
            this.doctName = this.doctorsList[selectedItem].first_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete Dr. ${this.doctName}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                  let formData = {
                    hospital: this.hospID,
                    doctor: this.doctID,
                    department: this.depID
                  }
                  this.axios
                  .post("api/v1/delete-doctor/", formData)
                  .then((response)=>{
                      this.$swal("Poof! Doctor removed succesfully!", {
                          icon: "success",
                      });
                  })
                  .catch((error)=>{
                      console.log(error.message);
                  })
                  .finally(()=>{
                      this.$store.commit("reloadingPage");
                  })
                
                } else {
                    this.$swal(`Dr. ${this.doctName} has not been deleted!`);
                }
            });
        },
        loadNext(){
          if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            this.searchDoctor();
        },
        loadPrev(){
          if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            this.searchDoctor();
        },
        firstPage(){
          if(this.pageCount > 1){
              this.currentPage = 1;
              this.searchDoctor();
            }
        },
        lastPage(){
          if(this.pageCount > 1){
              this.currentPage = this.pageCount;
              this.searchDoctor();
            }
        },
        searchDoctor(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            this.doctorsList = [];
            let formData = {
              first_name: this.search_first_name,
              last_name: this.search_last_name,
              specialization: this.search_specialization,
              department: this.search_doctor_department,
              payroll_number: this.search_payroll_number,
              phone_number: this.search_phone_number,
              hospital: this.hospID,
            }
            this.axios
            .post(`api/v1/doctor-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.doctorsList = response.data.results;
                this.doctResults = response.data;
                this.doctArrLen = this.doctorsList.length;
                this.doctCount = this.doctResults.count;
                this.pageCount = Math.ceil(this.doctCount / 10);

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
        exportDoctorPDF(){
            this.showLoader();
            let formData = {
              first_name: this.search_first_name,
              last_name: this.search_last_name,
              specialization: this.search_specialization,
              department: this.search_doctor_department,
              payroll_number: this.search_payroll_number,
              phone_number: this.search_phone_number,
              hospital: this.hospID,
            }
            this.axios
            .post("api/v1/export-doctors-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Doctors.pdf');
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
        exportDoctorExcel(){
            this.showLoader();
            let formData = {
              first_name: this.search_first_name,
              last_name: this.search_last_name,
              specialization: this.search_specialization,
              department: this.search_doctor_department,
              payroll_number: this.search_payroll_number,
              phone_number: this.search_phone_number,
              hospital: this.hospID,
            }
            this.axios
            .post("api/v1/export-doctors-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Doctors.xls');
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
        exportDoctorCSV(){
            this.showLoader();
            let formData = {
              first_name: this.search_first_name,
              last_name: this.search_last_name,
              specialization: this.search_specialization,
              department: this.search_doctor_department,
              payroll_number: this.search_payroll_number,
              phone_number: this.search_phone_number,
              hospital: this.hospID,
            }
            this.axios
            .post("api/v1/export-doctors-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Doctors.csv');
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
      this.hospID = localStorage.getItem("company_id")
      this.searchDoctor();
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