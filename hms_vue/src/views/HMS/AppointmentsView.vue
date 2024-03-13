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
            <h2 class="text-center font-bold">Appointments</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/4 pl-3">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Appointment</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="patient_name" id="" placeholder="Patient Name..." v-model="patient_name_search" @keyup.enter="searchAppointments">
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="doctor_name" id="" placeholder="Doctor Name..." v-model="doctor_name_search"  @keyup.enter="searchAppointments">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2 pl-3 items-center">
                                    <datepicker  placeholder="Date From...." v-model="from_date" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                                <div class="basis-1/2 pl-3 items-center">
                                    <datepicker  placeholder="Date To...." v-model="to_date" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchAppointments"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportAppointmentsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportAppointmentsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportAppointmentsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new appointment -->
                <Modal v-show="aptModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Appointment Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6" v-if="isEditing">
                                <label for="">Patient<em>*</em></label><br />
                                <input type="text" name="" id="" disabled class="rounded border bg-slate-100 border-gray-600 text-lg pl-2 w-60" v-model="patientName" required>                               
                            </div>
                            <div class="basis-1/2 mr-6" v-else>
                                <label for="">Patient<em>*</em></label><br />
                                <select name="patient" ref="patientSelect" id="selectPatient" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setPatientID" onfocus="this.selectedIndex = -1;" v-model="patient">
                                    <option value="" disabled selected>---Select Patient---</option> 
                                    <option v-for="pat in patientsArray">{{pat.first_name}}  {{pat.last_name}} - #{{ pat.id_number}}</option> 
                                </select>
                            </div>
                            <div class="basis-1/2"  v-if="isEditing">
                                <label for="">Doctor<em>*</em></label><br />
                                <select name="doctorUpdate" ref="doctorUpdateSelect" id="selectUpdateDoctor" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateDoctorID" onfocus="this.selectedIndex = -1;" v-model="doctorEditing">
                                    <option v-for="doct in doctorsArray" :key="doct.doctor_id" :value="(doct.first_name+' '+doct.last_name)" :label="(doct.first_name+' '+doct.last_name)" :selected="((doct.first_name+' '+doct.last_name)===doctorEditing)">{{doct.first_name}}  {{doct.last_name}}</option> 
                                </select>
                            </div>
                            <div class="basis-1/2" v-else>
                                <label for="">Doctor<em>*</em></label><br />
                                <select name="doctor" ref="doctorSelect" id="selectDoctor" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setDoctorID" onfocus="this.selectedIndex = -1;" v-model="doctor">
                                    <option value="" disabled selected>---Select Doctor---</option> 
                                    <option v-for="doct in doctorsArray">Dr. {{doct.first_name}}  {{doct.last_name}}</option> 
                                </select>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Date<em>*</em></label><br />
                                <datepicker  placeholder="Appointment Date...." v-model="appointment_date" clearable :clear-button="clearButton">
                                    </datepicker>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Time<em></em></label><br />
                                <input type="time" name="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="appointment_time">
                            </div>

                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2">
                                <label for="">Notes<em>*</em></label><br />
                                <textarea id="notes" name="appointment_notes" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="appointment_notes" rows="4" cols="50"></textarea>
                            </div>
                        </div>
                        
                        <div class="text-center" v-if="isEditing">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateAppointment">Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createAppointment">Save</button>
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
                                <th class="text-left py-3 px-4">Patient</th>
                                <th class="text-left py-3 px-4">Patient ID No.</th>
                                <th class="text-left py-3 px-4">Doctor</th>
                                <th class="text-left py-3 px-4">Date</th>
                                <th class="text-left py-3 px-4">Time</th>
                                <th class="text-left py-3 px-4">Notes</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(apt,index) in appointmentsList" :key="apt.appointment_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-2">{{ apt.patient_name }}</td>
                            <td class="text-left py-3 px-2">{{ apt.patient_id_number }}</td>
                            <td class="text-left py-3 px-2">Dr. {{ apt.doctor_name }}</td>
                            <td class="text-left py-3 px-2">{{ apt.date }}</td>
                            <td class="text-left py-3 px-2">{{ apt.time }}</td>
                            <td class="text-left py-3 px-2">{{ apt.notes }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editAppointment(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeAppointment(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="appointmentsCount"
                    :currentPage="currentPage"
                    :result="appointmentsArrLen"
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
    name: 'AppointmentsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Appointments',
        hospitalID: "",
        patient: "",
        doctor: "",
        appointment_date: null,
        appointment_time: "",
        appointment_notes: "",
        patient_name_search: "",
        doctor_name_search: "",
        from_date: null,
        to_date: null,
        aptModalVisible: false,
        isEditing: false,
        isSearching: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        pageCount: 0,
        appointmentID: "",
        appointmentsList: [],
        appointmentsDetails: [],
        appointmentsResults: [],
        appointmentsArr: [],
        appointmentsArrLen: [],
        appointmentsCount: 0,
        appointmentsEditing: "",
        clearButton: true,
        patientsArray: [],
        patientDetails: [],
        patient: "",
        patientID: "",
        patientName: "",
        doctorsArray: [],
        doctorDetails: [],
        doctor: "",
        doctorID: "",
        doctUpdateID: "",
        doctorName: "",
        doctUpdateName: "",
        doctorEditing: "",
    }
  },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker,
    },
    methods:{
        formatDate(dateString) {
            const date = new Date(dateString);
            const year = date.getFullYear().toString()
            const month = ('0' + (date.getMonth() + 1)).slice(-2);
            const day = ('0' + date.getDate()).slice(-2);
            return `${year}-${month}-${day}`;
        },
        fetchPatients(){
            this.patientsArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-patients/", formData)
            .then((response)=>{
                this.patientsArray = response.data;
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        fetchDoctors(){
            this.doctorsArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-department-doctors/", formData)
            .then((response)=>{
                this.doctorsArray = response.data;
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        createAppointment(){
            this.showLoader();
            this.appointmentsDetails = [];
            if(this.patient === '' || this.appointment_date === '' || this.doctor===''|| this.notes===''){
                this.$toast.error("Please Enter Appointment Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData();
                formData.append('patient', this.patientID);
                formData.append('patient_name', this.patientName);
                formData.append('date', this.formatDate(this.appointment_date));
                formData.append('doctor', this.doctorID);
                formData.append('doctor_name', this.doctorName);
                formData.append('notes', this.appointment_notes);
                if(this.appointment_time){
                    formData.append('time', this.appointment_time);
                }
                formData.append('hospital', this.hospitalID);
                
                this.axios
                .post("api/v1/create-appointment/", formData)
                .then((response)=>{
                    this.appointmentsDetails = response.data;
                    this.$toast.success("Appointment Scheduled Succesfully",{
                    duration: 3000,
                    dismissible: true
                })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                   
                    this.patient = "";
                    this.doctor = "";
                    this.appointment_date = "";
                    this.appointment_time = "";
                    this.appointment_notes = "";
                    this.hideLoader();
                    this.closeModal();
                    this.$store.commit('reloadingPage');

                })
            }
        },
        searchAppointments(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;

            let formData = new FormData();
            formData.append('patient_name', this.patient_name_search);
            if((this.from_date !=null) && (typeof(this.from_date) == "object")){
                formData.append('from_date', this.formatDate(this.from_date));
            }else{
                this.from_date = "";
                formData.append('from_date', this.from_date);
            }   
            if((this.to_date !=null) && (typeof(this.to_date) == "object")){
                formData.append('to_date', this.formatDate(this.to_date));
            }else{
                this.to_date = "";
                formData.append('to_date', this.to_date);
            } 
            formData.append('doctor_name', this.doctor_name_search);
            formData.append('hospital', this.hospitalID); 

            this.axios
            .post(`api/v1/appointments-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.appointmentsList = response.data.results;
                this.appointmentsResults = response.data;
                this.appointmentsArrLen = this.appointmentsList.length;
                this.appointmentsCount = this.appointmentsResults.count;
                this.pageCount = Math.ceil(this.appointmentsCount / 10);

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
        editAppointment(){
            this.appointmentID = "";
            this.isEditing = true;
            let selectedAppointment = arguments[0];
            this.appointmentID = this.appointmentsList[selectedAppointment].appointment_id;
            this.patientID = this.appointmentsList[selectedAppointment].patient_id;

            let formData = {
                hospital: this.hospitalID,
                appointment: this.appointmentID,
                patient: this.patientID
            }
            this.axios
            .post("api/v1/get-appointments/", formData)
            .then((response)=>{
                this.appointmentsDetails = response.data;
                this.patientID = this.appointmentsDetails.patient;
                this.doctorID = this.appointmentsDetails.doctor;
                this.patientName = this.appointmentsDetails.patient_name;
                this.doctorEditing = this.appointmentsDetails.doctor_name;
                this.appointment_date = this.appointmentsDetails.date;
                this.appointment_time = this.appointmentsDetails.time;
                this.appointment_notes = this.appointmentsDetails.notes;
            })
            .catch((error)=>{
                console.log(error.mesage);
            })
            .finally(()=>{
                this.scrollToTop();
                this.showModal();
            })
            
        },
        updateAppointment(){
            this.showLoader();
            if(this.patientName === '' || this.appointment_date === '' || this.notes ===''|| this.doctorEditing===''){
                    this.$toast.error("Please Enter Appointment Details",{
                        duration:3000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
            else{
                let formData = new FormData();
                formData.append('appointment', this.appointmentID);
                formData.append('patient', this.patientID);
                formData.append('date', this.formatDate(this.appointment_date));
                if(this.doctUpdateID != 0){
                    formData.append('doctor', this.doctUpdateID);
                    formData.append('doctor_name', this.doctUpdateName);
                }else{
                    formData.append('doctor', this.doctorID);
                }
                formData.append('notes', this.appointment_notes);
                if(this.appointment_time){
                    formData.append('time', this.appointment_time);
                }
                formData.append('hospital', this.hospitalID);
                console.log(formData);
                this.axios
                .put("api/v1/update-appointment/", formData)
                .then((response)=>{
                    this.$toast.success("Appointment Succesfully Updated",{
                        duration:3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{            
                    this.patient = "";
                    this.doctor = "";
                    this.appointment_date = "";
                    this.appointment_notes = "";
                    this.appointment_time = "";
                    this.doctorID = "";
                    this.doctorEditing = "";
                    this.hideLoader();
                    this.closeModal();
                    this.$store.commit('reloadingPage');
                    
                })
            }
        },
        removeAppointment() {
            let selectedItem = arguments[0];
            this.appointmentID = this.appointmentsList[selectedItem].appointment_id;
            this.patientName = this.appointmentsList[selectedItem].patient_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.patientName}'s Appointment?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Appointment!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        hospital: this.hospitalID,
                        appointment: this.appointmentID
                    }
                    this.axios
                    .post("api/v1/delete-appointment/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Appointment removed succesfully!", {
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
                this.patient = "";
                this.doctor = "";
                this.appointment_date = "";
                this.appointment_time = "";
                this.appointment_notes = "";
            }
            this.aptModalVisible = !this.aptModalVisible;
            this.fetchPatients();
            this.fetchDoctors();
        },
        closeModal(){
            this.aptModalVisible = false;
            this.isEditing = false;
        },
        setPatientID(){
            this.patientID = "";
            if(this.$refs.patientSelect.selectedIndex > 0){
                let selectedPatient = this.$refs.patientSelect.selectedIndex - 1;
                this.patientID = this.patientsArray[selectedPatient].patient_id;
                this.patientName = this.patientsArray[selectedPatient].first_name + " " +this.patientsArray[selectedPatient].last_name+ " - #"+this.patientsArray[selectedPatient].id_number ;
            }
        },
        setDoctorID(){
            this.doctorID = "";
            if(this.$refs.doctorSelect.selectedIndex > 0){
                let selectedDoctor = this.$refs.doctorSelect.selectedIndex - 1;
                this.doctorID = this.doctorsArray[selectedDoctor].doctor_id;
                this.doctorName = this.doctorsArray[selectedDoctor].first_name + " " +this.doctorsArray[selectedDoctor].last_name;
            }
        },
        setUpdateDoctorID(){
        this.doctUpdateID = "";
        if(this.$refs.doctorUpdateSelect.selectedIndex >= 0){
            let selectedUpdateDoct = this.$refs.doctorUpdateSelect.selectedIndex;
            this.doctUpdateID = this.doctorsArray[selectedUpdateDoct].doctor_id;
            this.doctUpdateName = this.doctorsArray[selectedUpdateDoct].first_name + " " +this.doctorsArray[selectedUpdateDoct].last_name;
            console.log("The selected Doctor ID is ",this.doctUpdateID);
            console.log("The selected Doctor Name is ",this.doctUpdateName);
        }
      },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchAppointments();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchAppointments();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchAppointments();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchAppointments();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportAppointmentsPDF(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient_name', this.patient);
            if((this.from_date !=null) && (typeof(this.from_date) == "object")){
                formData.append('from_date', this.formatDate(this.from_date));
            }else{
                this.from_date = "";
                formData.append('from_date', this.from_date);
            }   
            if((this.to_date !=null) && (typeof(this.to_date) == "object")){
                formData.append('to_date', this.formatDate(this.to_date));
            }else{
                this.to_date = "";
                formData.append('to_date', this.to_date);
            } 
            formData.append('doctor_name', this.doctor);
            formData.append('hospital', this.hospitalID);

            this.axios
            .post("api/v1/export-appointments-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Appointments.pdf');
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
        exportAppointmentsExcel(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient_name', this.patient);
            if((this.from_date !=null) && (typeof(this.from_date) == "object")){
                formData.append('from_date', this.formatDate(this.from_date));
            }else{
                this.from_date = "";
                formData.append('from_date', this.from_date);
            }   
            if((this.to_date !=null) && (typeof(this.to_date) == "object")){
                formData.append('to_date', this.formatDate(this.to_date));
            }else{
                this.to_date = "";
                formData.append('to_date', this.to_date);
            } 
            formData.append('doctor_name', this.doctor);
            formData.append('hospital', this.hospitalID);

            this.axios
            .post("api/v1/export-appointments-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Appointments.xls');
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
        exportAppointmentsCSV(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient_name', this.patient);
            if((this.from_date !=null) && (typeof(this.from_date) == "object")){
                formData.append('from_date', this.formatDate(this.from_date));
            }else{
                this.from_date = "";
                formData.append('from_date', this.from_date);
            }   
            if((this.to_date !=null) && (typeof(this.to_date) == "object")){
                formData.append('to_date', this.formatDate(this.to_date));
            }else{
                this.to_date = "";
                formData.append('to_date', this.to_date);
            } 
            formData.append('doctor_name', this.doctor);
            formData.append('hospital', this.hospitalID);

            this.axios
            .post("api/v1/export-appointments-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Appointments.csv');
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
        this.searchAppointments();
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