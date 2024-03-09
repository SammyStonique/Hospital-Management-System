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
            <h2 class="text-center font-bold">Patients Register</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Patient</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="first_name" id="" placeholder="First Name..." v-model="first_name_search" @keyup.enter="searchPatients">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="last_name" id="" placeholder="Last Name..." v-model="last_name_search"  @keyup.enter="searchPatients">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="phone_number" id="" placeholder="Phone Number..." v-model="phone_number_search"  @keyup.enter="searchPatients">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="id_number" id="" placeholder="ID Number..." v-model="id_number_search"  @keyup.enter="searchPatients">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Birth Date...." v-model="birth_date_search" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="city" id="" placeholder="City..." v-model="city_search"  @keyup.enter="searchPatients">
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchPatients"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportPatientsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportPatientsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportPatientsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new patient -->
                <Modal v-show="patientModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Patient Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">First Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="first_name" required>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Last Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="last_name" required>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Email<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" v-model="email" :style="{borderColor: eStyle,borderWidth: bWidth+'px' }" required><br />
                                <span v-if="watcherMsg.email" :style="{color: eStyle, fontSize:10 + 'px'}">{{watcherMsg.email}}</span>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" placeholder="e.g 07XXXX" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px' }" required><br />
                                <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">ID Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="id_number">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Birth Date<em>*</em></label><br />
                                <datepicker  placeholder="Birth Date...." v-model="birth_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">City<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="city">
                            </div>
                            <div class="basis-1/2">
                                <label for="">Country<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="country">
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Address<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="address">
                            </div>
                        </div>
                        <div class="border-b border-gray-400 pb-3">
                            <p class="font-bold">Emergency Contact Details</p>
                        </div>
                        <div class="flex mb-6 mt-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">First Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_first_name" required>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Last Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_last_name" required>
                            </div>
                        </div><div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Email<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_email" required>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_phone_number" required>
                            </div>
                        </div>
                        <div class="text-center" v-if="isEditing">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updatePatient">Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createPatient">Save</button>
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
                                <th class="text-left py-3 px-4">First Name</th>
                                <th class="text-left py-3 px-4">Last Name</th>
                                <th class="text-left py-3 px-4">Email</th>
                                <th class="text-left py-3 px-4">ID Number</th>
                                <th class="text-left py-3 px-4">Phone Number</th>
                                <th class="text-left py-3 px-4">Birth Date</th>
                                <th class="text-left py-3 px-4">City</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(pat,index) in patientList" :key="pat.patient_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ pat.first_name }}</td>
                            <td class="text-left py-3 px-4">{{ pat.last_name }}</td>
                            <td class="text-left py-3 px-4">{{ pat.email }}</td>
                            <td class="text-left py-3 px-4">{{ pat.id_number }}</td>
                            <td class="text-left py-3 px-4">{{ pat.phone_number }}</td>
                            <td class="text-left py-3 px-4">{{ pat.birth_date }}</td>
                            <td class="text-left py-3 px-4">{{ pat.city }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editPatient(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removePatient(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="patientCount"
                    :currentPage="currentPage"
                    :result="patientArrLen"
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
    name: 'PatientsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Patients',
        hospitalID: "",
        first_name: "",
        last_name: "",
        birth_date: null,
        city: "",
        phone_number: "",
        id_number: "",
        email: "",
        country: "",
        address: "",
        first_name_search: "",
        last_name_search: "",
        id_number_search: "",
        phone_number_search: "",
        city_search: "",
        birth_date_search: null,
        patientModalVisible: false,
        isEditing: false,
        isSearching: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        pageCount: 0,
        patientID: "",
        patientName: "",
        patientList: [],
        patientDetails: [],
        emergencyContactDetails: [],
        emergencyContactID: "",
        patientResults: [],
        patientArr: [],
        patientArrLen: [],
        patientCount: 0,
        patientEditing: "",
        clearButton: true,
        contact_person_first_name: "",
        contact_person_last_name: "",
        contact_person_email: "",
        contact_person_phone_number: "",
        watcherMsg: [],
        eStyle: null, nStyle:null, bWidth: null,
    }
  },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker
    },
    watch:{
      email(value){
        // binding this to the data value in the email input  
        this.email = value; 
        this.validateEmail(value);
        },
        phone_number(value){
            this.phone_number = value;
            this.validatePhoneNumber(value)
        },
    },
    methods:{
        validateEmail(value){  
            if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value)){ 
                this.watcherMsg['email'] = '';
                this.eStyle = 'green';
                this.bWidth = 2

            } else{
                if(value == ''){
                    this.watcherMsg['email'] = ''; 
                    this.eStyle = ''

                }
                else{
                    this.watcherMsg['email'] = 'Invalid Email Address'; 
                    this.eStyle = 'red'
                    this.bWidth = 2
                }
            }  
        },
        validatePhoneNumber(value){
            if ((/^(?:254|\+254|0)?((?:(?:7(?:(?:[01249][0-9])|(?:5[789])|(?:6[89])))|(?:1(?:[1][0-5])))[0-9]{6})$/.test(value))|| (/^(?:254|\+254|0)?((?:(?:7(?:(?:3[0-9])|(?:5[0-6])|(8[5-9])))|(?:1(?:[0][0-2])))[0-9]{6})$/.test(value))){
                    this.nStyle = 'green';
                    this.watcherMsg['phone_number'] = ''
                    this.bWidth = 2

            }else{
                if(value == ''){
                    this.nStyle = '';
                    this.watcherMsg['phone_number'] = ''                        
                }
                else{
                    this.nStyle = 'red';
                    this.watcherMsg['phone_number'] = 'Invalid Phone Number'
                    this.bWidth = 2
                }
            }
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            const year = date.getFullYear().toString()
            const month = ('0' + (date.getMonth() + 1)).slice(-2);
            const day = ('0' + date.getDate()).slice(-2);
            return `${year}-${month}-${day}`;
        },
        createPatient(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.birth_date === '' || this.city === ''
                 || this.phone_number === '' || this.id_number === '' || this.address === '' || this.country === '' || this.contact_person_first_name === ''
                 || this.contact_person_last_name === '' || this.contact_person_email === '' || this.contact_person_phone_number === ''){
                this.$toast.error("Please Enter Patient Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = {
                    hospital: this.hospitalID,
                    first_name: this.contact_person_first_name,
                    last_name: this.contact_person_last_name,
                    email: this.contact_person_email,
                    phone_number: this.contact_person_phone_number,
                }
                this.axios
                .post("api/v1/create-emergency-contact-person/", formData)
                .then((response)=>{
                    this.emergencyContactDetails = response.data;
                    this.emergencyContactID = this.emergencyContactDetails.contact_person_id;
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    let formData = {
                        hospital: this.hospitalID,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        email: this.email,
                        birth_date: this.formatDate(this.birth_date),
                        phone_number: this.phone_number,
                        city: this.city,
                        id_number: this.id_number,
                        address: this.address,
                        country: this.country,
                        emergency_contact_person: this.emergencyContactID
                    }
                    
                    this.axios
                    .post("api/v1/create-patient/", formData)
                    .then((response)=>{
                        this.patientDetails = response.data;
                        this.$toast.success("Patient Added Succesfully",{
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
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.city = "";
                        this.address = "";
                        this.country = "";
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    })
                })
            }
        },
        searchPatients(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('first_name', this.first_name_search);
            formData.append('last_name', this.last_name_search);
            formData.append('phone_number', this.phone_number_search);
            formData.append('id_number', this.id_number_search);
            formData.append('city', this.city_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.birth_date_search !=null) && (typeof(this.birth_date_search) == "object")){
                formData.append('birth_date', this.formatDate(this.birth_date_search));
            }else{
                this.birth_date_search = "";
                formData.append('birth_date', this.birth_date_search);
            }               

            this.axios
            .post(`api/v1/patients-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.patientList = response.data.results;
                this.patientResults = response.data;
                this.patientArrLen = this.patientList.length;
                this.patientCount = this.patientResults.count;
                this.pageCount = Math.ceil(this.patientCount / 10);

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
        editPatient(){
            this.isEditing = true;
            let selectedPatient = arguments[0];
            this.patientID = this.patientList[selectedPatient].patient_id;
            let formData = {
                company: this.companyID,
                patient: this.patientID
            }
            this.axios
            .post("api/v1/get-patients/", formData)
            .then((response)=>{
                this.patientDetails = response.data;
                this.first_name = this.patientDetails.first_name;
                this.last_name = this.patientDetails.last_name;
                this.email = this.patientDetails.email;
                this.id_number = this.patientDetails.id_number;
                this.birth_date = this.patientDetails.birth_date;
                this.city = this.patientDetails.city;
                this.phone_number = this.patientDetails.phone_number;
                this.address = this.patientDetails.address;
                this.country = this.patientDetails.country;
            })
            .catch((error)=>{
                console.log(error.mesage);
            })
            .finally(()=>{
                this.scrollToTop();
                this.showModal();
            })
            
        },
        updatePatient(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.birth_date === '' || this.city === ''
                 || this.phone_number === '' || this.id_number === '' || this.address === '' || this.country === ''){
                    this.$toast.error("Please Enter Patient Details",{
                        duration:5000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
            else{
                let formData = new FormData();
                formData.append('patient',this.patientDetails.patient_id);
                formData.append('first_name',this.managerDetails.first_name);
                formData.append('last_name',this.managerDetails.last_name);
                formData.append('birth_date',this.formatDate(this.birth_date));
                formData.append('phone_number',this.phone_number);
                formData.append('email',this.email);
                formData.append('hospital',this.hospitalID);
                formData.append('city',this.managerDetails.city);
                formData.append('address',this.managerDetails.address);
                formData.append('id_number',this.managerDetails.id_number);
                formData.append('country',this.managerDetails.country);

                this.axios
                .put("api/v1/update-patient/", formData)
                .then((response)=>{
                    this.$toast.success("Patient Succesfully Updated",{
                        duration:5000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.first_name = "";
                    this.last_name = "";
                    this.email = "";
                    this.birth_date = "";
                    this.id_number = "";
                    this.phone_number = "";
                    this.city = "";
                    this.address = "";
                    this.country = "";
                    this.hideLoader();
                    this.closeModal();
                    this.$store.commit('reloadingPage');
                })
            }
        },
        removePatient() {
            let selectedItem = arguments[0];
            this.patientID = this.patientList[selectedItem].patient_id;
            this.patientName = this.patientList[selectedItem].first_name + " " +this.patientList[selectedItem].last_name ;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.managerName}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Patient!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        hospital: this.hospitalID,
                        patient: this.patientID
                    }
                    this.axios
                    .post("api/v1/delete-patient/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Patient removed succesfully!", {
                            icon: "success",
                        });
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        this.$store.commit('reloadingPage');
                    })
                
                } else {
                    this.$swal(`${this.patientName} has not been deleted!`);
                }
            });
        },
        showModal(){
            this.scrollToTop();
            if(this.isEditing == false){
                this.first_name = "";
                this.last_name = "";
                this.email = "";
                this.birth_date = "";
                this.id_number = "";
                this.phone_number = "";
                this.city = "";
                this.address = "";
                this.country = "";
            }
            this.patientModalVisible = !this.patientModalVisible;
        },
        closeModal(){
            this.patientModalVisible = false;
            this.isEditing = false;
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchPatient();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchPatients();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchPatients();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchPatients();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportPatientsPDF(){
            this.showLoader();
            let formData = new FormData();
            formData.append('first_name', this.first_name_search);
            formData.append('last_name', this.last_name_search);
            formData.append('phone_number', this.phone_number_search);
            formData.append('id_number', this.id_number_search);
            formData.append('city', this.city_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.birth_date_search !=null) && (typeof(this.birth_date_search) == "object")){
                formData.append('birth_date', this.formatDate(this.birth_date_search));
            }else{
                this.birth_date_search = "";
                formData.append('birth_date', this.birth_date_search);
            } 

            this.axios
            .post("api/v1/export-patients-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients.pdf');
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
        exportPatientsExcel(){
            this.showLoader();
            let formData = new FormData();
            formData.append('first_name', this.first_name_search);
            formData.append('last_name', this.last_name_search);
            formData.append('phone_number', this.phone_number_search);
            formData.append('id_number', this.id_number_search);
            formData.append('city', this.city_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.birth_date_search !=null) && (typeof(this.birth_date_search) == "object")){
                formData.append('birth_date', this.formatDate(this.birth_date_search));
            }else{
                this.birth_date_search = "";
                formData.append('birth_date', this.birth_date_search);
            }

            this.axios
            .post("api/v1/export-patients-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients.xls');
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
        exportPatientsCSV(){
            this.showLoader();
            let formData = new FormData();
            formData.append('first_name', this.first_name_search);
            formData.append('last_name', this.last_name_search);
            formData.append('phone_number', this.phone_number_search);
            formData.append('id_number', this.id_number_search);
            formData.append('city', this.city_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.birth_date_search !=null) && (typeof(this.birth_date_search) == "object")){
                formData.append('birth_date', this.formatDate(this.birth_date_search));
            }else{
                this.birth_date_search = "";
                formData.append('birth_date', this.birth_date_search);
            }

            this.axios
            .post("api/v1/export-patients-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients.csv');
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
        this.hospitalID = localStorage.getItem("company_id")
        this.searchPatients();
    }
}
</script>

<style scoped>
.main-content{
  z-index: -1;
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
</style>