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
    <div class="main-content grid grid-rows-12 bg-gray-100 px-4 py-4">
        <div class="subsection row-span-2 rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Departments</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="basis-1/5 pl-3">
                        <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Deptmnt</button>
                    </div>
                    <div class="basis-1/5 pl-3 items-center">
                       <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="code" id="" placeholder="Code" v-model="code" @keyup.enter="searchDepartment">
                    </div>
                    <div class="basis-1/5 pl-3 items-center">
                       <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name" v-model="name"  @keyup.enter="searchDepartment">
                    </div>
                    <div class="basis-1/5 pl-3">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchDepartment"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/5 pl-3">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportDepartmentsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportDepartmentsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportDepartmentsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new department -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Department Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-4">
                        <div class="basis-1/2">
                            <label for="">Department ID<em>*</em></label>
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="dep_code">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="flex mb-4">
                        <div class="basis-1/2">
                            <label for="">Department Name<em>*</em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="dep_name">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateDepartment(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createDepartment">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> HMS. </template>
                </Modal>
                <!-- MODAL component for adding a new manager -->
                <Modal v-show="managerModalVisible" @close="closeManagerModal" :index="index">
                    <template v-slot:header> Manager Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-4">
                            <div class="basis-1/2 mr-4">
                                <label for="">Department<em>*</em></label><br />
                                <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-200 text-lg pl-2" placeholder="Department" v-model="department">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Manager<em>*</em></label><br />
                                <select name="user" ref="userSelect" id="selectUser" class="rounded border border-gray-600 text-lg pl-2 pt-2 w-60" @change="setUserID" onfocus="this.selectedIndex = -1;" v-model="manager">
                                    <option value="" disabled selected>---Select Manager---</option> 
                                    <option v-for="stf in staffArray">{{stf.first_name}}  {{stf.last_name}} - #{{ stf.identification_no }}</option> 
                                </select>
                            </div>
                        </div>
                        <div class="flex mb-4">
                            <div class="basis-1/2 mr-4">
                                <label for="">Start Date<em>*</em></label><br />
                                <input type="date" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="start_date">
                            </div>
                            <div class="basis-1/2">
                                <label for="">End Date<em></em></label><br />
                                <input type="date" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="end_date">
                            </div>
                        </div>
                        <div class="flex mb-4">
                            <div class="basis-1/2 mr-4">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" placeholder="e.g 07XXXX" v-model="phone_number">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Status<em>*</em></label><br />
                                <select name="" ref="" id="" class="rounded border border-gray-600 text-lg pl-2 pt-2 w-60"  v-model="status">
                                  <option value="" selected disabled>---Select Status</option>
                                  <option value="Active">Active</option>
                                  <option value="Inactive">Inactive</option> 
                                </select>
                            </div>
                        </div>
                        <div class="text-center">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createManager">Save</button>
                        </div>

                    </form>
                    </template>
                    <template v-slot:footer> HMS. </template>
                </Modal>
                <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                    <table class="min-w-full bg-white"> 
                        <thead class="bg-gray-800 text-white">
                            <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                <th>#</th>
                                <th class="text-left py-3 px-4">Code</th>
                                <th class="text-left py-3 px-4">Name</th>
                                <th class="text-left py-3 px-4">Manager</th>
                                <th class="text-left py-3 px-4">Start Date</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(det,index) in depList" :key="det.id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ det.code }}</td>
                            <td class="text-left py-3 px-4">{{ det.name }}</td>
                            <td class="text-left py-3 px-4">{{ det.manager_first_name }} {{ det.manager_last_name }}</td>
                            <td class="text-left py-3 px-4">{{ det.start_date }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editDepartment(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/3">
                                        <button @click="showManagerModal(index)"><i class="fa fa-plus-square-o" aria-hidden="true" title="Add Manager"></i></button>
                                    </div>
                                    <div class="basis-1/3">
                                        <button @click="removeDepartment(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="depCount"
                    :currentPage="currentPage"
                    :result="depArrLen"
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
    </div>
</template>

<script>

import Loader from '@/components/Loader.vue'
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'
import { getTransitionRawChildren } from 'vue'


export default{
    name: 'DepartmentsView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Departments',
            isModalVisible: false,
            managerModalVisible: false,
            dep_code: "",
            dep_name: "",
            department: "",
            start_date: "",
            end_date: "",
            manager: "",
            phone_number: "",
            status: "",
            isEditing: false,
            depID: 0,
            managerDepID: 0,
            userID: 0,
            currentPage: 1,
            depCount: 0,
            depArrLen: 0,
            depResults: [],
            newDepList: [],
            depList: [],
            manager_department: 0,
            manager_user: 0,
            manager_start_date: "",
            manager_phone_number: "",
            manager_status: "",
            manager_id: 0,
            managerList: [],
            managerArr: [],
            newManagerArr: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            code: '',
            name: '',
            showOptions: false,
            staffArray: [],
        }
    },
    components: {
        NavBar,
        SideBar,
        Modal,
        MyPagination,
        Loader
    },
    methods:{
        fetchStaff(department){
        this.staffArray = [];
        this.axios
        .get("api/v1/user-list/")
        .then((response)=>{
            for(let i=0; i<response.data.results.length; i++){
                if(response.data.results[i].profile != "Super Admin" && response.data.results[i].profile != "Patient" && response.data.results[i].user_department == department  ){
                    this.staffArray.push(response.data.results[i]);
                }
            }
        })
        .catch((error)=>{
          console.log(error.message)
        })
        .finally(()=>{
          
        })
      },
      setUserID(){
        this.userID = 0;
        if(this.$refs.userSelect.selectedIndex > 0){
            this.selectedDep = this.$refs.userSelect.selectedIndex - 1;
            this.userID = this.staffArray[this.selectedDep].id;
            this.phone_number = this.staffArray[this.selectedDep].phone_number;
            let userName = this.staffArray[this.selectedDep].first_name;
        }
      },
      showModal(){
        if(this.isEditing == false){
          this.dep_code = "";
          this.dep_name = "";
        }
        this.isModalVisible = !this.isModalVisible;
      },
      showManagerModal(){
        this.scrollToTop();
        let selectedDepartment = arguments[0];
        this.department = this.depList[selectedDepartment].name;
        this.managerDepID = this.depList[selectedDepartment].id;
        this.managerModalVisible = !this.managerModalVisible;
        this.fetchStaff(this.department);
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
      },
      closeManagerModal(){
        this.managerModalVisible = false;
        this.manager = "";
        this.start_date = "";
        this.end_date = "";
        this.phone_number = "";
        this.status = "";
      },
      createDepartment(){
        this.showLoader();
        if(this.dep_code === '' || this.dep_name === ''){
          this.$toast.error("Please Enter Department Details",{
            duration: 5000,
            dismissible: true
          })
        }
        else{
            let formData = {
                code: this.dep_code,
                name: this.dep_name
            }
          this.axios
          .post("api/v1/department-list/", formData)
          .then((response)=>{
            this.$toast.success("Department Successfully Added",{
                duration: 5000,
                dismissible: true
            })
          })
          .catch((error)=>{
            console.log(error.message);
          })
          .finally(()=>{
            this.hideLoader();
            this.dep_code = "";
            this.dep_name = "";
          })
        }
      },
      fetchDepartments(){
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            this.axios
            .get(`api/v1/departments/?page=${this.currentPage}`)
            .then((response)=>{
                this.newDepList = response.data.results;
                this.depResults = response.data;
                this.depArrLen = this.newDepList.length;
                this.depCount = this.depResults.count;
                this.pageCount = Math.ceil(this.depCount / 10);

                if(response.data.next){
                    this.showNextBtn = true;
                }
                if(response.data.previous){
                    this.showPreviousBtn = true;
                }
            })
            .catch((error)=>{
                console.log(error.message);
            })
            .finally(()=>{
                for(let i=0; i<this.newDepList.length; i++){
                    this.axios
                    .get(`api/v1/get-manager/${this.newDepList[i].id}`)
                    .then((response)=>{
                       
                        if(response.data.managers.length){
                            this.managerList = response.data.managers[0];
                            this.newDepList[i] = this.managerList;
                        }
                    })
                    .catch((error)=>{
                        // console.log(error.message);
                    })
                }
                this.depList = this.newDepList;
            })
        },
        editDepartment(){
            this.isEditing = true;
            let selectedDepartment = arguments[0];
            this.depID = this.depList[selectedDepartment].id;
            console.log("The depList is ",this.depList);
            this.axios
            .get(`api/v1/department-details/${this.depID}/`)
            .then((response)=>{
                this.dep_code = response.data.code;
                this.dep_name = response.data.name;
            })
            .catch((error)=>{
                console.log(error.message);
            })
            .finally(()=>{
                this.scrollToTop();
                this.showModal();

            })

        },
        updateDepartment(){
            this.showLoader();
            if(this.dep_code === "" || this.dep_name === ""){
                this.$toast.error("Please Enter Department Details",{
                    duration:5000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = {
                    code: this.dep_code,
                    name: this.dep_name,
                }
                this.axios
                .put("api/v1/department-details/"+this.depID+"/", formData)
                .then((response)=>{
                    this.$toast.success("Department Succesfully Updated",{
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
        removeDepartment() {
            let selectedItem = arguments[0];
            this.depID = this.depList[selectedItem].id;
            this.depName = this.depList[selectedItem].name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.depName}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                this.axios
                .delete("api/v1/department-details/"+this.depID+"/")
                .then((response)=>{
                    this.$swal("Poof! Department removed succesfully!", {
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
                    this.$swal(`${this.depName} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }

            this.fetchDepartments();
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.fetchDepartments();
        },
        firstPage(){
            this.currentPage = 1;
            this.fetchDepartments();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.fetchDepartments();
        },
        searchDepartment(){
            let formData = {
                code: this.code,
                name: this.name,
            }
            this.axios
            .post("api/v1/department-search/",formData)
            .then((response)=>{
                this.depList = response.data.departments;
                this.depArrLen = response.data.departments.length;
                // this.fetchDepartments();
            })
            .catch((error)=>{
                console.log(error);
            })
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportDepartmentsPDF(){
            this.showLoader();
            this.axios
            .get("api/v1/export-departments-pdf/", { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Departments.pdf');
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
        exportDepartmentsExcel(){
            this.showLoader();
            this.axios
            .get("api/v1/export-departments-excel/", { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Departments.xls');
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
        exportDepartmentsCSV(){
            this.showLoader();
            this.axios
            .get("api/v1/export-departments-csv/", { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Departments.csv');
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

        // MANAGER METHODS
        createManager(){
            this.showLoader();
            if(this.department === '' || this.manager === '' || this.start_date === ''
                 || this.phone_number === '' || this.status === ''){
                this.$toast.error("Please Enter Manager Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = {
                    department: this.managerDepID,
                    user: this.userID,
                    start_date: this.start_date,
                    phone_number: this.phone_number,
                    status: this.status,
                }
                this.axios
                .post("api/v1/manager-list/", formData)
                .then((response)=>{
                    console.log(response.data);
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.axios
                    .get("api/v1/manager-list/")
                    .then((response)=>{
                        this.managerArr = response.data.results;
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        for(let i=1; i<this.managerArr.length; i++){
                            if(this.managerArr[i].department == this.managerDepID){
                                this.newManagerArr.push(this.managerArr[i]);
                            }
                        }
                        this.manager_status= "Inactive";
                        this.manager_department = this.newManagerArr[0].department;
                        this.manager_user = this.newManagerArr[0].user;
                        this.manager_phone_number = this.newManagerArr[0].phone_number;
                        this.manager_start_date = this.newManagerArr[0].start_date;
                        this.manager_id = this.newManagerArr[0].id;

                        let formData = {
                            department: this.manager_department,
                            user: this.manager_user,
                            start_date: this.manager_start_date,
                            phone_number: this.manager_phone_number,
                            end_date: this.start_date,
                            status: this.manager_status,
                        }
                        this.axios
                           .put("api/v1/manager-details/"+this.manager_id+"/", formData)
                           .then((response)=>{

                           })
                           .catch((error)=>{
                            console.log(error.message);
                           })
                           .finally(()=>{
                                this.$toast.success("Manager Added Succesfully",{
                                    duration: 3000,
                                    dismissible: true
                                })
                                this.department = "";
                                this.user = "";
                                this.start_date = "";
                                this.end_date = "";
                                this.status = "";
                                this.phone_number = "";
                                this.manager_status= "Inactive";
                                this.manager_department = 0;
                                this.manager_user = 0;
                                this.manager_phone_number = "";
                                this.manager_start_date = "";
                                this.manager_id = 0;
                                this.hideLoader();
                                this.closeManagerModal();
                                this.$store.commit('reloadingPage');
                           })
                    })
                    
                })
            }
        },
    },
    mounted(){
        this.fetchDepartments();
    }
}
</script>

<style scoped>
.main-content{
  z-index: 1;
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
.pagination{
    bottom: 20px;
}
em{
  color: red;
}
.options-container {
  width: 150px;

}
.dropdown-button{
    z-index: 1;
}
.inset-button{
    min-height: 100vh;
}
</style>