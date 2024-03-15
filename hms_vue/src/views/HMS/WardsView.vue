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
            <h2 class="text-center font-bold">Wards</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/4 pl-3">
                            <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Ward</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex items-end mb-3">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="code" id="" placeholder="Code..." v-model="ward_code_search" @keyup.enter="searchWards">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name..." v-model="ward_name_search"  @keyup.enter="searchWards">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="wing" id="" placeholder="Wing..." v-model="wing_search"  @keyup.enter="searchWards">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-3 pt-2 w-60" placeholder="Category...." v-model="category_search">
                                        <option value="" selected disabled  class="status-placeholder">Category</option>
                                        <option value="Children">Children</option>
                                        <option value="Women">Women</option>
                                        <option value="Men">Men</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchWards"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportWardsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportWardsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportWardsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                                <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new ward -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Ward Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Ward ID<em>*</em></label>
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="ward_code">
                        </div>
                        <div class="basis-1/2">
                            <label for="">Ward Name<em>*</em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="ward_name">
                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Category<em>*</em></label><br />
                                <select name="" ref="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60"  v-model="category">
                                  <option value="" selected disabled>---Select Category</option>
                                  <option value="Children">Children</option>
                                  <option value="Women">Women</option> 
                                  <option value="Men">Men</option> 
                                </select>
                        </div>
                        <div class="basis-1/2">
                            <label for="">Wing<em></em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="wing">
                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateWard(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createWard">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>

                <!-- MODAL component for importing wards -->
                <Modal v-show="importModalVisible" @close="closeImportModal" :index="index">
                    <template v-slot:header> Import Wards </template>
                    <template v-slot:body>
                    
                    <form action="" @submit.prevent="importWardsExcel" enctype="multipart/form-data" class="import-form">
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
                                        <th class="text-left py-3 px-4">Wing</th>
                                        <th class="text-left py-3 px-4">Category</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(wrd,index) in excelWardList" :key="wrd.ward_id" class="even:bg-gray-100">
                                        <td>{{ index + 1 }}.</td>
                                        <td class="text-left py-3 px-4">{{ wrd.ward_code_code }}</td>
                                        <td class="text-left py-3 px-4">{{ wrd.ward_name }}</td>
                                        <td class="text-left py-3 px-4">{{ wrd.wing }}</td>
                                        <td class="text-left py-3 px-4">{{ wrd.category }}</td>
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
                                <th class="text-left py-3 px-4">Wing</th>
                                <th class="text-left py-3 px-4">Category</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(wrd,index) in wardsList" :key="wrd.ward_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ wrd.ward_code }}</td>
                            <td class="text-left py-3 px-4">{{ wrd.ward_name }}</td>
                            <td class="text-left py-3 px-4">{{ wrd.wing }}</td>
                            <td class="text-left py-3 px-4">{{ wrd.category }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editWard(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    
                                    <div class="basis-1/3">
                                        <button @click="removeWard(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="wardCount"
                    :currentPage="currentPage"
                    :result="wardArrLen"
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
    name: 'WardsView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Wards',
            isModalVisible: false,
            importModalVisible: false,
            ward_code: "",
            ward_name: "",
            category: "",
            wing: "",
            isEditing: false,
            isSearching: false,
            wardID: "",
            wardName: "",
            hospitalID: "",
            currentPage: 1,
            wardCount: 0,
            wardArrLen: 0,
            wardResults: [],
            wardsList: [],
            excelWardList: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            ward_code_search: '',
            ward_name_search: '',
            category_search: "",
            wing_search: "",
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
      showModal(){
        this.scrollToTop();
        if(this.isEditing == false){
          this.ward_code = "";
          this.ward_name = "";
          this.category = "";
          this.wing = "";
        }
        this.isModalVisible = !this.isModalVisible;
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
      createWard(){
            this.showLoader();
            if(this.ward_code === '' || this.ward_name === '' || this.category === ''){
                this.$toast.error("Please Enter Ward Details",{
                    duration: 3000,
                    dismissible: true
                })
            }
            else{
                let new_ward_name = "";
                let x = this.ward_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_ward_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_wing = "";
                if(this.wing){
                    let y = this.wing.split(" ");
                    for(let i=0; i<y.length; i++){
                        new_wing += y[i][0].toUpperCase()+ y[i].slice(1).toLowerCase() + " ";
                    }
                }
                else{
                    new_wing = "";
                }
                let new_ward_code = this.ward_code.toUpperCase();
                
                let formData = {
                    ward_code: new_ward_code,
                    ward_name: new_ward_name,
                    category: this.category,
                    wing: new_wing,
                    hospital: this.hospitalID
                }
                this.axios
                .post("api/v1/create-ward/", formData)
                .then((response)=>{
                    this.$toast.success("Ward Successfully Added",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.ward_code = "";
                    this.ward_name = "";
                    this.category = "";
                    this.wing = "";

                })
            }
        },
        editWard(){
            this.isEditing = true;
            let selectedWard= arguments[0];
            this.wardID = this.wardsList[selectedWard].ward_id;
            this.ward_code = this.wardsList[selectedWard].ward_code;
            this.ward_name = this.wardsList[selectedWard].ward_name;
            this.category = this.wardsList[selectedWard].category;
            this.wing = this.wardsList[selectedWard].wing;
            this.showModal();

        },
        updateWard(){
            this.showLoader();
            if(this.ward_code === '' || this.ward_name === '' || this.category === ''){
                this.$toast.error("Please Enter Ward Details",{
                    duration:3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let new_ward_name = "";
                let x = this.ward_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_ward_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_wing = "";
                if(this.wing){
                    let y = this.wing.split(" ");
                    for(let i=0; i<y.length; i++){
                        new_wing += y[i][0].toUpperCase()+ y[i].slice(1).toLowerCase() + " ";
                    }
                }
                else{
                    new_wing = "";
                }
                let new_ward_code = this.ward_code.toUpperCase();

                let formData = {
                    ward: this.wardID,
                    ward_code: new_ward_code,
                    ward_name: new_ward_name,
                    category: this.category,
                    wing: new_wing,
                    hospital: this.hospitalID
                }

                this.axios
                .put("api/v1/update-ward/", formData)
                .then((response)=>{
                    this.$toast.success("Ward Succesfully Updated",{
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
        removeWard() {
            let selectedItem = arguments[0];
            this.wardID = this.wardsList[selectedItem].ward_id;
            this.wardName = this.wardsList[selectedItem].ward_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.wardName}?`,
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
                        ward: this.wardID,
                    }
                    this.axios
                    .post("api/v1/delete-ward/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Ward removed succesfully!", {
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
                    this.$swal(`${this.wardName} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchWards();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchWards();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchWards();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchWards();
            this.scrollToTop();
        },
        searchWards(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                ward_code: this.ward_code_search,
                ward_name: this.ward_name_search,
                category: this.category_search,
                wing: this.wing_search,
                hospital: this.hospitalID
            }
            this.axios
            .post(`api/v1/wards-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.wardsList = response.data.results;
                this.wardResults = response.data;
                this.wardArrLen = this.wardsList.length;
                this.wardCount = this.wardResults.count;
                this.pageCount = Math.ceil(this.wardCount / 10);

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
        exportWardsPDF(){
            this.showLoader();
            let formData = {
                ward_code: this.ward_code_search,
                ward_name: this.ward_name_search,
                category: this.category_search,
                wing: this.wing_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-wards-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Wards.pdf');
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
        exportWardsExcel(){
            this.showLoader();
            let formData = {
                ward_code: this.ward_code_search,
                ward_name: this.ward_name_search,
                category: this.category_search,
                wing: this.wing_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-wards-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Wards.xls');
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
        exportWardsCSV(){
            this.showLoader();
            let formData = {
                ward_code: this.ward_code_search,
                ward_name: this.ward_name_search,
                category: this.category_search,
                wing: this.wing_search,
                hospital: this.hospitalID
            }
            this.axios
            .post("api/v1/export-wards-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Wards.csv');
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
                formData.append("wards_excel", this.excel_file) 

                this.axios
                .post("api/v1/display-wards-import-excel/", formData)
                .then((response)=>{
                    this.excelWardList = response.data.wards;
                    console.log(this.excelWardList);
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                })
            }
            
        },
        importStaffRoomsExcel(){
            this.showLoader();
            if(!this.excelWardList.length){
                this.$toast.error("Please Import Excel Template",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData()
                formData.append("wards_excel", this.excel_file)
                formData.append("hospital", this.hospitalID)

                this.axios
                .post("api/v1/import-wards-excel/", formData)
                .then((response)=>{
                   this.$toast.success("Wards Imported Succesfully",{
                        duration: 3000,
                        dismissible: true
                   })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.excelWardList = [];
                    this.excel_file = "";
                    this.$router.push("/hms/wards")
                    this.$store.commit('reloadingPage')
                })
            }
                
        },

       
    },
    mounted(){
        this.hospitalID = localStorage.getItem("company_id")
        this.searchWards();
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