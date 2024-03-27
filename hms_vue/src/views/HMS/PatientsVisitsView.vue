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
        <div class="subsection rounded bg-white">
            <h2 class="text-center font-bold">Patients Visits</h2>
            <div class="md:px-8 w-full">
                <div class="flex items-end pb-3 w-full border-b-2 border-gray-300 mb-3">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Visit</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="patient" id="" placeholder="Patient..." v-model="patient_search" @keyup.enter="searchPatientHistory">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="doctor" id="" placeholder="..."  @keyup.enter="searchPatientHistory">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="staff" id="" placeholder="Staff..." v-model="staff_search"  @keyup.enter="searchPatientHistory">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="patient_code" id="" placeholder="Patient Code..." v-model="patient_code_search"  @keyup.enter="searchPatientHistory">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Date From...." v-model="date_from_search" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Date To...." v-model="date_to_search" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchPatientHistory"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportPatientsHistoryPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportPatientsHistoryExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportPatientsHistoryCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new patient visit -->
                <Modal v-show="patientModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Patient Visit Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6 patient-visit-container">
                            <div class="basis-1/2 mr-6">
                                <label for="">Date<em>*</em></label><br />
                                <datepicker  placeholder="Date...." v-model="visit_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Patient<em>*</em></label><br />
                                <input type="text" name="" disabled id="" class="rounded border border-gray-600 bg-gray-100 text-lg pl-2" v-model="patientEditing" v-if="isEditing">
                                <div v-else>
                                    <SearchableDropdown
                                        :options="patientsArr"
                                        :dropdownWidth="patientDropdownWidth"
                                        :searchPlaceholder="patientsPlaceholder"
                                        @option-selected="handleSelectedPatient"
                                    />
                                </div>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6"  v-if="isEditing">
                                <label for="">Doctor<em>*</em></label><br />
                                <SearchableDropdown
                                    :updateValue="selectedDoctor"
                                    :options="doctorsArr"
                                    :dropdownWidth="patientDropdownWidth"
                                    :fontSize="doctorFontSize"
                                    @option-selected="handleSelectedDoctor"
                                />
                            </div>
                            <div class="basis-1/2" v-else>
                                <label for="">Doctor<em>*</em></label><br />
                                <SearchableDropdown
                                    :options="doctorsArr"
                                    :dropdownWidth="patientDropdownWidth"
                                    :searchPlaceholder="doctorsPlaceholder"
                                    :fontSize="doctorFontSize"
                                    @option-selected="handleSelectedDoctor"
                                />
                            </div>
                    
                                <div class="basis-1/2">
                                    <label for="">Staff<em>*</em></label><br />
                                    <SearchableDropdown
                                        :options="staffArr"
                                        :dropdownWidth="patientDropdownWidth"
                                        :searchPlaceholder="staffPlaceholder"
                                        :fontSize="doctorFontSize"
                                        @option-selected="handleSelectedStaff"
                                    />
                                </div>
                            </div>
                        <div class="flex mb-3">
                            <div class="basis-1/2">
                                <label for="">Notes<em>*</em></label><br />
                                <textarea id="notes" name="visit_notes" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="visit_notes" rows="4" cols="50"></textarea>
                            </div>
                        </div>
                        <div class="flex mb-6" v-if="!isEditing">
                            <div class="basis-1/2 mr-6">
                                <label for=""><em></em></label><br />
                                <input type="checkbox" name="" id="" class="rounded border border-gray-600 text-lg pl-2 mr-3" @click="showChargeFeesOption" v-model="applyMedicalFees">
                                <label for="">Add Medical Fees<em></em></label>
                            </div>
                        </div>
                        <div v-if="medicalFeeCharge && !isEditing">
                            <div class="border-b border-gray-400 pb-3">
                                <p class="font-bold">Fees Details</p>
                            </div>
                            <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8 mb-8 w-full fees-table">
                                <table class="min-w-full bg-white"> 
                                    <thead class="bg-gray-800 text-white static">
                                        <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                            <th class="text-left px-2 row-span-4">Fees Charged</th>
                                            <th class="text-right px-2 row-span-2">Amount</th>
                                            <th class="text-right px-2"></th>
                                            <th class="text-right px-2"></th>
                                        </tr>
                                    </thead>
                                    <tbody class="">
                                        <tr v-for="(fee, index) in fees" :key="index">
        
                                            <td class="text-left border border-black text-sm">
                                                <SearchableDropdown
                                                    :options="feesArr"
                                                    :dropdownWidth="feesDropdownWidth"
                                                    :searchPlaceholder="feesPlaceholder"
                                                    @option-selected="handleSelectedFees"
                                                    @reset="removeRow"
                                                />
                                            </td>
                                            <td class="text-left border border-black"><input type="number" class="text-right w-full" v-model="fee.amount" /></td>
                                            <td class="border border-black">
                                                <button type="button" @click="removeRow(index)"><i class="fa fa-minus-circle" aria-hidden="true"></i></button>
                                            </td>
                                            <td class="border border-black">
                                                <button type="button" @click="addRow"><i class="fa fa-plus" aria-hidden="true"></i></button>
                                            </td>
                                        </tr>
                                    
                                    </tbody>
                                </table>   
                            </div>
                        
                        </div>
                        <div class="text-center" v-if="isEditing">
                            <button class="rounded border bg-green-400 w-42 py-2 px-4 text-white text-lg" @click="updatePatientHistory">Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createPatientHistory">Save</button>
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
                                <th class="text-left py-3 px-2">Date</th>
                                <th class="text-left py-3 px-2">Patient</th>
                                <th class="text-left py-3 px-2">Staff To Visit</th>
                                <th class="text-left py-3 px-2">Notes</th>
                                <th class="text-left py-3 px-2">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(hist,index) in patientHistoryList" :key="hist.patient_history_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-2">{{ hist.date }}</td>
                            <td class="text-left py-2">{{ hist.patient_name }}</td>
                            <td class="text-left py-2" v-if="hist.staff_profile ==='Doctor'">Dr. {{ hist.staff_name}}</td>
                            <td class="text-left py-2" v-else>{{ hist.staff_name}}</td>
                            <td class="text-left py-2">{{ hist.notes }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editPatientHistory(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removePatientHistory(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="patientHistCount"
                    :currentPage="currentPage"
                    :result="patientHistArrLen"
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
import SearchableDropdown from '@/components/SearchableDropdown.vue'
import Datepicker from 'vuejs3-datepicker';

export default{
    name: 'PatientsVisitsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Patients Visits',
        hospitalID: "",
        patient: "",
        doctor: "",
        visit_date: new Date(),
        staff: "",
        visit_notes: "",
        id_number: "",
        patient_search: "",
        patient_code_search: "",
        staff_search: "",
        date_from_search: new Date(),
        date_to_search: new Date(),
        patientModalVisible: false,
        isEditing: false,
        isSearching: false,
        isAddingFees: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        patientHistoryID: "",
        patientID: "",
        patientName: "",
        patientCode: "",
        patientLedgerID: "",
        patientHistoryList: [],
        patientHistoryDetails: [],
        patientHistoryResults: [],
        patientHistoryArr: [],
        patientHistArrLen: [],
        patientHistCount: 0,
        patientHistoryEditing: "",
        clearButton: true,
        doctorID: "",
        doctorName: "",
        staffID: "",
        staffName: "",
        patientEditing: "",
        staffArray: [],
        staffArr: [],
        doctorsArray: [],
        doctorsArr: [],
        feesID: "",
        feesName: "",
        feesLedger: "",
        feesArray: [],
        feesArr: [],
        journalDetails: [],
        medicalFeeCharge: false,
        fees: [
        {itemIndex:0, type: null, amount: null, fee_name: null, fee_ledger: null }
        ],
        itemInd: 0,
        applyMedicalFees: false,
        visitDoctor: false,
        txn_type: "",
        journalEntryArr: [],
        contra: 0,
        invoice_description: [],
        invDescr: "",
        invoice_totals: 0,
        patientDropdownWidth: '400px',
        patientsPlaceholder: 'Select Patient...',
        selectedPatient: "",
        patientsArray: [],
        patientsArr: [],
        doctorsPlaceholder: 'Select Doctor...',
        doctorFontSize: '14px',
        selectedDoctor: "",
        staffPlaceholder: 'Select Staff...',
        selectedStaff: "",
        feesDropdownWidth: '250px',
        feesPlaceholder: 'Select Fees...',
        selectedFees: "",
    }
  },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        Loader,
        MyPagination,
        Datepicker,
        SearchableDropdown
    },
    methods:{
        addRow() {
            this.itemInd += 1;
            this.fees.push({itemIndex:this.itemInd, type: null, amount: null, fee_name: null, fee_ledger: null });
        },
        removeRow(){
            if(this.fees.length > 1){
                let selectedFee = arguments[0];
                this.fees.splice(selectedFee, 1);
                
            }else{
                this.fees = [{itemIndex:0, type: null, amount: null , fee_name: null, fee_ledger: null}];
                this.selectedFees = "";
            }
        },
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
                for(let i=0; i<this.patientsArray.length; i++){
                    this.patientsArr.push(this.patientsArray[i].patient_code + " - "+this.patientsArray[i].first_name+ " "+this.patientsArray[i].last_name)
                }
                return this.patientsArr;
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
                for(let i=0; i<this.doctorsArray.length; i++){
                    this.doctorsArr.push("Dr. " +this.doctorsArray[i].first_name+ " "+this.doctorsArray[i].last_name+" ("+this.doctorsArray[i].email+")")
                }
                return this.doctorsArr;
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        fetchStaff(){
            this.staffArray = [];
            let formData = {
                company: this.hospitalID,
            }
            this.axios
            .post("api/v1/department-staff-list/", formData)
            .then((response)=>{
                for(let i=0; i<response.data.length; i++){
                    if(response.data[i].profile != "Super Admin" && response.data[i].profile != "Patient"&& response.data[i].profile != "Doctor"){
                        this.staffArray.push(response.data[i]);
                    }
                }
                for(let i=0; i<this.staffArray.length; i++){
                    this.staffArr.push(this.staffArray[i].first_name+ " "+this.staffArray[i].last_name+" ("+this.staffArray[i].email+")")
                }
                return this.staffArr;
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        fetchFees(){
            this.feesArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-medical-fees/", formData)
            .then((response)=>{
                this.feesArray = response.data;
                for(let i=0; i<this.feesArray.length; i++){
                    this.feesArr.push(this.feesArray[i].fee_name);
                }
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        handleSelectedPatient(option) {
            this.selectedPatient = option;
            for (let i=0; i<this.patientsArray.length; i++){
                if((this.patientsArray[i].patient_code+ " - "+this.patientsArray[i].first_name+ " "+this.patientsArray[i].last_name) == this.selectedPatient){
                    this.patientID = this.patientsArray[i].patient_id;
                    this.patientName = this.patientsArray[i].first_name + " "+ this.patientsArray[i].last_name;
                    this.patientLedgerID = this.patientsArray[i].ledger_id;
                }else{
                   
                }
            }
        },
        handleSelectedDoctor(option) {
            this.selectedDoctor = option;
            for (let i=0; i<this.doctorsArray.length; i++){
                if(("Dr. " +this.doctorsArray[i].first_name+ " "+this.doctorsArray[i].last_name+" ("+this.doctorsArray[i].email+")") == this.selectedDoctor){
                    this.doctorID = this.doctorsArray[i].user;
                    this.doctorName = this.doctorsArray[i].first_name + " "+ this.doctorsArray[i].last_name;
                }else{
                   
                }
            }
        },
        handleSelectedStaff(option) {
            this.selectedStaff = option;
            for (let i=0; i<this.staffArray.length; i++){
                if((this.staffArray[i].first_name+ " "+this.staffArray[i].last_name+" ("+this.staffArray[i].email+")") == this.selectedStaff){
                    this.staffID = this.staffArray[i].user_id;
                    this.staffName = this.staffArray[i].first_name + " "+ this.staffArray[i].last_name;
                }else{
                   
                }
            }
        },
        handleSelectedFees(option) {
            this.selectedFees = option;
            for (let i=0; i<this.feesArray.length; i++){
                if((this.feesArray[i].fee_name) == this.selectedFees){
                    this.feesID = this.feesArray[i].fees_id;
                    this.fees[this.itemInd].fee_ledger = this.feesArray[i].posting_account;
                    this.fees[this.itemInd].fee_name = this.feesArray[i].fee_name;
                    this.fees[this.itemInd].amount = this.feesArray[i].default_amount;
                }else{
                   
                }
            }
            console.log("The fees array is ",this.fees);
        },
        createPatientHistory(){
            this.showLoader();
            if(this.selectedPatient === '' || this.visit_date === '' || this.visit_notes === ''|| (this.selectedStaff === '' && this.selectedDocotor === '')){
                this.$toast.error("Please Enter Patient Visit Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else if(this.medicalFeeCharge && this.fees[0].type != null && this.fees[0].amount != null){
                this.invoice_description = [];
                this.txn_type = "INV";
                this.journalEntryArr = [];
                for(let i=0; i<this.fees.length; i++){
                    if(this.fees[i].amount != null){
                        this.invoice_totals += Number(this.fees[i].amount);
                        this.invoice_description.push(this.fees[i].fee_name);
                        let jnlEntry1 ={
                            "date": this.formatDate(this.visit_date),
                            "description": this.fees[i].fee_name,
                            "txn_type": this.txn_type,
                            "posting_account": this.patientID,
                            "debit_amount": this.fees[i].amount,
                            "credit_amount": this.contra,
                        }
                        let jnlEntry2 = {
                            "date": this.formatDate(this.visit_date),
                            "description": this.fees[i].fee_name +" for "+this.patientName,
                            "txn_type": this.txn_type,
                            "posting_account": this.fees[i].fee_ledger,
                            "debit_amount": this.contra,
                            "credit_amount": this.fees[i].amount,
                        }
                        this.journalEntryArr.push(jnlEntry1,jnlEntry2);
                    }else{
                        this.$toast.error("Please input fee amount",{
                            duration: 3000,
                            dismissible: true
                        })
                    }
                }
                if(this.invoice_description.length > 1){
                    for(let x=0; x<this.invoice_description.length; x++){
                        this.invDescr += (this.invoice_description[x]+", ")
                    }
                }else{
                    this.invDescr = this.invoice_description[0];
                }   
                let formData = {
                    hospital: this.hospitalID,
                    doctor: this.doctorID,
                    staff: this.userID,
                    patient: this.patientID,
                    visit_notes: this.visit_notes,
                    company: this.hospitalID,
                    client: this.patientName,
                    description: this.invDescr,
                    txn_type: this.txn_type,
                    issue_date: this.formatDate(this.visit_date),
                    total_amount: this.invoice_totals,
                    journal_entry_array: this.journalEntryArr,
                }
                this.axios
                .post("api/v1/create-patient-visit/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Visit Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.visit_date = "";
                        this.visit_notes = "";
                        this.medicalFeeCharge = false;
                        this.fees = [{itemIndex:0, type: null, amount: null , fee_name: null, fee_ledger: null}];
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient Visit",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.hideLoader();
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient Visit",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .finally(()=>{

                })                                
            }
            else{
                let formData = {
                    hospital: this.hospitalID,
                    doctor: this.doctorID,
                    staff: this.userID,
                    patient: this.patientID,
                    visit_notes: this.visit_notes,
                    date: this.formatDate(this.visit_date)
                }
                this.axios
                .post("api/v1/create-patient-visit/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Visit Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.visit_date = "";
                        this.visit_notes = "";
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient Visit",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.hideLoader();
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient Visit",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .finally(()=>{

                })

            }
        },
        searchPatientHistory(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('patient', this.patient_search);
            formData.append('staff', this.staff_search);
            formData.append('patient_code', this.patient_code_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.date_from_search !=null) && (typeof(this.date_from_search) == "object")){
                formData.append('date_from', this.formatDate(this.date_from_search));
            }else{
                this.date_from_search = "";
                formData.append('date_from', this.date_from_search);
            }  
            if((this.date_to_search !=null) && (typeof(this.date_to_search) == "object")){
                formData.append('date_to', this.formatDate(this.date_to_search));
            }else{
                this.date_to_search = "";
                formData.append('date_to', this.date_to_search);
            }             
            

            this.axios
            .post(`api/v1/patients-history-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.patientHistoryList = response.data.results;
                this.patientHistoryResults = response.data;
                this.patientHistArrLen = this.patientHistoryList.length;
                this.patientHistCount = this.patientHistoryResults.count;
                this.pageCount = Math.ceil(this.patientHistCount / 10);

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
        editPatientHistory(){
            this.isEditing = true;
            let selectedPatientHistory = arguments[0];
            this.visitDoctor = this.patientHistoryList[selectedPatientHistory].staff_is_doctor;
            this.patientHistoryID = this.patientHistoryList[selectedPatientHistory].patient_history_id;
            this.patientID = this.patientHistoryList[selectedPatientHistory].patient_id;
            this.visit_date = this.patientHistoryList[selectedPatientHistory].date;
            this.visit_notes = this.patientHistoryList[selectedPatientHistory].notes;
            if(this.visitDoctor){
                this.doctorID = this.patientHistoryList[selectedPatientHistory].staff_id;
                this.selectedDoctor = "Dr. "+this.patientHistoryList[selectedPatientHistory].staff_name+" ("+this.patientHistoryList[selectedPatientHistory].staff_email+")";
                this.selectedStaff = "";
            }
            else{
                this.staffID = this.patientHistoryList[selectedPatientHistory].staff_id;
                this.selectedStaff = this.patientHistoryList[selectedPatientHistory].staff_name+" ("+this.patientHistoryList[selectedPatientHistory].staff_email+")";
                this.selectedDoctor = "";
            }
            this.patientEditing = this.patientHistoryList[selectedPatientHistory].patient_name;
            
            this.scrollToTop();
            this.showModal();
            
        },
        updatePatientHistory(){
            this.showLoader();
            if(this.patientEditing === '' || this.visit_date === '' || this.visit_notes === '' 
                || (this.selectedStaff === '' && this.selectedDoctor === '')){
                    this.$toast.error("Please Enter Patient Visit Details",{
                        duration:3000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
            else if(!this.medicalFeeCharge || this.fees[0].type === null){
                let formData = new FormData();
                formData.append('patient_history', this.patientHistoryID);
                formData.append('patient', this.patientID);
                formData.append('date', this.formatDate(this.visit_date));
                formData.append('notes', this.visit_notes);
                formData.append('hospital', this.hospitalID);
                if(this.selectedDoctor != "" && this.selectedStaff == ""){
                    this.visitDoctor = true;
                    formData.append('staff', this.doctorID);
                    formData.append('is_doctor', this.visitDoctor);
                }else if(this.selectedStaff != "" && this.selectedDoctor == ""){
                    this.visitDoctor = false;
                    formData.append('staff', this.staffID);
                    formData.append('is_doctor', this.visitDoctor);
                }

                this.axios
                .put("api/v1/update-patient-history/", formData)
                .then((response)=>{
                    this.$toast.success("Patient Visit Updated Succesfully",{
                        duration:3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.$store.commit('reloadingPage');
                })
            }
        },
        removePatientHistory() {
            let selectedItem = arguments[0];
            this.patientHistoryID = this.patientHistoryList[selectedItem].patient_history_id;
            this.patientName = this.patientHistoryList[selectedItem].patient_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.patientName}'s Visit?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Visit!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        hospital: this.hospitalID,
                        patient_history: this.patientHistoryID
                    }
                    this.axios
                    .post("api/v1/delete-patient-history/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Patient Visit removed succesfully!", {
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
                    this.$swal(`${this.patientName}'s Visit has not been deleted!`);
                }
            });
        },
        showModal(){
            this.scrollToTop();
            this.fees = [{itemIndex:0, type: null, amount: null , fee_name: null, fee_ledger: null}];
            this.feesLedger = "";
            this.invoice_totals = 0;
            this.invoice_description = "";
            this.applyMedicalFees = false;
            this.medicalFeeCharge = false;
            if(this.isEditing == false){
                this.visit_date = new Date();
                this.visit_notes = "";
            }
            this.patientModalVisible = !this.patientModalVisible;
            this.fetchDoctors();
            this.fetchStaff();
            this.fetchPatients();
        },
        showChargeFeesOption(){
            this.medicalFeeCharge = !this.medicalFeeCharge;
            this.fetchFees();
        },
        closeModal(){
            this.patientModalVisible = false;
            this.isEditing = false;
            this.selectedDoctor = "";
            this.selectedPatient = "";
            this.selectedStaff = "";
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchPatientHistory();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchPatientHistory();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchPatientHistory();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchPatientHistory();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportPatientsHistoryPDF(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient', this.patient_search);
            formData.append('staff', this.staff_search);
            formData.append('patient_code', this.patient_code_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.date_from_search !=null) && (typeof(this.date_from_search) == "object")){
                formData.append('date_from', this.formatDate(this.date_from_search));
            }else{
                this.date_from_search = "";
                formData.append('date_from', this.date_from_search);
            }  
            if((this.date_to_search !=null) && (typeof(this.date_to_search) == "object")){
                formData.append('date_to', this.formatDate(this.date_to_search));
            }else{
                this.date_to_search = "";
                formData.append('date_to', this.date_to_search);
            } 

            this.axios
            .post("api/v1/export-patients-history-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients Visits.pdf');
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
        exportPatientsHistoryExcel(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient', this.patient_search);
            formData.append('staff', this.staff_search);
            formData.append('patient_code', this.patient_code_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.date_from_search !=null) && (typeof(this.date_from_search) == "object")){
                formData.append('date_from', this.formatDate(this.date_from_search));
            }else{
                this.date_from_search = "";
                formData.append('date_from', this.date_from_search);
            }  
            if((this.date_to_search !=null) && (typeof(this.date_to_search) == "object")){
                formData.append('date_to', this.formatDate(this.date_to_search));
            }else{
                this.date_to_search = "";
                formData.append('date_to', this.date_to_search);
            }

            this.axios
            .post("api/v1/export-patients-history-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients Visits.xls');
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
        exportPatientsHistoryCSV(){
            this.showLoader();
            let formData = new FormData();
            formData.append('patient', this.patient_search);
            formData.append('staff', this.staff_search);
            formData.append('patient_code', this.patient_code_search);
            formData.append('hospital_id', this.hospitalID);  
            if((this.date_from_search !=null) && (typeof(this.date_from_search) == "object")){
                formData.append('date_from', this.formatDate(this.date_from_search));
            }else{
                this.date_from_search = "";
                formData.append('date_from', this.date_from_search);
            }  
            if((this.date_to_search !=null) && (typeof(this.date_to_search) == "object")){
                formData.append('date_to', this.formatDate(this.date_to_search));
            }else{
                this.date_to_search = "";
                formData.append('date_to', this.date_to_search);
            }

            this.axios
            .post("api/v1/export-patients-history-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Patients Visits.csv');
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
        this.searchPatientHistory();
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
.import-table{
    min-height: 100vh;
    max-height: 100vh;
    overflow-y: scroll;
    overflow-x: scroll;
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
.fees-table{
    min-height: 25vh;
    max-height: 40vh;
    overflow-y: scroll;
    overflow-x: scroll;
}
.patient-visit-container{
    min-width: 60vw;
}
</style>