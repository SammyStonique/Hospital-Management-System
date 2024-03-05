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
    <div class="main-content grid grid-rows-12 bg-gray-100 px-4 py-4">
        <div class="subsection row-span-2 rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Departments</h2>
            <div class="md:px-4 pt-4 pb-1 w-full border-b-2 border-gray-300 mb-6">
                <div class="mb-4 flex items-end h-24">
                    <div class="basis-1/4 pl-3">
                        <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Department</button>
                    </div>
                    <div class="basis-3/4">
                        <div class="flex items-end">
                            <div class="basis-1/2 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="code" id="" placeholder="Code..." v-model="code" @keyup.enter="searchDepartment">
                            </div>
                            <div class="basis-1/2 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name..." v-model="name"  @keyup.enter="searchDepartment">
                            </div>
                        </div>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchDepartment"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportDepartmentsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportDepartmentsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportDepartmentsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new department -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Department Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Department ID<em>*</em></label>
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="dep_code">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="flex mb-6">
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
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>
                <!-- MODAL component for adding a new manager -->
                <Modal v-show="managerModalVisible" @close="closeManagerModal" :index="index">
                    <template v-slot:header> Manager Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-4">
                                <label for="">Department<em>*</em></label><br />
                                <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" placeholder="Department" v-model="department">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Manager<em>*</em></label><br />
                                <select name="user" ref="userSelect" id="selectUser" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUserID" onfocus="this.selectedIndex = -1;" v-model="manager">
                                    <option value="" disabled selected>---Select Manager---</option> 
                                    <option v-for="stf in staffArray">{{stf.first_name}}  {{stf.last_name}} - #{{ stf.identification_no }}</option> 
                                </select>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-4">
                                <label for="">Start Date<em>*</em></label><br />
                                <input type="date" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="start_date">
                            </div>
                            <div class="basis-1/2">
                                <label for="">End Date<em></em></label><br />
                                <input type="date" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="end_date">
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-4">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" placeholder="e.g 07XXXX" v-model="phone_number">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Status<em>*</em></label><br />
                                <select name="" ref="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60"  v-model="status">
                                  <option value="" selected disabled>---Select Status</option>
                                  <option value="Active">Active</option>
                                  <option value="Inactive">Inactive</option> 
                                </select>
                            </div>
                        </div>
                        <div class="text-center" v-if="hasManager">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="replaceManager">Replace</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createManager">Save</button>
                        </div>

                    </form>
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
                </Modal>
                <!-- MODAL component for importing departments -->
                <Modal v-show="importModalVisible" @close="closeImportModal" :index="index">
                    <template v-slot:header> Import Departments </template>
                    <template v-slot:body>
                    
                    <form action="" @submit.prevent="importDepartmentsExcel" enctype="multipart/form-data" class="import-form">
                        <div class="border-2 rounded-lg py-4 px-3 mb-6">
                            <div class="relative border h-18 w-76 mb-6">
                                <DropZone 
                                    :maxFiles="Number(10000000000)"
                                    url=""
                                    :uploadOnDrop="false"
                                    :multipleUpload="true"
                                    :parallelUpload="3"
                                    method="POST"
                                    @addedFile="onFileAdd"
                                    :headers="{'Cache-Control': '' ,'X-Requested-With': ''}"
                                    
                                />
                            </div>
                            <div>
                                <label for="" class="mb-2 mr-3">Select Excel To Import:<em>*</em></label>
                                <input type="text" name="" class="rounded border-2 border-gray-600 text-gray-500 text-sm pl-2 mr-2 mb-4 w-72 h-8" placeholder="" v-model="filePath" >
                                <input type="file" name="file-input" @change="onFileChange" id="file-input" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel">
                                <label class="rounded-lg border bg-gray-200 p-2 cursor-pointer" for="file-input">Browse...</label>
                            </div>
                            <div class="text-center">
                                <button type="button" class="rounded border bg-green-400 w-24 py-2 px-2 text-white text-lg" @click="displayExcelData">Import</button>
                            </div>
                        </div>
                        <div class="import-table">
                            <table class="min-w-full bg-white mb-6"> 
                                <thead class="bg-gray-800 text-white">
                                    <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                        <th>#</th>
                                        <th class="text-left py-3 px-4">Code</th>
                                        <th class="text-left py-3 px-4">Name</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(det,index) in excelDepList" :key="det.department_id" class="even:bg-gray-100">
                                        <td>{{ index + 1 }}.</td>
                                        <td class="text-left py-3 px-4">{{ det.code }}</td>
                                        <td class="text-left py-3 px-4">{{ det.name }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="text-center">
                            <button type="submit" class="rounded border bg-green-400 w-24 py-2 px-2 text-white text-lg">Save</button>
                        </div>
                    </form>
                    
                    
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
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
                        
                        <tr v-for="(det,index) in depList" :key="det.department_id" class="even:bg-gray-100">
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
                                    <div class="basis-1/3" v-if="!det.manager_first_name">
                                        <button @click="showManagerModal(index)"><i class="fa fa-plus-square-o" aria-hidden="true" title="Add Manager"></i></button>
                                    </div>
                                    <div class="basis-1/3" v-else>
                                        <button @click="showReplaceManagerModal(index)"><i class="fa fa-plus-square-o" aria-hidden="true" title="Replace Manager"></i></button>
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
import SideBarHMS from '@/components/SideBarHMS.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'
import DropZone from 'dropzone-vue';


export default{
    name: 'DepartmentsView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Departments',
            isModalVisible: false,
            managerModalVisible: false,
            importModalVisible: false,
            dep_code: "",
            dep_name: "",
            department: "",
            start_date: "",
            end_date: "",
            manager: "",
            hasManager: false,
            phone_number: "",
            status: "",
            isEditing: false,
            isSearching: false,
            depID: 0,
            companyID: "",
            managerDepID: 0,
            userID: 0,
            currentPage: 1,
            depCount: 0,
            depArrLen: 0,
            depResults: [],
            newDepList: [],
            depList: [],
            excelDepList: [],
            manager_department: 0,
            manager_user: 0,
            manager_start_date: "",
            manager_phone_number: "",
            manager_status: "",
            manager_id: 0,
            manager_name: "",
            managerDetails: [],
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
            empty: "",
            excel_file: "",
            filePath: ""
        }
    },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        MyPagination,
        Loader,
        DropZone
    },
    methods:{
        onFileChange(e){
            this.excel_file = e.target.files[0];
            console.log("The target is ",e.target);
            console.log(this.excel_file)
            this.filePath = "C:\\fakepath\\"+ this.excel_file.name; 
        },
        onFileAdd(item){
            this.excel_file = item.file;
            console.log("The excel file is ",this.excel_file);
            console.log("The excel file name is ",this.excel_file.name);
            this.filePath = "C:\\fakepath\\"+ this.excel_file.name; 
            this.displayExcelData();
        },
        fetchStaff(){
        this.staffArray = [];
        let formData = {
            company: this.companyID,
            department: this.managerDepID
        }
        this.axios
        .post("api/v1/department-staff-list/", formData)
        .then((response)=>{
            for(let i=0; i<response.data.length; i++){
                if(response.data[i].profile != "Super Admin" && response.data[i].profile != "Patient"){
                    this.staffArray.push(response.data[i]);
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
            this.userID = this.staffArray[this.selectedDep].user_id;
            this.phone_number = this.staffArray[this.selectedDep].phone_number;
            let userName = this.staffArray[this.selectedDep].first_name;
        }
      },
      showModal(){
        this.scrollToTop();
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
        this.managerDepID = this.depList[selectedDepartment].department_id;
        this.managerModalVisible = !this.managerModalVisible;
        this.fetchStaff();
      },
      showReplaceManagerModal(){
        this.hasManager = true;
        this.scrollToTop();
        let selectedDepartment = arguments[0];
        this.department = this.depList[selectedDepartment].name;
        this.managerDepID = this.depList[selectedDepartment].department_id;
        this.managerModalVisible = !this.managerModalVisible;
        this.fetchStaff();
      },
      showImportModal(){
        this.showOptions = false;
        this.importModalVisible = ! this.importModalVisible;
        this.scrollToTop();
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
      closeImportModal(){
        this.importModalVisible = false;
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
                let new_dep_name = "";
                let x = this.dep_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_dep_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_dep_code = this.dep_code.toUpperCase();
                let formData = {
                    code: new_dep_code,
                    name: new_dep_name,
                    company: this.companyID
                }
            this.axios
            .post("api/v1/create-department/", formData)
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
        editDepartment(){
            this.isEditing = true;
            let selectedDepartment = arguments[0];
            this.depID = this.depList[selectedDepartment].department_id;
            
            let formData ={
                company: this.companyID,
                department: this.depID
            }
            this.axios
            .post("api/v1/fetch-departments/", formData)
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
                let new_dep_name = "";
                let x = this.dep_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_dep_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_dep_code = this.dep_code.toUpperCase();
                let formData = {
                    code: new_dep_code,
                    name: new_dep_name,
                    company: this.companyID,
                    department: this.depID
                }
                this.axios
                .put("api/v1/update-department/", formData)
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
            this.depID = this.depList[selectedItem].department_id;
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
                    let formData = {
                        company: this.companyID,
                        department: this.depID
                    }
                    this.axios
                    .post("api/v1/delete-department/", formData)
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
            
            this.searchDepartment();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchDepartment();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchDepartment();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchDepartment();
            this.scrollToTop();
        },
        searchDepartment(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                code: this.code,
                name: this.name,
                company_id: this.companyID
            }
            this.axios
            .post(`api/v1/department-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.depList = response.data.results;
                this.depResults = response.data;
                this.depArrLen = this.depList.length;
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
                console.log(error);
            })
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportDepartmentsPDF(){
            this.showLoader();
            let formData = {
                code: this.code,
                name: this.name,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-departments-pdf/", formData, { responseType: 'blob' })
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
            let formData = {
                code: this.code,
                name: this.name,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-departments-excel/", formData, { responseType: 'blob' })
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
            let formData = {
                code: this.code,
                name: this.name,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-departments-csv/", formData, { responseType: 'blob' })
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
        displayExcelData(){
            this.showLoader();
            if(this.excel_file == ""){
                this.$toast.error("No File Selected",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }else{
                let formData = new FormData()
                formData.append("departments_excel", this.excel_file) 

                this.axios
                .post("api/v1/display-import-excel/", formData)
                .then((response)=>{
                    this.excelDepList = response.data.departments;
                    console.log(this.excelDepList);
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                })
            }
            
        },
        importDepartmentsExcel(){
            this.showLoader();
            if(!this.excelDepList.length){
                this.$toast.error("Please Import Excel Template",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData()
                formData.append("departments_excel", this.excel_file)
                formData.append("company_id", this.companyID)

                this.axios
                .post("api/v1/import-departments-excel/", formData)
                .then((response)=>{
                   this.$toast.success("Departments Imported Succesfully",{
                        duration: 3000,
                        dismissible: true
                   })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.excelDepList = [];
                    this.excel_file = "";
                    this.$router.push("/hms/departments")
                    this.$store.commit('reloadingPage')
                })
            }
                
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
                    company: this.companyID,
                    department: this.managerDepID,
                    user: this.userID,
                    start_date: this.start_date,
                    phone_number: this.phone_number,
                    status: this.status,
                }
                console.log(formData);
                this.axios
                .post("api/v1/create-department-manager/", formData)
                .then((response)=>{
                    this.managerDetails = response.data;
                    this.$toast.success("Manager Added Succesfully",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    this.$toast.error("Operation Failed",{
                        duration: 3000,
                        dismissible: true
                    })
                    console.log(error.message);
                })
                .finally(()=>{
                    let formData = {
                        company: this.companyID,
                        staff: this.managerDetails.user,
                        department: this.managerDetails.department
                    }
                    this.axios
                    .post("api/v1/department-staff-list/", formData)
                    .then((response)=>{
                        this.manager_name = response.data.first_name + " " + response.data.last_name;
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        let formData = {
                            manager: this.managerDetails.manager_id,
                            user: this.managerDetails.user,
                            start_date: this.managerDetails.start_date,
                            phone_number: this.managerDetails.phone_number,
                            department: this.managerDetails.department,
                            status: this.managerDetails.status,
                            company: this.companyID,
                            manager_name: this.manager_name
                        }
                        this.axios
                        .put("api/v1/update-department-manager/", formData)
                        .then((response)=>{

                        })
                        .catch((error)=>{
                            console.log(error.mesage);
                        })
                        .finally(()=>{
                            this.department = "";
                            this.user = "";
                            this.start_date = "";
                            this.end_date = "";
                            this.status = "";
                            this.phone_number = "";
                            this.hideLoader();
                            this.closeManagerModal();
                            this.$store.commit('reloadingPage');
                        })
                    })  
                })
            }
        },
        replaceManager(){

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
                    company: this.companyID,
                    department: this.managerDepID,
                    user: this.userID,
                    start_date: this.start_date,
                    phone_number: this.phone_number,
                    status: this.status,
                }
                this.axios
                .post("api/v1/create-department-manager/", formData)
                .then((response)=>{
                    this.managerDetails = response.data;
                    this.$toast.success("Manager Added Succesfully",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    let formData = {
                        company: this.companyID,
                        staff: this.managerDetails.user,
                        department: this.managerDetails.department
                    }
                    this.axios
                    .post("api/v1/department-staff-list/", formData)
                    .then((response)=>{
                        this.manager_name = response.data.first_name + " " + response.data.last_name;
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        let formData = {
                            manager: this.managerDetails.manager_id,
                            user: this.managerDetails.user,
                            start_date: this.managerDetails.start_date,
                            phone_number: this.managerDetails.phone_number,
                            department: this.managerDetails.department,
                            status: this.managerDetails.status,
                            company: this.companyID,
                            manager_name: this.manager_name
                        }
                        this.axios
                        .put("api/v1/update-department-manager/", formData)
                        .then((response)=>{

                        })
                        .catch((error)=>{
                            console.log(error.mesage);
                        })
                        .finally(()=>{
                            let formData = {
                                company: this.companyID,
                                department: this.managerDetails.department
                            }
                            this.axios
                            .post("api/v1/get-department-managers/", formData)
                            .then((response)=>{
                                this.managerArr = response.data;
                            })
                            .catch((error)=>{
                                console.log(error.message);
                            })
                            .finally(()=>{
                                this.manager_status= "Inactive";
                                this.manager_department = this.managerArr[1].department;
                                this.manager_user = this.managerArr[1].user;
                                this.manager_phone_number = this.managerArr[1].phone_number;
                                this.manager_start_date = this.managerArr[1].start_date;
                                this.manager_id = this.managerArr[1].manager_id;

                                let formData = {
                                    company: this.companyID,
                                    department: this.manager_department,
                                    user: this.manager_user,
                                    start_date: this.manager_start_date,
                                    phone_number: this.manager_phone_number,
                                    end_date: this.start_date,
                                    status: this.manager_status,
                                    manager: this.manager_id
                                }
                                this.axios
                                .put("api/v1/replace-manager/", formData)
                                .then((response)=>{
                                })
                                .catch((error)=>{
                                    console.log(error.message);
                                })
                                .finally(()=>{
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
                                    this.hasManager = false;
                                    this.hideLoader();
                                    this.closeManagerModal();
                                    this.$store.commit('reloadingPage');
                                })
                            })
                        })
                    })
                    
                })
            }
        },
        
    },
    mounted(){
        this.companyID = localStorage.getItem("company_id")
        this.searchDepartment();
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
.import-table{
    min-height: 80vh;
    max-height: 100vh;
    overflow-y: scroll;
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
#file-input{
    display: none;
}
.import-form{
    min-width: 50vw;
}
</style>