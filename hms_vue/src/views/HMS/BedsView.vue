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
            <h2 class="text-center font-bold">Beds</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/4 pl-3">
                            <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Bed</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex items-end mb-3">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="number" id="" placeholder="Number..." v-model="bed_number_search" @keyup.enter="searchBeds">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="ward" id="" placeholder="Ward..." v-model="ward_search"  @keyup.enter="searchBeds">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2 pl-3 items-center">
                                    <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-3 pt-2 w-60" placeholder="Category...." v-model="category_search">
                                        <option value="" selected disabled  class="status-placeholder">Category</option>
                                        <option value="Children">Children</option>
                                        <option value="Women">Women</option>
                                        <option value="Men">Men</option>
                                    </select>
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-3 pt-2 w-60" placeholder="Status...." v-model="status_search">
                                        <option value="" selected disabled  class="status-placeholder">Status</option>
                                        <option value="Available">Available</option>
                                        <option value="Occupied">Occupied</option>
                                        <option value="Reserved">Reserved</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchBeds"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/6 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportBedsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportBedsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportBedsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                                <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new ward -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Beds Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Bed Number<em>*</em></label>
                            <input type="number" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="bed_number">
                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2"  v-if="isEditing">
                            <label for="">Ward<em>*</em></label><br />
                            <select name="wardUpdate" ref="wardUpdateSelect" id="selectUpdateWard" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateWardID" onfocus="this.selectedIndex = -1;" v-model="wardEditing">
                                <option v-for="wrd in wardsArray" :key="wrd.ward_id" :value="(wrd.ward_code+'-'+wrd.ward_name)" :label="(wrd.ward_code+'-'+wrd.ward_name)" :selected="((wrd.ward_code+'-'+wrd.ward_name)===doctorEditing)">{{wrd.ward_code}} - {{wrd.ward_name}}</option> 
                            </select>
                        </div>
                        <div class="basis-1/2" v-else>
                            <label for="">Ward<em>*</em></label><br />
                            <select name="ward" ref="wardSelect" id="selectWard" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setWardID" onfocus="this.selectedIndex = -1;" v-model="ward">
                                <option value="" disabled selected>---Select Ward---</option> 
                                <option v-for="wrd in wardsArray">{{wrd.ward_code}} - {{wrd.ward_name}}</option> 
                            </select>
                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Price<em></em></label><br />
                            <input type="number" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="price">
                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateBed(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createBed">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>

                <!-- MODAL component for importing beds -->
                <Modal v-show="importModalVisible" @close="closeImportModal" :index="index">
                    <template v-slot:header> Import Beds </template>
                    <template v-slot:body>
                    
                    <form action="" @submit.prevent="importBedsExcel" enctype="multipart/form-data" class="import-form">
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
                                        <th class="text-left py-3 px-4">Number</th>
                                        <th class="text-left py-3 px-4">Ward</th>
                                        <th class="text-left py-3 px-4">Category</th>
                                        <th class="text-left py-3 px-4">Price</th>
                                        <th class="text-left py-3 px-4">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(bed,index) in excelBedList" :key="bed.bed_id" class="even:bg-gray-100">
                                        <td>{{ index + 1 }}.</td>
                                        <td class="text-left py-3 px-4">{{ bed.bed_number }}</td>
                                        <td class="text-left py-3 px-4">{{ bed.ward_name }}</td>
                                        <td class="text-left py-3 px-4">{{ bed.ward_category }}</td>
                                        <td class="text-left py-3 px-4">{{ bed.price }}</td>
                                        <td class="text-left py-3 px-4">{{ bed.status }}</td>
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
                                <th class="text-left py-3 px-4">Number</th>
                                <th class="text-left py-3 px-4">Ward</th>
                                <th class="text-left py-3 px-4">Patient</th>        
                                <th class="text-left py-3 px-4">Price</th>
                                <th class="text-left py-3 px-4">Status</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(bed,index) in bedsList" :key="bed.bed_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ bed.bed_number }}</td>
                            <td class="text-left py-3 px-4">{{ bed.ward_name }} - {{ bed.ward_category }}</td>
                            <td class="text-left py-3 px-4">{{ bed.patient_name }}</td>
                            <td class="text-left py-3 px-4">{{ bed.price }}</td>
                            <td class="text-left py-3 px-4">{{ bed.status }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editBed(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    
                                    <div class="basis-1/3">
                                        <button @click="removeBed(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="bedCount"
                    :currentPage="currentPage"
                    :result="bedArrLen"
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
    name: 'BedsView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Beds',
            isModalVisible: false,
            importModalVisible: false,
            bed_number: "",
            ward: "",
            price: "",
            isEditing: false,
            isSearching: false,
            bedID: "",
            bedNumber: "",
            hospitalID: "",
            wardID: "",
            wardUpdateID: "",
            wardName: "",
            wardUpdateName: "",
            currentPage: 1,
            bedCount: 0,
            bedArrLen: 0,
            bedResults: [],
            bedsList: [],
            excelBedList: [],
            wardsArray: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            bed_number_search: '',
            ward_search: '',
            status_search: "",
            category_search: "",
            price_search: "",
            showOptions: false,
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
        fetchWards(){
            this.wardsArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-wards/", formData)
            .then((response)=>{
                this.wardsArray = response.data;
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        showModal(){
            this.scrollToTop();
            if(this.isEditing == false){
            this.bed_number = "";
            this.ward = "";
            this.price = "";
            }
            this.isModalVisible = !this.isModalVisible;
            this.fetchWards();
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
        closeImportModal(){
            this.importModalVisible = false;
        },
        createBed(){
            this.showLoader();
            if(this.bed_number === '' || this.ward === '' || this.price === ''){
                this.$toast.error("Please Enter Bed Details",{
                    duration: 3000,
                    dismissible: true
                })
            }
            else{               
                let formData = {
                    bed_number: this.bed_number,
                    ward: this.wardID,
                    price: this.price,
                    patient: this.patient,
                    hospital: this.hospitalID
                }
                this.axios
                .post("api/v1/create-ward-bed/", formData)
                .then((response)=>{
                    this.$toast.success("Bed Successfully Added",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.bed_number = "";
                    this.status = "";
                    this.ward = "";
                    this.price = "";

                })
            }
        },
        editBed(){
            this.isEditing = true;
            let selectedBed = arguments[0];
            this.wardID = this.bedsList[selectedBed].ward_id;
            this.bedID = this.bedsList[selectedBed].bed_id;
            this.bed_number = this.bedsList[selectedBed].bed_number;
            this.price = this.bedsList[selectedBed].price;
            this.wardEditing = this.bedsList[selectedBed].ward_code +'-'+ this.bedsList[selectedBed].ward_name;
            this.status = this.bedsList[selectedBed].status;
            this.showModal();

        },
        updateBed(){
            this.showLoader();
            if(this.bed_number === '' || this.wardEditing === '' || this.price === ''){
                this.$toast.error("Please Enter Bed Details",{
                    duration:3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData();
                formData.append('bed', this.bedID);
                formData.append('bed_number', this.bed_number);
                formData.append('price', this.price);
                formData.append('status', this.status);
                if(this.wardUpdateID != 0){
                    formData.append('ward', this.wardUpdateID);
                }else{
                    formData.append('ward', this.wardID);
                }
                formData.append('hospital', this.hospitalID);

                this.axios
                .put("api/v1/update-ward-bed/", formData)
                .then((response)=>{
                    this.$toast.success("Bed Succesfully Updated",{
                        duration:3000,
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
        removeBed() {
            let selectedItem = arguments[0];
            this.wardID = this.bedsList[selectedItem].ward_id;
            this.bedID = this.bedsList[selectedItem].bed_id;
            this.bedNumber = this.bedsList[selectedItem].bed_number;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete Bed ${this.bedNumber}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        hospital: this.hospitalID,
                        bed: this.bedID,
                        ward: this.wardID,
                    }
                    this.axios
                    .post("api/v1/delete-ward-bed/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Bed removed succesfully!", {
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
                    this.$swal(`Bed ${this.bedNumber} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchBeds();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchBeds();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchBeds();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchBeds();
            this.scrollToTop();
        },
        searchBeds(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;

            let formData = {
                bed_number: this.bed_number_search,
                ward: this.ward_search,
                category: this.category_search,
                status: this.status_search,
                hospital: this.hospitalID
            }

            this.axios
            .post(`api/v1/beds-search/?page=${this.currentPage}`,formData)
            .then((response)=>{

                this.bedsList = response.data.results;
                this.bedResults = response.data;
                this.bedArrLen = this.bedsList.length;
                this.bedCount = this.bedResults.count;
                this.pageCount = Math.ceil(this.bedCount / 10);

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
        setWardID(){
            this.wardID = "";
            if(this.$refs.wardSelect.selectedIndex > 0){
                let selectedWard = this.$refs.wardSelect.selectedIndex - 1;
                this.wardID = this.wardsArray[selectedWard].ward_id;
                this.wardName = this.wardsArray[selectedWard].ward_name;
            }
        },
        setUpdateWardID(){
            this.wardUpdateID = "";
            if(this.$refs.wardUpdateSelect.selectedIndex >= 0){
                let selectedUpdateWard = this.$refs.wardUpdateSelect.selectedIndex;
                this.wardUpdateID = this.wardsArray[selectedUpdateWard].ward_id;
                this.wardUpdateName = this.wardsArray[selectedUpdateWard].ward_name;

            }
        },
        exportBedsPDF(){
            this.showLoader();
            let formData = {
                bed_number: this.bed_number_search,
                ward: this.ward_search,
                category: this.category_search,
                status: this.status_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-beds-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Beds.pdf');
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
        exportBedsExcel(){
            this.showLoader();
            let formData = {
                bed_number: this.bed_number_search,
                ward: this.ward_search,
                category: this.category_search,
                status: this.status_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-beds-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Beds.xls');
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
        exportBedsCSV(){
            this.showLoader();
            let formData = {
                bed_number: this.bed_number_search,
                ward: this.ward_search,
                category: this.category_search,
                status: this.status_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-beds-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Beds.csv');
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
                formData.append("beds_excel", this.excel_file) 

                this.axios
                .post("api/v1/display-beds-import-excel/", formData)
                .then((response)=>{
                    this.excelBedList = response.data.beds;
                    console.log(this.excelBedList);
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                })
            }
            
        },
        importBedsExcel(){
            this.showLoader();
            if(!this.excelBedList.length){
                this.$toast.error("Please Import Excel Template",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData()
                formData.append("beds_excel", this.excel_file)
                formData.append("hospital", this.hospitalID)

                this.axios
                .post("api/v1/import-beds-excel/", formData)
                .then((response)=>{
                   this.$toast.success("Beds Imported Succesfully",{
                        duration: 3000,
                        dismissible: true
                   })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.excelBedList = [];
                    this.excel_file = "";
                    this.$router.push("/hms/beds")
                    this.$store.commit('reloadingPage')
                })
            }
                
        },

       
    },
    mounted(){
        this.hospitalID = localStorage.getItem("company_id")
        this.searchBeds();
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