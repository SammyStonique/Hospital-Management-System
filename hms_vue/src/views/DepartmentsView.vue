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
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="dep_id">
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
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateDepartment">Update</button>
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
                                <th class="text-left py-3 px-4">ID</th>
                                <th class="text-left py-3 px-4">Name</th>
                                <th class="text-left py-3 px-4">Manager</th>
                                <th class="text-left py-3 px-4">Start Date</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(det,index) in depList" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ det.id }}</td>
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
                                        <button><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            
            </div>
        </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'
import Modal from '@/components/Modal.vue'

export default{
    name: 'DepartmentsView',
    props:['scrollToTop'],
    data(){
        return{
            title: 'Departments',
            isModalVisible: false,
            dep_id: "",
            dep_name: "",
            start_date: "",
            depList: [],
            isEditing: false,
            depID: ""
        }
    },
    components: {
        NavBar,
        SideBar,
        Modal
    },
    methods:{
      showModal(){
        this.isModalVisible = !this.isModalVisible;
      },
      closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
        this.dep_id = "";
        this.dep_name = "";
      },
      createDepartment(){
        if(this.dep_id === '' || this.dep_name === ''){
          this.$toast.error("Please Enter Department Details",{
            duration: 5000,
            dismissible: true
          })
        }
        else{
            let formData = {
                id: this.dep_id,
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
            this.dep_id = "";
            this.dep_name = "";
          })
        }
      },
      fetchDepartments(){
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
            this.depID = this.depList[selectedDepartment].id;
            this.axios
            .get(`api/v1/department-details/${this.depID}/`)
            .then((response)=>{
                this.dep_id = response.data.id;
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
            if(this.dep_id === "" || this.dep_name === ""){
                this.$toast.error("Please Enter Department Details",{
                    duration:5000,
                    dismissible: true
                })
            }
            else{
                let formData = {
                    id: this.dep_id,
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
                })
            }
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
em{
  color: red;
}
</style>