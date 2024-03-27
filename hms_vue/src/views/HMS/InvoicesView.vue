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
            <h2 class="text-center font-bold">Invoices</h2>
            <div class="md:px-2 w-full">
                <div class="flex items-end pb-3 w-full border-b-2 border-gray-300 mb-3">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Invoice</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="invoice_number" id="" placeholder="Invoice No..." v-model="invoice_number_search"  @keyup.enter="searchInvoices">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="client" id="" placeholder="Client..." v-model="client_search"  @keyup.enter="searchInvoices">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="patient_code" id="" placeholder="Patient Code..." v-model="patient_code_search"  @keyup.enter="searchInvoices">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="description" id="" placeholder="Description..." v-model="description_search"  @keyup.enter="searchInvoices">
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
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchInvoices"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportInvoicesPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportInvoicesExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportInvoicesCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new invoice -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Invoice Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6 invoices-table">
                            <div class="basis-1/2 w-72 mr-6">
                                <label for="">Patient<em>*</em></label><br />
                                <SearchableDropdown
                                :options="patientsArr"
                                :dropdownWidth="patientDropdownWidth"
                                :searchPlaceholder="patientsPlaceholder"
                                @option-selected="handleSelectedPatient"
                                />
                            </div>
                            <div class="basis-1/4 mr-6">
                                <label for="">Invoice Date<em>*</em></label><br />
                                <datepicker  placeholder="Invoice Date...." v-model="invoice_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                            <div class="basis-1/4 mr-3">
                                <label for="">Due Date<em>*</em></label><br />
                                <datepicker  placeholder="Due Date...." v-model="due_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2">
                                <label for="">Memo<em>*</em></label><br />
                                <textarea id="notes" name="description" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="description" rows="4" cols="50"></textarea>
                            </div>
                        </div>
                        <div class="shadow overflow-hidden rounded border-b border-gray-200 mb-8 w-full invoice-table">
                                <table class="min-w-full bg-white" style="width:100%"> 
                                    <thead class="bg-gray-800 text-white static">
                                        <tr class="rounded bg-slate-800 text-white font-semibold text-sm capitalize">
                                            <th class="text-left py-2 px-2" style="width:20%">Income Account</th>
                                            <th class="text-left py-2 px-2" style="width:35%">Description</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Cost</th>
                                            <th class="text-left py-2 px-2" style="width:5%">Qty</th>
                                            <th class="text-left py-2 px-2" style="width:8%">Tax Rate</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Tax Amnt</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Sub Total</th>
                                            <th class="text-left py-2 px-2" style="width:1%"></th>
                                            <th class="text-left py-2 px-2" style="width:1%"></th>
                                        </tr>
                                    </thead>
                                    <tbody class="">
                                        <tr v-for="(led, index) in ledgers" :key="index">
        
                                            <td class="text-left text-sm border border-black">
                                                <SearchableDropdown
                                                    :options="ledgersArr"
                                                    :searchPlaceholder="ledgersPlaceholder"
                                                    @option-selected="handleSelectedLedger"
                                                />
                                            </td>
                                            <td class="text-left border border-black"><input type="text" class="text-left w-full" v-model="led.details" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.cost" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.quantity" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.tax_rate" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.tax_amount" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.sub_total" /></td>
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
                        <div class="text-center">
                            <button class="rounded border bg-green-400 w-42 py-2 px-4 text-white text-lg" @click="createInvoice">Save</button>
                        </div>
                    </form>
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
                </Modal>
                <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                    <table class="min-w-full bg-white" style="width:100%"> 
                        <thead class="bg-gray-800 text-white">
                            <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                <th style="width:1%">#</th>
                                <th class="text-left py-3 px-2" style="width:10%">Invoice No</th>
                                <th class="text-left py-3 px-2" style="width:15%">Patient</th>
                                <th class="text-left py-3 px-2" style="width:55%">Description</th>
                                <th class="text-left py-3 px-2" style="width:5%">Amnt</th>
                                <th class="text-left py-3 px-2" style="width:3%">Paid</th>
                                <th class="text-left py-3 px-2" style="width:5%">Balance</th>
                                <th class="text-left py-3 px-2" style="width:3%">Status</th>
                                <th class="text-left py-3 px-2" style="width:3%">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(inv,index) in invoiceList" :key="inv.patient_id" class="even:bg-gray-100">
                            <td></td>
                            <td class="text-left py-2">{{ inv.journal_no }}</td>
                            <td class="text-left py-2">{{ inv.client }}</td>
                            <td class="text-left py-2 overflow-x:hidden">{{ inv.description }}</td>
                            <td class="text-left py-2">{{ Number(inv.total_amount).toLocaleString() }}</td>
                            <td class="text-left py-2">{{ Number(inv.total_paid).toLocaleString() }}</td>
                            <td class="text-left py-2">{{ Number(inv.due_amount).toLocaleString() }}</td>
                            <td class="text-left py-2">{{ inv.status }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="printPatientInvoice(index)"><i class="fa fa-print" aria-hidden="true" title="Print"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeInvoice(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="invoiceCount"
                    :currentPage="currentPage"
                    :result="invoiceArrLen"
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
    name: 'InvoicesView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Invoices',
        companyID: "",
        patient: "",
        invoice_date: "",
        due_date: "",
        description: "",
        client_search: "",
        description_search: "",
        invoice_number_search: "",
        patient_code_search: "",
        min_amount_search: "",
        max_amount_search: "",
        date_from: null,
        date_to: null,
        isModalVisible: false,
        isEditing: false,
        isSearching: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        invoiceID: "",
        invoiceClient: "",
        invoiceNumber: "",
        invoiceList: [],
        invoiceDetails: [],
        invoiceResults: [],
        invoiceArr: [],
        invoiceArrLen: [],
        invoiceCount: 0,
        invoice_totals: 0,
        clearButton: true,
        patientsArray : [],
        patientsArr : [],
        patientID: "",
        patientName: "",
        patientLedger: "",
        txn_type: "INV",
        ledgersArray: [],
        ledgersArr: [],
        ledgerID: "",
        ledgerName: "",
        ledgers: [
            {itemIndex:0, account: null, details: null, cost: null, quantity: null, tax_rate: null, tax_amount: null, sub_total: null }
        ],
        itemInd: 0,
        contra: 0,
        ledgersPlaceholder: 'Posting Account...',
        patientDropdownWidth: '400px',
        patientsPlaceholder: 'Select Patient...',
        selectedPatient: "",
        selectedLedger: "",
        journalEntryArr: [],
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
        handleSelectedPatient(option) {
            this.selectedPatient = option;
            for (let i=0; i<this.patientsArray.length; i++){
                if((this.patientsArray[i].patient_code+ " - "+this.patientsArray[i].first_name+ " "+this.patientsArray[i].last_name) == this.selectedPatient){
                    this.patientID = this.patientsArray[i].patient_id;
                    this.patientName = this.patientsArray[i].first_name + " "+ this.patientsArray[i].last_name;
                    this.patientLedger = this.patientsArray[i].ledger_id;
                }else{
                   
                }
            }
        },
        handleSelectedLedger(option) {
            this.selectedLedger = option;
            console.log("The selected ledger is ",this.selectedLedger);
            for (let i=0; i<this.ledgersArray.length; i++){
                if((this.ledgersArray[i].ledger_code+ " - "+this.ledgersArray[i].ledger_name) == this.selectedLedger){
                    this.ledgerID = this.ledgersArray[i].ledger_id;
                    this.ledgers[this.itemInd].account = this.ledgersArray[i].ledger_id;
                }else{
                   
                }
            }
        },
        addRow() {
            this.itemInd += 1;
            this.ledgers.push({itemIndex:0,account: null, details: null, cost: null, quantity: null, tax_rate: null, tax_amount: null, sub_total: null});
        },
        removeRow(){
            if(this.ledgers.length > 1){
                let selectedLedger = arguments[0];
                this.ledgers.splice(selectedLedger, 1);
                
            }else{
                this.ledgers = [{itemIndex:0,account: null, details: null, cost: null, quantity: null, tax_rate: null, tax_amount: null, sub_total: null }];
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
                hospital: this.companyID,
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
        fetchLedgers(){
            this.ledgersArray = [];
            let formData = {
                company: this.companyID,
            }
            this.axios
            .post("api/v1/fetch-ledgers/", formData)
            .then((response)=>{
                this.ledgersArray = response.data;
                for(let i=0; i<this.ledgersArray.length; i++){
                    this.ledgersArr.push(this.ledgersArray[i].ledger_code + " - "+this.ledgersArray[i].ledger_name)
                }
                return this.ledgersArr;
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        createInvoice(){
            this.showLoader();
            this.journalEntryArr = [];
            if(this.selectedPatient === '' || this.invoice_date === '' || this.due_date === '' || this.description === ""){
                this.$toast.error("Please Enter Invoice Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
                console.log("Ledger account is ", this.ledgers[0].account);
                console.log("Ledger cost is ", this.ledgers[0].cost);
                console.log("Ledger subtotal is ", this.ledgers[0].sub_total);
            }
            else if(this.ledgers[0].account != null && this.ledgers[0].cost != null && this.ledgers[0].sub_total != null){
                this.txn_type = "INV";
                for(let i=0; i<this.ledgers.length; i++){
                    if(this.ledgers[i].sub_total != null){
                        this.invoice_totals += Number(this.ledgers[i].sub_total);
                        let jnlEntry1 ={
                            "date": this.formatDate(this.invoice_date),
                            "description": this.ledgers[i].details,
                            "txn_type": this.txn_type,
                            "posting_account": this.patientLedger,
                            "debit_amount": this.ledgers[i].sub_total,
                            "credit_amount": this.contra,
                        }
                        let jnlEntry2 = {
                            "date": this.formatDate(this.invoice_date),
                            "description": this.ledgers[i].details +" for "+this.patientName,
                            "txn_type": this.txn_type,
                            "posting_account": this.ledgerID,
                            "debit_amount": this.contra,
                            "credit_amount": this.ledgers[i].sub_total,
                        }
                        this.journalEntryArr.push(jnlEntry1,jnlEntry2);
                        console.log("The journal entry array is ",this.journalEntryArr);
                    }else{

                    }
                }
                let formData = {
                    company: this.companyID,
                    client: this.patientName,
                    client_id: this.patientID,
                    description: this.description,
                    txn_type: this.txn_type,
                    issue_date: this.formatDate(this.invoice_date),
                    due_date: this.formatDate(this.due_date),
                    total_amount: this.invoice_totals,
                    journal_entry_array: this.journalEntryArr,
                }
                console.log("FORM DATA IS ",formData);
                this.axios
                .post("api/v1/create-journal/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Invoice Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.patient = "";
                        this.invoice_date = "";
                        this.due_date = "";
                        this.description = "";
                        this.ledgers = [{itemIndex:0, account: null, details: null, cost: null, quantity: null, tax_rate: null, tax_amount: null, sub_total: null }];
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.hideLoader();
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient Invoice",{
                        duration: 3000,
                        dismissible: true
                    })
                    this.hideLoader();
                })
                .finally(()=>{

                })
            }else{
                this.$toast.error("ERROR",{
                        duration: 3000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
        },
        searchInvoices(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('client', this.client_search);
            formData.append('journal_no', this.invoice_number_search);
            formData.append('description', this.description_search);
            formData.append('txn_type', this.txn_type);
            formData.append('min_amount', this.min_amount_search);
            formData.append('max_amount', this.max_amount_search);
            formData.append('company_id', this.companyID);  
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
            .post(`api/v1/journals-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.invoiceList = response.data.results;
                this.invoiceResults = response.data;
                this.invoiceArrLen = this.invoiceList.length;
                this.invoiceCount = this.invoiceResults.count;
                this.pageCount = Math.ceil(this.invoiceCount / 10);

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
            this.visit_creation = false;
            this.contact_personID = "";
            this.isEditing = true;
            let selectedPatient = arguments[0];
            this.patientID = this.patientList[selectedPatient].patient_id;
            let formData = {
                hospital: this.hospitalID,
                patient: this.patientID
            }
            this.axios
            .post("api/v1/get-patients/", formData)
            .then((response)=>{
                this.patientDetails = response.data;
                this.patient_code = this.patientDetails.patient_code;
                this.first_name = this.patientDetails.first_name;
                this.last_name = this.patientDetails.last_name;
                this.email = this.patientDetails.email;
                this.id_number = this.patientDetails.id_number;
                this.birth_date = this.patientDetails.birth_date;
                this.city = this.patientDetails.city;
                this.gender = this.patientDetails.gender;
                this.phone_number = this.patientDetails.phone_number;
                this.address = this.patientDetails.address;
                this.country = this.patientDetails.country;
                this.contact_personID = this.patientDetails.emergency_contact_person;
            })
            .catch((error)=>{
                console.log(error.mesage);
            })
            .finally(()=>{
                if(this.contact_personID){
                    this.isAddingContactPerson = false;
                    let formData = {
                        contact_person: this.contact_personID,
                        hospital: this.hospitalID
                    }
                    this.axios
                    .post("api/v1/get-emergency-contact-persons/", formData)
                    .then((response)=>{
                        this.contact_person_first_name = response.data.first_name;
                        this.contact_person_last_name = response.data.last_name;
                        this.contact_person_email = response.data.email;
                        this.contact_person_phone_number = response.data.phone_number;
                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                }else{
                    this.isAddingContactPerson = true;
                    this.contact_person_first_name = "";
                    this.contact_person_last_name = "";
                    this.contact_person_email = "";
                    this.contact_person_phone_number = "";
                }
                
                this.scrollToTop();
                this.showModal();
            })
            
        },
        updatePatient(){
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.birth_date === '' || this.city === '' || this.gender ===''
                 || this.phone_number === '' || this.id_number === '' || this.address === '' || this.country === '' || this.contact_person_first_name === ''
                 || this.contact_person_last_name === '' || this.contact_person_email === '' || this.contact_person_phone_number === ''){
                    this.$toast.error("Please Enter Patient Details",{
                        duration:3000,
                        dismissible: true
                    })
                    this.hideLoader();
            }
            else if(this.contact_personID){
                let formData = new FormData();
                formData.append('patient',this.patientDetails.patient_id);
                formData.append('patient_code',this.patient_code);
                formData.append('first_name',this.first_name);
                formData.append('last_name',this.last_name);
                formData.append('birth_date',this.formatDate(this.birth_date));
                formData.append('phone_number',this.phone_number);
                formData.append('email',this.email);
                formData.append('hospital',this.hospitalID);
                formData.append('city',this.city);
                formData.append('gender',this.gender);
                formData.append('address',this.address);
                formData.append('id_number',this.id_number);
                formData.append('country',this.country);
                formData.append('emergency_contact_person',this.contact_personID);

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
                    let formData = {
                        contact_person: this.contact_personID,
                        hospital: this.hospitalID,
                        first_name: this.contact_person_first_name,
                        last_name: this.contact_person_last_name,
                        email: this.contact_person_email,
                        phone_number: this.contact_person_phone_number,
                    }
                    this.axios
                    .put("api/v1/update-emergency-contact-person/", formData)
                    .then((response)=>{

                    })
                    .catch((error)=>{
                        console.log(error.message);
                    })
                    .finally(()=>{
                        this.patient_code = "";
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.gender = "";
                        this.city = "";
                        this.address = "";
                        this.country = "";
                        this.contact_person_first_name = "";
                        this.contact_person_last_name = "";
                        this.contact_person_email = "";
                        this.contact_person_phone_number = "";
                        this.contact_personID = "";
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    })
                    
                })
            }else if(this.contact_personID == null){
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
                    let formData = new FormData();
                    formData.append('patient',this.patientDetails.patient_id);
                    formData.append('patient_code',this.patient_code);
                    formData.append('first_name',this.first_name);
                    formData.append('last_name',this.last_name);
                    formData.append('birth_date',this.formatDate(this.birth_date));
                    formData.append('phone_number',this.phone_number);
                    formData.append('email',this.email);
                    formData.append('hospital',this.hospitalID);
                    formData.append('city',this.city);
                    formData.append('gender',this.gender);
                    formData.append('address',this.address);
                    formData.append('id_number',this.id_number);
                    formData.append('country',this.country);
                    formData.append('emergency_contact_person', this.emergencyContactID);

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
                        this.patient_code = "";
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.city = "";
                        this.gender = "";
                        this.address = "";
                        this.country = "";
                        this.contact_person_first_name = "";
                        this.contact_person_last_name = "";
                        this.contact_person_email = "";
                        this.contact_person_phone_number = "";
                        this.contact_personID = "";
                        this.isAddingContactPerson = false;
                        this.isEditing = false;
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    })
                })
            }
            else{
                this.hideLoader();
                this.$toast.error("Error Updating Patient",{
                    duration:3000,
                    dismissible: true
                })
            }
        },
        removeInvoice() {
            let selectedItem = arguments[0];
            this.invoiceID = this.invoiceList[selectedItem].journal_id;
            this.invoiceNumber = this.invoiceList[selectedItem].journal_no;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.invoiceNumber}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Invoice!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        company: this.companyID,
                        journal: this.invoiceID
                    }
                    this.axios
                    .post("api/v1/delete-journal/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Invoice removed succesfully!", {
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
                    this.$swal(`${this.invoiceNumber} has not been deleted!`);
                }
            });
        },
        showModal(){
            this.scrollToTop();
            this.fetchPatients();
            this.fetchLedgers();
            if(this.isEditing == false){
                this.invoice_date = "";
                this.due_date = "";
                this.patient = "";
                this.ledgers = [{itemIndex:0, account: null, details: null, cost: null, quantity: null, tax_rate: null, tax_amount: null, sub_total: null }];
            }
            this.isModalVisible = !this.isModalVisible;
        },
        closeModal(){
            this.isModalVisible = false;
            this.isEditing = false;
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchInvoices();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchInvoices();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchInvoices();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchInvoices();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        printPatientInvoice() {
            this.showLoader();
            let selectedInvoice = arguments[0];
            this.invoiceID = this.invoiceList[selectedInvoice].journal_id;

            let formData = {
                invoice: this.invoiceID,
                hospital: this.companyID
            }
            this.axios
            .post("api/v1/patient-invoice-pdf/", formData, { responseType: 'blob' })
            .then((response) => {
            if(response.status == 200){
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'Invoice.pdf');
                document.body.appendChild(link);
                link.click();
            }
            
            })
            .catch((error) => {
            console.log(error);
            })
            .finally(()=>{
            this.hideLoader();
            });
            
        },
        exportInvoicesPDF(){
            this.showLoader();
            let formData = new FormData();
            formData.append('first_name', this.first_name_search);
            formData.append('last_name', this.last_name_search);
            formData.append('phone_number', this.phone_number_search);
            formData.append('id_number', this.id_number_search);
            formData.append('gender', this.gender_search);
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
            formData.append('gender', this.gender_search);
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
            formData.append('gender', this.gender_search);
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
                formData.append("patients_excel", this.excel_file) 

                this.axios
                .post("api/v1/display-patients-import-excel/", formData)
                .then((response)=>{
                    this.excelPatList = response.data.patients;
                    console.log(this.excelPatList);
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                })
            }
            
        },
        importPatientsExcel(){
            this.showLoader();
            if(!this.excelPatList.length){
                this.$toast.error("Please Import Excel Template",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let formData = new FormData()
                formData.append("patients_excel", this.excel_file)
                formData.append("hospital_id", this.hospitalID)

                this.axios
                .post("api/v1/import-patients-excel/", formData)
                .then((response)=>{
                   this.$toast.success("Patients Imported Succesfully",{
                        duration: 3000,
                        dismissible: true
                   })
                })
                .catch((error)=>{
                    this.$toast.error("Import Error",{
                        duration: 3000,
                        dismissible: true
                   })
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.excelPatList = [];
                    this.excel_file = "";
                    this.$router.push("/hms/patients")
                    this.$store.commit('reloadingPage')
                })
            }
                
        },

    },
    mounted(){
        this.companyID = localStorage.getItem("company_id")
        this.searchInvoices();
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
.invoices-table{
    min-width: 70vw;
}
.invoice-table{
    min-height: 50vh;
}

</style>