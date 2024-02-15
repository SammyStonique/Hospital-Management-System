<template>
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content bg-gray-100 px-4 py-4">
        <div class="rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Departments</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="mb-4">
                    <button class="rounded-lg bg-green-500 text-white p-3" @click="showModal">+ New Department</button>
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
                <div class="shadow overflow-hidden rounded border-b border-gray-200">
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
                        
                        <tr v-for="(det,index) in pageOfDepartments" :key="det.id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ det.code }}</td>
                            <td class="text-left py-3 px-4">{{ det.name }}</td>
                            <td></td>
                            <td></td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editDepartment(det.id)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
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
                <Pagination :items="exampleItems" @changePage="onChangePage" :pageSize="10" />
            </div>
        </div>
    </div>
</template>

<script>
// import swal from "sweetalert2";
import axios from "axios"
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'
import Pagination from '@/components/Pagination.vue'

export default{
    name: 'DepartmentsView',
    props:['scrollToTop','depList','fetchDepartments'],
    data(){
        return{
            title: 'Departments',
            isModalVisible: false,
            dep_code: "",
            dep_name: "",
            start_date: "",
            // depList: [],
            isEditing: false,
            depID: "",
            exampleItems: [],
            pageOfDepartments: [],
        }
    },
    components: {
        NavBar,
        SideBar,
        Modal,
        Pagination
    },
    methods:{
        onChangePage(pageOfDepartments) {
            // update page of items
            this.pageOfDepartments = pageOfDepartments;
        },
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
      fetchDepartment(){
            this.axios
            .get("api/v1/department-list/")
            .then((response)=>{
                this.depList = response.data;
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
            console.log("SelectedDep is ",selectedDepartment);
            this.depID = this.depList[selectedDepartment-1].id;
            console.log("The depID is ",this.depID);
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
            console.log("The selected item is ",selectedItem);
            this.depID = this.depList[selectedItem].id;
            console.log("The depID to be removed is ",this.depID);
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.pageOfDepartments[selectedItem].name}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                this.axios
                .delete("api/v1/department-details/"+this.pageOfDepartments[selectedItem].id+"/")
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
                    this.$swal(`${this.pageOfDepartments[selectedItem].name} has not been deleted!`);
                }
            });
        },
    },
    mounted(){
        this.fetchDepartments();
        this.exampleItems = this.depList;
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
em{
  color: red;
}
</style>