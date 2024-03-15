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
            <h2 class="text-center font-bold">Staff Rooms</h2>
            <div class="md:px-4 pt-4 pb-1 w-full">
                <div class="mb-4 flex items-end h-24 border-b-2 border-gray-300 mb-6 pb-6">
                    <div class="basis-1/6 pl-3">
                        <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Room</button>
                    </div>
                    <div class="basis-3/4">
                        <div class="flex items-end">
                            <div class="basis-1/3 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="code" id="" placeholder="Code..." v-model="room_code_search" @keyup.enter="searchStaffRooms">
                            </div>
                            <div class="basis-1/3 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="name" id="" placeholder="Name..." v-model="room_name_search"  @keyup.enter="searchStaffRooms">
                            </div>
                            <div class="basis-1/3 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="department" id="" placeholder="Department..." v-model="room_department_search"  @keyup.enter="searchStaffRooms">
                            </div>
                        </div>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchStaffRooms"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportStaffRoomsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportStaffRoomsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportStaffRoomsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new staff room -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Staff Room Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Staff Room ID<em>*</em></label>
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="room_code">
                        </div>
                        <div class="basis-1/2">
                            <label for="">Staff Room Name<em>*</em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="room_name">
                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2">
                            <label for="">Department<em>*</em></label><br />
                            <select name="departmentUpdate" ref="departmentUpdateSelect" id="selectUpdateDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateDepartmentID" onfocus="this.selectedIndex = -1;" v-model="departmentEditing" v-if="isEditing">
                                <option v-for="dep in departmentsArray" :key="dep.department_id" :value="dep.name" :label="dep.name" :selected="dep.name===departmentEditing">({{dep.code}}) - {{ dep.name }}</option> 
                            </select>
                            <select name="department" ref="departmentSelect" id="selectDepartment" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setDepartmentID" onfocus="this.selectedIndex = -1;" v-model="department" required v-else>
                                    <option value="" disabled selected>--Select Department--</option>
                                    <option v-for="dep in departmentsArray" >({{dep.code}}) - {{ dep.name }}</option> 
                                </select>
                        </div>
                        <div class="basis-1/2">
                            <label for="">Staff<em></em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="staff">
                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateStaffRoom(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createStaffRoom">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>

                <!-- MODAL component for importing staff rooms -->
                <Modal v-show="importModalVisible" @close="closeImportModal" :index="index">
                    <template v-slot:header> Import Staff Rooms </template>
                    <template v-slot:body>
                    
                    <form action="" @submit.prevent="importStaffRoomsExcel" enctype="multipart/form-data" class="import-form">
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
                                        <th class="text-left py-3 px-4">Department</th>
                                        <th class="text-left py-3 px-4">Staff</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(rom,index) in excelRoomList" :key="rom.room_id" class="even:bg-gray-100">
                                        <td>{{ index + 1 }}.</td>
                                        <td class="text-left py-3 px-4">{{ rom.room_code }}</td>
                                        <td class="text-left py-3 px-4">{{ rom.room_name }}</td>
                                        <td class="text-left py-3 px-4">{{ rom.department }}</td>
                                        <td class="text-left py-3 px-4">{{ rom.staff }}</td>
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
                                <th class="text-left py-3 px-4">Departent</th>
                                <th class="text-left py-3 px-4">Staff</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(rom,index) in roomsList" :key="rom.room_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ rom.room_code }}</td>
                            <td class="text-left py-3 px-4">{{ rom.room_name }}</td>
                            <td class="text-left py-3 px-4">{{ rom.department_name }}</td>
                            <td class="text-left py-3 px-4">{{ rom.staff_name }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editStaffRoom(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    
                                    <div class="basis-1/3">
                                        <button @click="removeStaffRoom(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="roomCount"
                    :currentPage="currentPage"
                    :result="roomArrLen"
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
import DropZone from 'dropzone-vue';


export default{
    name: 'DepartmentsView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Staff Room',
            isModalVisible: false,
            importModalVisible: false,
            room_code: "",
            room_name: "",
            department: "",
            staff: "",
            staffName: "",
            hasStaff: false,
            isEditing: false,
            isSearching: false,
            departmentEditing: "",
            roomID: "",
            roomName: "",
            depID: "",
            depUpdateID: "",
            depUpdateName: "",
            companyID: "",
            userID: "",
            currentPage: 1,
            roomCount: 0,
            roomArrLen: 0,
            roomResults: [],
            newRoomList: [],
            roomsList: [],
            excelRoomList: [],
            staffDetails: [],
            staffList: [],
            staffArr: [],
            newStaffArr: [],
            departmentsArray: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            room_code_search: '',
            room_name_search: '',
            room_department_search: "",
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
        Datepicker,
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
        fetchDepartments(){
            this.axios
            .get("api/v1/department-list/")
            .then((response)=>{
                this.departmentsArray = response.data.results;
            })
            .catch((error)=>{
                console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        fetchStaff(){
            this.staffList = [];
            let formData = {
                company: this.companyID,
                department: this.managerDepID
            }
            this.axios
            .post("api/v1/department-staff-list/", formData)
            .then((response)=>{
                for(let i=0; i<response.data.length; i++){
                    if(response.data[i].profile != "Super Admin" && response.data[i].profile != "Patient"){
                        this.staffList.push(response.data[i]);
                    }
                }
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        setDepartmentID(){
            this.depID = 0;
            if(this.$refs.departmentSelect.selectedIndex > 0){
                let selectedDep = this.$refs.departmentSelect.selectedIndex - 1;
                this.depID = this.departmentsArray[selectedDep].department_id;
            }
        },
        setUpdateDepartmentID(){
            this.depUpdateID = 0;
            if(this.$refs.departmentUpdateSelect.selectedIndex >= 0){
                let selectedUpdateDep = this.$refs.departmentUpdateSelect.selectedIndex;
                this.depUpdateID = this.departmentsArray[selectedUpdateDep].department_id;
                this.depUpdateName = this.departmentsArray[selectedUpdateDep].name;
                console.log("The dep Id is ",this.depUpdateID);
                console.log("The dep name is ",this.depUpdateName);
            }

        },
        setUserID(){
            this.userID = "";
            if(this.$refs.userSelect.selectedIndex > 0){
                let selectedStaff = this.$refs.userSelect.selectedIndex - 1;
                this.userID = this.staffArray[selectedStaff].user_id;
                this.phone_number = this.staffArray[selectedStaff].phone_number;
                this.staffName = this.staffArray[selectedStaff].first_name + " "+ this.staffArray[selectedStaff].last_name ;
            }
        },
      showModal(){
        this.scrollToTop();
        if(this.isEditing == false){
          this.room_code = "";
          this.room_name = "";
          this.staff = "";
          this.department = "";
        }
        this.isModalVisible = !this.isModalVisible;
        this.fetchDepartments();
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
      createStaffRoom(){
            this.showLoader();
            if(this.room_code === '' || this.room_name === '' || this.department === ''){
                this.$toast.error("Please Enter Staff Room Details",{
                    duration: 3000,
                    dismissible: true
                })
            }
            else{
                let new_room_name = "";
                let x = this.room_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_room_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_staff = "";
                if(this.staff){
                    let y = this.staff.split(" ");
                    for(let i=0; i<y.length; i++){
                        new_staff += y[i][0].toUpperCase()+ y[i].slice(1).toLowerCase() + " ";
                    }
                }
                else{
                    new_staff = "";
                }
                let new_room_code = this.room_code.toUpperCase();
                
                let formData = {
                    room_code: new_room_code,
                    room_name: new_room_name,
                    department: this.depID,
                    staff: new_staff,
                    company: this.companyID
                }
                this.axios
                .post("api/v1/create-department-room/", formData)
                .then((response)=>{
                    this.$toast.success("Staff Room Successfully Added",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.room_code = "";
                    this.room_name = "";
                    this.department = "";
                })
            }
        },
        editStaffRoom(){
            this.isEditing = true;
            let selectedRoom = arguments[0];
            this.roomID = this.roomsList[selectedRoom].room_id;
            this.depID = this.roomsList[selectedRoom].department_id;
            this.room_code = this.roomsList[selectedRoom].room_code;
            this.room_name = this.roomsList[selectedRoom].room_name;
            this.staff = this.roomsList[selectedRoom].staff_name;
            this.departmentEditing = this.roomsList[selectedRoom].department_name;
            this.showModal();

        },
        updateStaffRoom(){
            this.showLoader();
            if(this.room_code === "" || this.room_name === "" || this.departmentEditing ===""){
                this.$toast.error("Please Enter Room Details",{
                    duration:3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let new_room_name = "";
                let x = this.room_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_room_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let new_staff = "";
                if(this.staff){
                    let y = this.staff.split(" ");
                    for(let i=0; i<y.length; i++){
                        new_staff += y[i][0].toUpperCase()+ y[i].slice(1).toLowerCase() + " ";
                    }
                }
                else{
                    new_staff = "";
                }
                
                let new_room_code = this.room_code.toUpperCase();

                let formData = new FormData();
                formData.append('room', this.roomID);
                formData.append('room_code', new_room_code);
                formData.append('room_name', new_room_name);
                if(new_staff){
                    formData.append('staff', new_staff);
                }
                formData.append('company', this.companyID);
                if(this.depUpdateID != 0){
                    formData.append('department', this.depUpdateID);
                }else{
                    formData.append('department', this.depID);
                }
                console.log(formData);

                this.axios
                .put("api/v1/update-department-room/", formData)
                .then((response)=>{
                    this.$toast.success("Room Succesfully Updated",{
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
        removeStaffRoom() {
            let selectedItem = arguments[0];
            this.roomID = this.roomsList[selectedItem].room_id;
            this.depID = this.roomsList[selectedItem].department_id;
            this.roomName = this.roomsList[selectedItem].room_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.roomName}?`,
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
                        room: this.roomID,
                        department: this.depID
                    }
                    this.axios
                    .post("api/v1/delete-room/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Room removed succesfully!", {
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
                    this.$swal(`${this.roomName} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchStaffRooms();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchStaffRooms();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchStaffRooms();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchStaffRooms();
            this.scrollToTop();
        },
        searchStaffRooms(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                room_code: this.room_code_search,
                room_name: this.room_name_search,
                department: this.room_department_search,
                company: this.companyID
            }
            this.axios
            .post(`api/v1/rooms-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.roomsList = response.data.results;
                this.roomResults = response.data;
                this.roomArrLen = this.roomsList.length;
                this.roomCount = this.roomResults.count;
                this.pageCount = Math.ceil(this.roomCount / 10);

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
        exportStaffRoomsPDF(){
            this.showLoader();
            let formData = {
                room_code: this.room_code_search,
                room_name: this.room_name_search,
                department: this.room_department_search,
                company: this.companyID
            }
            this.axios
            .post("api/v1/export-rooms-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff Rooms.pdf');
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
        exportStaffRoomsExcel(){
            this.showLoader();
            let formData = {
                room_code: this.room_code_search,
                room_name: this.room_name_search,
                department: this.room_department_search,
                company: this.companyID
            }
            this.axios
            .post("api/v1/export-rooms-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff Rooms.xls');
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
        exportStaffRoomsCSV(){
            this.showLoader();
            let formData = {
                room_code: this.room_code_search,
                room_name: this.room_name_search,
                department: this.room_department_search,
                company: this.companyID
            }
            this.axios
            .post("api/v1/export-rooms-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Staff Rooms.csv');
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
                formData.append("rooms_excel", this.excel_file) 

                this.axios
                .post("api/v1/display-rooms-import-excel/", formData)
                .then((response)=>{
                    this.excelRoomList = response.data.rooms;
                    console.log(this.excelRoomList);
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
            if(!this.excelRoomList.length){
                this.$toast.error("Please Import Excel Template",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData()
                formData.append("rooms_excel", this.excel_file)
                formData.append("company", this.companyID)

                this.axios
                .post("api/v1/import-rooms-excel/", formData)
                .then((response)=>{
                   this.$toast.success("Staff Rooms Imported Succesfully",{
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
                    this.$router.push("/hms/staff-rooms")
                    this.$store.commit('reloadingPage')
                })
            }
                
        },

       
    },
    mounted(){
        this.companyID = localStorage.getItem("company_id")
        this.searchStaffRooms();
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
.vuejs3-datepicker__value{
    padding: 4px 4px !important;
    min-width: 250px;
    border-color: gray;
}
.vuejs3-datepicker__calendar{
    width: 230px;
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