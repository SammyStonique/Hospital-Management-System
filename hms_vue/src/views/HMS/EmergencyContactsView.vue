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
            <h2 class="text-center font-bold">Emergency Contacts</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/4 pl-3">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Contact</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="first_name" id="" placeholder="First Name..." v-model="first_name_search" @keyup.enter="searchEmergencyContacts">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="last_name" id="" placeholder="Last Name..." v-model="last_name_search"  @keyup.enter="searchEmergencyContacts">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="phone_number" id="" placeholder="Phone Number..." v-model="phone_number_search"  @keyup.enter="searchEmergencyContacts">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="email" id="" placeholder="Email..." v-model="email_search"  @keyup.enter="searchEmergencyContacts">
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchEmergencyContacts"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportEmergencyContactsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportEmergencyContactsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportEmergencyContactsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new emergency contact -->
                <Modal v-show="contactModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Emergency Contact Details </template>
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
                            <div class="basis-1/2" v-if="isEditing">
                                <label for="">Patient<em>*</em></label><br />
                                <input type="text" name="" id="" disabled class="rounded border bg-slate-100 border-gray-600 text-lg pl-2 w-60" v-model="patientName" required>                               
                            </div>
                            <div class="basis-1/2" v-else>
                                <label for="">Patient<em>*</em></label><br />
                                <select name="patient" ref="patientSelect" id="selectPatient" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setPatientID" onfocus="this.selectedIndex = -1;" v-model="patient">
                                    <option value="" disabled selected>---Select Patient---</option> 
                                    <option v-for="pat in patientsArray">{{pat.first_name}}  {{pat.last_name}} - #{{ pat.id_number}}</option> 
                                </select>
                            </div>
                        </div>
                        
                        <div class="text-center" v-if="isEditing">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateEmergencyContact">Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createEmergencyContact">Save</button>
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
                                <th class="text-left py-3 px-4">Phone Number</th>
                                <th class="text-left py-3 px-4">Patient</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(cont,index) in contactPersonList" :key="cont.contact_person_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-2">{{ cont.first_name }}</td>
                            <td class="text-left py-3 px-2">{{ cont.last_name }}</td>
                            <td class="text-left py-3 px-2">{{ cont.email }}</td>
                            <td class="text-left py-3 px-2">{{ cont.phone_number }}</td>
                            <td class="text-left py-3 px-2">{{ cont.patient }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editEmergencyContact(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeEmergencyContact(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="contactPersonCount"
                    :currentPage="currentPage"
                    :result="contactPersonArrLen"
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
    name: 'EmergencyContactView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Emergency Contacts',
        hospitalID: "",
        first_name: "",
        last_name: "",
        phone_number: "",
        email: "",
        first_name_search: "",
        last_name_search: "",
        email_search: "",
        phone_number_search: "",
        contactModalVisible: false,
        isEditing: false,
        isSearching: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        pageCount: 0,
        contactPersonID: "",
        contactPersonName: "",
        contactPersonList: [],
        contactPersonDetails: [],
        contactPersonResults: [],
        contactPersonArr: [],
        contactPersonArrLen: [],
        contactPersonCount: 0,
        contactPersonEditing: "",
        clearButton: true,
        watcherMsg: [],
        eStyle: null, nStyle:null, bWidth: null,
        patientsArray: [],
        patientDetails: [],
        patient: "",
        patientID: "",
        patientName: "",
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
        fetchPatients(){
            this.patientsArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-patients/", formData)
            .then((response)=>{
                for(let i=0; i<response.data.length; i++){
                    if (!response.data[i].emergency_contact_person){
                        this.patientsArray.push(response.data[i]);
                    }
                }
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        createEmergencyContact(){
            this.showLoader();
            this.emergencyContactDetails = [];
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.phone_number === ''|| this.patient === ''){
                this.$toast.error("Please Enter Contact Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = {
                    hospital: this.hospitalID,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    phone_number: this.phone_number,
                    patient: this.patientName,
                }
                this.axios
                .post("api/v1/create-emergency-contact-person/", formData)
                .then((response)=>{
                    this.emergencyContactDetails = response.data;
                    this.$toast.success("Emergency Contact Succesfully Added",{
                    duration: 3000,
                    dismissible: true
                })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    let formData = {
                        patient : this.patientID,
                        hospital: this.hospitalID
                    }
                    this.axios
                    .post("api/v1/get-patients/", formData)
                    .then((response)=>{
                        this.patientDetails = response.data;
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        let formData = new FormData();
                        formData.append('patient',this.patientDetails.patient_id);
                        formData.append('first_name',this.patientDetails.first_name);
                        formData.append('last_name',this.patientDetails.last_name);
                        formData.append('birth_date',this.patientDetails.birth_date);
                        formData.append('phone_number',this.patientDetails.phone_number);
                        formData.append('email',this.patientDetails.email);
                        formData.append('hospital',this.hospitalID);
                        formData.append('city',this.patientDetails.city);
                        formData.append('address',this.patientDetails.address);
                        formData.append('id_number',this.patientDetails.id_number);
                        formData.append('country',this.patientDetails.country);
                        formData.append('emergency_contact_person',this.emergencyContactDetails.contact_person_id);

                        this.axios
                        .put("api/v1/update-patient/", formData)
                        .then((response)=>{

                        })
                        .catch((error)=>{
                            console.log(error.message);
                            this.$toast.error("Error Assigining Patient",{
                                duration:3000,
                                dismissible: true
                            })
                        })
                        .finally(()=>{
                            this.first_name = "";
                            this.last_name = "";
                            this.email = "";
                            this.phone_number = "";
                            this.patientDetails = [];
                            this.hideLoader();
                            this.closeModal();
                            this.$store.commit('reloadingPage');
                        })
                    })
                })
            }
        },
        searchEmergencyContacts(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                first_name: this.first_name_search,
                last_name: this.last_name_search,
                email: this.email_search,
                phone_number: this.phone_number_search,
                hospital_id: this.hospitalID
            }
            this.axios
            .post(`api/v1/emergency-contact-person-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.contactPersonList = response.data.results;
                this.contactPersonResults = response.data;
                this.contactPersonArrLen = this.contactPersonList.length;
                this.contactPersonCount = this.contactPersonResults.count;
                this.pageCount = Math.ceil(this.contactPersonCount / 10);

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
        editEmergencyContact(){
            this.contact_personID = "";
            this.isEditing = true;
            let selectedContact = arguments[0];
            this.contactPersonID = this.contactPersonList[selectedContact].contact_person_id;

            let formData = {
                hospital: this.hospitalID,
                contact_person: this.contactPersonID
            }
            this.axios
            .post("api/v1/get-emergency-contact-persons/", formData)
            .then((response)=>{
                this.contactPersonDetails = response.data;
                this.first_name = this.contactPersonDetails.first_name;
                this.last_name = this.contactPersonDetails.last_name;
                this.email = this.contactPersonDetails.email;
                this.phone_number = this.contactPersonDetails.phone_number;
                this.patientName = this.contactPersonDetails.patient;
            })
            .catch((error)=>{
                console.log(error.mesage);
            })
            .finally(()=>{
                this.scrollToTop();
                this.showModal();
            })
            
        },
        updateEmergencyContact(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.phone_number === ''){
                    this.$toast.error("Please Enter Contact Details",{
                        duration:3000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
            else{
                let formData = {
                    contact_person: this.contactPersonID,
                    hospital: this.hospitalID,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    phone_number: this.phone_number,
                    patient: this.patientName
                }
                console.log(formData);
                this.axios
                .put("api/v1/update-emergency-contact-person/", formData)
                .then((response)=>{
                    this.$toast.success("Emergency Contact Succesfully Updated",{
                        duration:3000,
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
                    this.phone_number = "";
                    this.patientName = "";
                    this.hideLoader();
                    this.closeModal();
                    this.$store.commit('reloadingPage');
                    
                })
            }
        },
        removeEmergencyContact() {
            let selectedItem = arguments[0];
            this.contactPersonID = this.contactPersonList[selectedItem].contact_person_id;
            this.contactPersonName = this.contactPersonList[selectedItem].first_name + " " +this.contactPersonList[selectedItem].last_name ;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.contactPersonName}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Contact!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        hospital: this.hospitalID,
                        contact_person: this.contactPersonID
                    }
                    this.axios
                    .post("api/v1/delete-emergency-contact-person/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Contact Person removed succesfully!", {
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
                    this.$swal(`${this.contactPersonName} has not been deleted!`);
                }
            });
        },
        showModal(){
            this.scrollToTop();
            if(this.isEditing == false){
                this.first_name = "";
                this.last_name = "";
                this.email = "";
                this.phone_number = "";
            }
            this.contactModalVisible = !this.contactModalVisible;
            this.fetchPatients();
        },
        closeModal(){
            this.contactModalVisible = false;
            this.isEditing = false;
        },
        setPatientID(){
            this.patientID = "";
            if(this.$refs.patientSelect.selectedIndex > 0){
                this.selectedPatient = this.$refs.patientSelect.selectedIndex - 1;
                this.patientID = this.patientsArray[this.selectedPatient].patient_id;
                this.patientName = this.patientsArray[this.selectedPatient].first_name + " " +this.patientsArray[this.selectedPatient].last_name+ " - #"+this.patientsArray[this.selectedPatient].id_number ;
            }
        },

        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchEmergencyContacts();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchEmergencyContacts();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchEmergencyContacts();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchEmergencyContacts();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportEmergencyContactsPDF(){
            this.showLoader();
            let formData = {
                first_name: this.first_name_search,
                last_name: this.last_name_search,
                email: this.email_search,
                phone_number: this.phone_number_search,
                hospital_id: this.hospitalID
            }

            this.axios
            .post("api/v1/export-emergency-contact-person-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Emergency Contacts.pdf');
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
        exportEmergencyContactsExcel(){
            this.showLoader();
            let formData = {
                first_name: this.first_name_search,
                last_name: this.last_name_search,
                email: this.email_search,
                phone_number: this.phone_number_search,
                hospital_id: this.hospitalID
            }

            this.axios
            .post("api/v1/export-emergency-contact-person-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Emergency Contacts.xls');
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
        exportEmergencyContactsCSV(){
            this.showLoader();
            let formData = {
                first_name: this.first_name_search,
                last_name: this.last_name_search,
                email: this.email_search,
                phone_number: this.phone_number_search,
                hospital_id: this.hospitalID
            }

            this.axios
            .post("api/v1/export-emergency-contact-person-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Emergency Contacts.csv');
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
        this.searchEmergencyContacts();
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