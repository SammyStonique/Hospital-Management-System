<template>
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content grid grid-rows-12 bg-gray-100 px-4 py-4">
        <div class="subsection row-span-2 rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Departments</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="mb-4 flex">
                    <div class="basis-1/4 pl-3">
                        <button class="rounded-lg bg-green-500 text-white p-3" @click="showModal">+ New Department</button>
                    </div>
                    <div class="basis-1/4 pl-3">
                       <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="code" id="" placeholder="Code" v-model="code">
                    </div>
                    <div class="basis-1/4 pl-3">
                       <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name" v-model="name">
                    </div>
                    <div class="basis-1/4 pl-3">
                        <button class="rounded-lg bg-green-500 text-white px-3 py-2" @click="searchDepartment">Search</button>
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
                            <td></td>
                            <td></td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editDepartment(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/3">
                                        <button><i class="fa fa-plus-square-o" aria-hidden="true" title="Add Manager"></i></button>
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

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'


export default{
    name: 'DepartmentsView',
    props:['scrollToTop',],
    data(){
        return{
            title: 'Departments',
            isModalVisible: false,
            dep_code: "",
            dep_name: "",
            start_date: "",
            isEditing: false,
            depID: "",
            currentPage: 1,
            depCount: 0,
            depArrLen: 0,
            depResults: [],
            depList: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            code: '',
            name: ''
        }
    },
    components: {
        NavBar,
        SideBar,
        Modal,
        MyPagination
    },
    methods:{
      showModal(){
        this.isModalVisible = !this.isModalVisible;
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
        this.dep_code = "";
        this.dep_name = "";
      },
      createDepartment(){
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
                console.log(error.message);
            })
            .finally(()=>{

            })
        },
        editDepartment(){
            this.isEditing = true;
            let selectedDepartment = arguments[0];
            this.depID = this.depList[selectedDepartment].id;
            console.log("The depID is ", this.depID);
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
            if(this.dep_code === "" || this.dep_name === ""){
                this.$toast.error("Please Enter Department Details",{
                    duration:5000,
                    dismissible: true
                })
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
                console.log("Current Page ",this.currentPage," is equal to ", this.pageCount);
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
                console.log("Current page plus 1 ",this.currentPage,"pageCount ",this.pageCount);
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
                console.log("The depList is ", this.depList);
                this.depArrLen = response.data.departments.length;
                // this.fetchDepartments();
            })
            .catch((error)=>{
                console.log(error);
            })
        }
    },
    mounted(){
        this.fetchDepartments();
    }
}
</script>

<style scoped>
.main-content{
  z-index: -1;
  margin-left: 338px;
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
</style>