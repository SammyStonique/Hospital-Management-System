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
            <h2 class="text-center font-bold">Managers</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showManagerModal"><i class="fa fa-plus" aria-hidden="true"></i> New Manager</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="name" id="" placeholder="Name..." v-model="manager_name" @keyup.enter="searchManager">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="department" id="" placeholder="Department..." v-model="department"  @keyup.enter="searchManager">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="phone_number" id="" placeholder="Phone Number..." v-model="phone_number"  @keyup.enter="searchManager">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-2 pt-2 w-52" placeholder="Status...." v-model="status">
                                        <option value="" selected disabled  class="status-placeholder">Status</option>
                                        <option value="True">Active</option>
                                        <option value="False">Inactive</option>
                                    </select>
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Start Date From...." v-model="start_date_from" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Start Date To...." v-model="start_date_to" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchManager"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportManagersPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportManagersExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportManagersCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new manager -->
                <Modal v-show="managerModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Manager Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-4">
                                <label for="">Department<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" placeholder="Department" v-model="department">
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
                        <div class="text-center">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createManager">Save</button>
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
                                <th class="text-left py-3 px-4">Name</th>
                                <th class="text-left py-3 px-4">Department</th>
                                <th class="text-left py-3 px-4">Start Date</th>
                                <th class="text-left py-3 px-4">End Date</th>
                                <th class="text-left py-3 px-4">Phone Number</th>
                                <th class="text-left py-3 px-4">Status</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(mgr,index) in managerList" :key="mgr.manager_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ mgr.manager_name }}</td>
                            <td class="text-left py-3 px-4">{{ mgr.department }}</td>
                            <td class="text-left py-3 px-4">{{ mgr.start_date }}</td>
                            <td class="text-left py-3 px-4">{{ mgr.end_date }}</td>
                            <td class="text-left py-3 px-4">{{ mgr.phone_number }}</td>
                            <td class="text-left py-3 px-4">{{ mgr.status }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editManager(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeManager(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="managerCount"
                    :currentPage="currentPage"
                    :result="managerArrLen"
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
import Datepicker from 'vuejs3-datepicker';


export default{
    name: 'ManagerView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Managers',
            companyID: "",
            department: "",
            start_date: "",
            start_date_from: null,
            start_date_to: null,
            end_date: "",
            status: "",
            phone_number: "",
            manager_name: "",
            managerModalVisible: false,
            isEditing: false,
            isSearching: false,
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            showOptions: false,
            currentPage: 1,
            pageCount: 0,
            managerList: [],
            managerResults: [],
            managerArrLen: [],
            managerCount: 0,
            clearButton: true
        }
    },
    components:{
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker
    },
    methods:{
        searchManager(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('department', this.department);
            formData.append('start_date', this.start_date);
            if((this.start_date_from !=null) && (typeof(this.start_date_from) == "object")){
                formData.append('start_date_from', this.start_date_from.toDateString().slice(4));
            }else{
                this.start_date_from = "";
                formData.append('start_date_from', this.start_date_from);
            }   
            if((this.start_date_to !=null) && (typeof(this.start_date_to) == "object")){
                formData.append('start_date_to', this.start_date_to.toDateString().slice(4));
            }else{
                this.start_date_to = "";
                formData.append('start_date_to', this.start_date_to);
            } 
            formData.append('end_date', this.end_date);
            formData.append('status', this.status);
            formData.append('phone_number', this.phone_number);
            formData.append('manager_name', this.manager_name);
            formData.append('company_id', this.companyID);                 

            this.axios
            .post(`api/v1/managers-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.managerList = response.data.results;
                this.managerResults = response.data;
                this.managerArrLen = this.managerList.length;
                this.managerCount = this.managerResults.count;
                this.pageCount = Math.ceil(this.managerCount / 10);

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
        showManagerModal(){
            this.scrollToTop();
            if(this.isEditing == false){
                this.department = "";
                this.start_date = "";
                this.end_date = "";
                this.status = "";
                this.phone_number = "";
            }
            this.managerModalVisible = !this.managerModalVisible;
        },
        closeModal(){
            this.managerModalVisible = false;
            this.isEditing = false;
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchManager();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchManager();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchManager();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchManager();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportManagersPDF(){
            this.showLoader();
            let formData = new FormData();
            formData.append('department', this.department);
            formData.append('start_date', this.start_date);
            if((this.start_date_from !=null) && (typeof(this.start_date_from) == "object")){
                formData.append('start_date_from', this.start_date_from.toDateString().slice(4));
            }else{
                this.start_date_from = "";
                formData.append('start_date_from', this.start_date_from);
            }   
            if((this.start_date_to !=null) && (typeof(this.start_date_to) == "object")){
                formData.append('start_date_to', this.start_date_to.toDateString().slice(4));
            }else{
                this.start_date_to = "";
                formData.append('start_date_to', this.start_date_to);
            } 
            formData.append('end_date', this.end_date);
            formData.append('status', this.status);
            formData.append('phone_number', this.phone_number);
            formData.append('manager_name', this.manager_name);
            formData.append('company_id', this.companyID); 

            this.axios
            .post("api/v1/export-managers-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Managers.pdf');
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
        exportManagersExcel(){
            this.showLoader();
            let formData = new FormData();
            formData.append('department', this.department);
            formData.append('start_date', this.start_date);
            if((this.start_date_from !=null) && (typeof(this.start_date_from) == "object")){
                formData.append('start_date_from', this.start_date_from.toDateString().slice(4));
            }else{
                this.start_date_from = "";
                formData.append('start_date_from', this.start_date_from);
            }   
            if((this.start_date_to !=null) && (typeof(this.start_date_to) == "object")){
                formData.append('start_date_to', this.start_date_to.toDateString().slice(4));
            }else{
                this.start_date_to = "";
                formData.append('start_date_to', this.start_date_to);
            } 
            formData.append('end_date', this.end_date);
            formData.append('status', this.status);
            formData.append('phone_number', this.phone_number);
            formData.append('manager_name', this.manager_name);
            formData.append('company_id', this.companyID); 
            this.axios
            .post("api/v1/export-managers-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Managers.xls');
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
        exportManagersCSV(){
            this.showLoader();
            let formData = new FormData();
            formData.append('department', this.department);
            formData.append('start_date', this.start_date);
            if((this.start_date_from !=null) && (typeof(this.start_date_from) == "object")){
                formData.append('start_date_from', this.start_date_from.toDateString().slice(4));
            }else{
                this.start_date_from = "";
                formData.append('start_date_from', this.start_date_from);
            }   
            if((this.start_date_to !=null) && (typeof(this.start_date_to) == "object")){
                formData.append('start_date_to', this.start_date_to.toDateString().slice(4));
            }else{
                this.start_date_to = "";
                formData.append('start_date_to', this.start_date_to);
            } 
            formData.append('end_date', this.end_date);
            formData.append('status', this.status);
            formData.append('phone_number', this.phone_number);
            formData.append('manager_name', this.manager_name);
            formData.append('company_id', this.companyID); 
            this.axios
            .post("api/v1/export-managers-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Managers.csv');
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
        this.searchManager();
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
em{
  color: red;
}
.vuejs3-datepicker__value{
    padding: 4px 4px !important;
    min-width: 210px;
    border-color: gray;
}

.vuejs3-datepicker__calendar header .up:not(.disabled){
    background-color: #1f2937;
    color: white;
}
.vuejs3-datepicker__calendar header .up:not(.disabled):hover{
    background-color: #1f2937;
    color: white;
    opacity: 75%;
}
.vuejs3-datepicker__calendar-topbar{
    background-color: #1f2937;
}
.vuejs3-datepicker__calendar .cell.selected{
    background-color: #1f2937;
}
.vuejs3-datepicker__calendar .cell:hover{
    border-color: #1f2937;
}
.vuejs3-datepicker__clear-button{
    padding-bottom: 10px;
    font-size: 28px;
    top: -8px;
}
</style>