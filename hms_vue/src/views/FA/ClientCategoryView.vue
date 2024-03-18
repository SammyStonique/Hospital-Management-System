<template>
    <Loader
    :loader="loader"
    :showLoader="showLoader"
    :hideLoader="hideLoader"
    />
    <NavBar
    :title="title"
    />
    <SideBarFA />
    <div class="main-content grid grid-rows-12 bg-gray-100 px-4 py-4">
        <div class="subsection row-span-2 rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Client Categories</h2>
            <div class="md:px-4 pt-4 pb-1 w-full">
                <div class="mb-4 flex items-end h-24 border-b-2 border-gray-300 mb-6 pb-6">
                    <div class="basis-1/4 pl-3">
                        <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Category</button>
                    </div>
                    <div class="basis-3/4">
                        <div class="flex items-end">
                            <div class="basis-1/2 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name..." v-model="category_name_search"  @keyup.enter="searchClientCategory">
                            </div>
                        </div>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchClientCategory"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportClientCategoryPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportClientCategoryExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportClientCategoryCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new department -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Category Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                    <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Name<em>*</em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="category_name">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateCategory(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createCategory">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>

                <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                    <table class="min-w-full bg-white"> 
                        <thead class="bg-gray-800 text-white">
                            <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                <th>#</th>
                                <th class="text-left py-3 px-4">Name</th>
                                <th class="text-left py-3 px-4"></th>
                                <th class="text-left py-3 px-4"></th>
                                <th class="text-left py-3 px-4"></th>
                                <th class="text-left py-3 px-4"></th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(cat,index) in categoryList" :key="cat.category_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ cat.category_name }}</td>
                            <th class="text-left py-3 px-4"></th>
                            <th class="text-left py-3 px-4"></th>
                            <th class="text-left py-3 px-4"></th>
                            <th class="text-left py-3 px-4"></th>
                            <td class="text-right right-0">
                                <div class="flex">
                                    <div class="basis-1/6">
                                        <button @click="editCategory(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/6">
                                        <button @click="removeCategory(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="catCount"
                    :currentPage="currentPage"
                    :result="catArrLen"
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
import SideBarFA from '@/components/SideBarFA.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'


export default{
    name: 'ClientCategoryView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Financial Accounts/ Client Categories',
            isModalVisible: false,
            category_name: "",
            category_name_search: "",
            isEditing: false,
            isSearching: false,
            catID: "",
            catName: "",
            companyID: "",
            currentPage: 1,
            catCount: 0,
            catArrLen: 0,
            catResults: [],
            categoryList: [],
            categoryDetails: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            showOptions: false,
        }
    },
    components: {
        NavBar,
        SideBarFA,
        Modal,
        MyPagination,
        Loader,
    },

    methods:{
        
      showModal(){
        this.scrollToTop();
        if(this.isEditing == false){
          this.category_name = "";
        }
        this.isModalVisible = !this.isModalVisible;
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
      },

      createCategory(){
            this.showLoader();
            if(this.category_name === ''){
                this.$toast.error("Please Enter Category Name",{
                    duration: 3000,
                    dismissible: true
                })
            }
            else{
                let new_category_name = "";
                let x = this.category_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_category_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let formData = {
                    name: new_category_name,
                    company: this.companyID
                }
                this.axios
                .post("api/v1/create-client-category/", formData)
                .then((response)=>{
                    this.$toast.success("Category Successfully Added",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.category_name = "";
                })
            }
        },
        editCategory(){
            this.isEditing = true;
            let selectedCategory = arguments[0];
            this.catID = this.categoryList[selectedCategory].category_id;
            
            let formData ={
                company: this.companyID,
                category: this.catID
            }
            this.axios
            .post("api/v1/fetch-client-categories/", formData)
            .then((response)=>{
                this.category_name = response.data.name;
            })
            .catch((error)=>{
                console.log(error.message);
            })
            .finally(()=>{
                this.scrollToTop();
                this.showModal();

            })

        },
        updateCategory(){
            this.showLoader();
            if(this.category_name === ""){
                this.$toast.error("Please Enter Category Name",{
                    duration:3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let new_category_name = "";
                let x = this.category_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_category_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let formData = {
                    category: this.catID,
                    name: new_category_name,
                    company: this.companyID,
                }
                this.axios
                .put("api/v1/update-client-category/", formData)
                .then((response)=>{
                    this.$toast.success("Category Succesfully Updated",{
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
        removeCategory() {
            let selectedItem = arguments[0];
            this.catID = this.categoryList[selectedItem].category_id;
            this.catName = this.categoryList[selectedItem].category_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.catName}?`,
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
                        category: this.catID
                    }
                    this.axios
                    .post("api/v1/delete-client-category/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Category removed succesfully!", {
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
                    this.$swal(`${this.catName} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchClientCategory();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchClientCategory();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchClientCategory();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchClientCategory();
            this.scrollToTop();
        },
        searchClientCategory(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                category_name: this.category_name_search,
                company_id: this.companyID
            }
            this.axios
            .post(`api/v1/client-category-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.categoryList = response.data.results;
                this.catResults = response.data;
                this.catArrLen = this.categoryList.length;
                this.catCount = this.catResults.count;
                this.pageCount = Math.ceil(this.catCount / 10);

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
        exportClientCategoryPDF(){
            this.showLoader();
            let formData = {
                category_name: this.category_name_search,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-client-categories-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Client Categories.pdf');
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
        exportClientCategoryExcel(){
            this.showLoader();
            let formData = {
                category_name: this.category_name_search,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-client-categories-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Client Categories.xls');
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
        exportClientCategoryCSV(){
            this.showLoader();
            let formData = {
                category_name: this.category_name_search,
                company_id: this.companyID
            }
            this.axios
            .post("api/v1/export-client-categories-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Client Categories.csv');
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
        this.searchClientCategory();
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