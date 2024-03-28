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
            <h2 class="text-center font-bold">Patient Receipts</h2>
            <div class="md:px-2 w-full">
                <div class="flex items-end pb-3 w-full border-b-2 border-gray-300 mb-3">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Receipt</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="receipt_number" id="" placeholder="Receipt No..." v-model="receipt_number_search"  @keyup.enter="searchReceipts">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="reference_no" id="" placeholder="Reference No..." v-model="reference_no_search"  @keyup.enter="searchReceipts">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="client" id="" placeholder="Client..." v-model="client_search"  @keyup.enter="searchReceipts">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-2 pt-2 w-52" placeholder="Payment Method...." v-model="payment_method_search">
                                        <option value="" selected disabled  class="status-placeholder">Payment Method</option>
                                        <option value="Cash">Cash</option>
                                        <option value="Mpesa">Mpesa</option>
                                        <option value="Bank Deposit">Bank Deposit</option>
                                        <option value="EFT">EFT</option>
                                        <option value="RTGS">RTGS</option>
                                        <option value="Cheque">Cheque</option>
                                        <option value="Check-off">Check-off</option>
                                    </select>
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
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchReceipts"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportReceiptsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportReceiptsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportReceiptsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new receipt -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Receipt Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6 invoices-table">
                            <div class="basis-1/2 w-72 mr-6">
                                <label for="">Patient:<em>*</em></label><br />
                                <SearchableDropdown
                                :options="patientsArr"
                                :updateValue="selectedPatient"
                                :dropdownWidth="patientDropdownWidth"
                                :searchPlaceholder="patientsPlaceholder"
                                @option-selected="handleSelectedPatient"
                                />
                            </div>
                            <div class="basis-1/4 mr-6">
                                <label for="">Receipt Date:<em>*</em></label><br />
                                <datepicker  placeholder="Receipt Date...." v-model="receipt_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                            <div class="basis-1/4 mr-3">
                                <label for="">Banking Date:<em>*</em></label><br />
                                <datepicker  placeholder="Banking Date...." v-model="banking_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/4">
                                <label for="">Payment Method:<em>*</em></label><br />
                                <SearchableDropdown
                                    :options="paymentMethodsArr"
                                    :searchPlaceholder="paymentMethodPlaceholder"
                                    @option-selected="handleSelectedPaymentMethod"
                                />
                            </div>
                            <div class="basis-1/4">
                                <label for="">Reference No<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-52" v-model="reference_no">
                            </div>
                            <div class="basis-1/4">
                                <label for="">Cashbook:<em>*</em></label><br />
                                <SearchableDropdown
                                    :options="ledgersArr"
                                    :searchPlaceholder="ledgersPlaceholder"
                                    @option-selected="handleSelectedLedger"
                                />
                            </div>
                            <div class="basis-1/4">
                                <label for="">Amount Received:<em>*</em></label><br />
                                <input type="number" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-52" v-model="received_amount">
                                <button type="button" @click="calculateReceiptTotals" class="rounded bg-slate-600"><i class="fa fa-refresh text-sm" aria-hidden="true"></i></button>
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2">
                                <label for="">Memo:<em></em></label><br />
                                <textarea id="notes" name="description" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="description" rows="2" cols="50"></textarea>
                            </div>
                        </div>
                        <div class="shadow overflow-hidden rounded border-b border-gray-200 mb-8 w-full invoice-table">
                                <table class="min-w-full bg-white" style="width:100%"> 
                                    <thead class="bg-gray-800 text-white static">
                                        <tr class="rounded bg-slate-800 text-white font-semibold text-sm capitalize">
                                            <th class="text-left py-2 px-2" style="width:10%">Invoice</th>
                                            <th class="text-left py-2 px-2" style="width:38%">Description</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Amount</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Paid</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Due</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Payment</th>
                                            <th class="text-left py-2 px-2" style="width:10%">Balance</th>
                                            <th class="text-left py-2 px-2" style="width:1%"></th>
                                        </tr>
                                    </thead>
                                    <tbody class="">
                                        <tr v-for="(inv, index) in transformedInvoiceArray" :key="index">
                                            <td class="text-left text-sm border border-black">{{ inv.journal_no }}</td>
                                            <td class="text-left border border-black">{{ inv.description }}</td>
                                            <td class="text-left border border-black">{{ Number(inv.total_amount).toLocaleString() }}</td>
                                            <td class="text-left border border-black">{{ Number(inv.total_paid).toLocaleString() }}</td>
                                            <td class="text-left border border-black cursor-pointer" @dblclick="autoPopulatePaymentAlloc(index)">{{ Number(inv.due_amount).toLocaleString() }}</td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="inv.payment_allocation" @input="invoiceLineBalance(index)" /></td>
                                            <td class="text-left border border-black">{{ Number(inv.bal_after_alloc).toLocaleString() }}</td>
                                        </tr>
                                    
                                    </tbody>
                                </table>   
                        </div>
                        <div class="text-center">
                            <button class="rounded border bg-green-400 w-42 py-2 px-4 text-white text-lg" @click="createReceipt">Save</button>
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
                                <th class="text-left py-3 px-2" style="width:10%">Receipt No</th>
                                <th class="text-left py-3 px-2" style="width:10%">Date</th>
                                <th class="text-left py-3 px-2" style="width:10%">Bank. Date</th>
                                <th class="text-left py-3 px-2" style="width:17%">Patient</th>
                                <th class="text-left py-3 px-2" style="width:10%">Pmnt Metd</th>
                                <th class="text-left py-3 px-2" style="width:15%">Ref No</th>
                                <th class="text-left py-3 px-2" style="width:6%">Amnt</th>
                                <th class="text-left py-3 px-2" style="width:17%">Done By</th>
                                <th class="text-left py-3 px-2" style="width:4%">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(rcpt,index) in receiptList" :key="rcpt.journal_id" class="even:bg-gray-100">
                            <td></td>
                            <td class="text-left py-2">{{ rcpt.journal_no }}</td>
                            <td class="text-left py-2">{{ rcpt.issue_date }}</td>
                            <td class="text-left py-2">{{ rcpt.banking_date }}</td>
                            <td class="text-left py-2">{{ rcpt.client }}</td>
                            <td class="text-left py-2">{{ rcpt.payment_method }}</td>
                            <td class="text-left py-2">{{ rcpt.reference_no }}</td>
                            <td class="text-left py-2">{{ Number(rcpt.total_amount).toLocaleString() }}</td>
                            <td class="text-left py-2">{{ rcpt.done_by }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="printPatientReceipt(index)"><i class="fa fa-print" aria-hidden="true" title="Print"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeReceipt(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="receiptCount"
                    :currentPage="currentPage"
                    :result="receiptArrLen"
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
    name: 'PatientReceiptsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
        title: 'Hospital Management/ Receipts',
        companyID: "",
        patient: "",
        receipt_date: new Date(),
        banking_date: "",
        description: "",
        payment_method: "",
        cashbook: "",
        reference_no: "",
        received_amount: 0,
        client_search: "",
        receipt_number_search: "",
        reference_no_search: "",
        payment_method_search: "",
        description_search: "",
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
        receiptID: "",
        receiptClient: "",
        receiptNumber: "",
        receiptList: [],
        receiptDetails: [],
        receiptResults: [],
        receiptArr: [],
        receiptArrLen: [],
        receiptCount: 0,
        invoice_totals: 0,
        invoice_status: "",
        clearButton: true,
        patientsArray : [],
        patientsArr : [],
        patientInvoices: [],
        transformedInvoiceArray: [],
        patientID: "",
        patientName: "",
        patientLedger: "",
        txn_type: "RCPT",
        ledgersArray: [],
        ledgersArr: [],
        ledgerID: "",
        ledgerName: "",
        contra: 0,
        patientDropdownWidth: '400px',
        patientsPlaceholder: 'Select Patient...',
        selectedPatient: "",
        selectedLedger: "",
        journalEntryArr: [],
        journalsArr: [],
        paymentMethodsArr: ['Mpesa','Cash','Bank Deposit','EFT','Cheque','RTGS','Check-off'],
        paymentMethodPlaceholder: 'Payment Method...',
        ledgersPlaceholder: 'Select Cashbook...',
        ledger_type: 'Cashbook',
        done_by: "User",
        invoiceStatus: "Open"
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
    computed:{     
        
    },
    methods:{
        calculateReceiptTotals(){
            this.received_amount = 0;
            for(let i=0; i<this.transformedInvoiceArray.length; i++){
                if(this.transformedInvoiceArray[i].payment_allocation <= this.transformedInvoiceArray[i].due_amount){
                    this.received_amount = this.received_amount + Number(this.transformedInvoiceArray[i].payment_allocation);
                }
                else{
                    this.$toast.error("Incorrect Receipt Allocation",{
                        duration: 5000,
                        dismissible: true
                    })
                }
            }
        },
        invoiceLineBalance(){
            let selectedInvoice = arguments[0];
            if(this.transformedInvoiceArray[selectedInvoice].due_amount >= this.transformedInvoiceArray[selectedInvoice].payment_allocation){
                this.transformedInvoiceArray[selectedInvoice].bal_after_alloc = this.transformedInvoiceArray[selectedInvoice].due_amount - this.transformedInvoiceArray[selectedInvoice].payment_allocation;
            }
            else{
                this.$toast.error("Exceeded maximum allocation",{
                    duration: 5000,
                    dismissible: true
                })
                this.transformedInvoiceArray[selectedInvoice].payment_allocation = 0;
                this.transformedInvoiceArray[selectedInvoice].bal_after_alloc = this.transformedInvoiceArray[selectedInvoice].due_amount;
            }
        },
        autoPopulatePaymentAlloc(){
            let selectedInvoice = arguments[0];
            this.transformedInvoiceArray[selectedInvoice].payment_allocation = this.transformedInvoiceArray[selectedInvoice].due_amount;
            this.transformedInvoiceArray[selectedInvoice].bal_after_alloc = 0;
        },
        handleSelectedPatient(option) {
            this.selectedPatient = option;
            this.received_amount = 0;
            for (let i=0; i<this.patientsArray.length; i++){
                if((this.patientsArray[i].patient_code+ " - "+this.patientsArray[i].first_name+ " "+this.patientsArray[i].last_name) == this.selectedPatient){
                    this.patientID = this.patientsArray[i].patient_id;
                    this.patientName = this.patientsArray[i].first_name + " "+ this.patientsArray[i].last_name;
                    this.patientLedger = this.patientsArray[i].ledger_id;
                }else{
                   
                }
            }
            this.fetchInvoices();
           
        },
        handleSelectedLedger(option) {
            this.selectedLedger = option;
            for (let i=0; i<this.ledgersArray.length; i++){
                if((this.ledgersArray[i].ledger_code+ " - "+this.ledgersArray[i].ledger_name) == this.selectedLedger){
                    this.ledgerID = this.ledgersArray[i].ledger_id;
                }else{
                   
                }
            }
        },
        handleSelectedPaymentMethod(option) {
            this.payment_method = option;
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
                ledger_type: this.ledger_type
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
        fetchInvoices(){
            this.patientInvoices = [];
            this.txn_type = "INV";
            let formData = {
                company: this.companyID,
                txn_type: this.txn_type,
                client: this.patientID,
                status: this.invoiceStatus
            }
            this.axios
            .post("api/v1/fetch-journals/",formData)
            .then((response)=>{
                this.patientInvoices = response.data;
                this.transformedInvoiceArray = this.patientInvoices.map(patientInvoice =>({
                        ...patientInvoice,
                        payment_allocation: 0,
                        bal_after_alloc: 0
                    }));
                    console.log("The transformed patient invoices array is ",this.transformedInvoiceArray);
            })
            .catch((error)=>{
                console.log(error.message)
            })
        },
        createReceipt(){
            this.showLoader();
            this.journalEntryArr = [];
            if(this.selectedPatient === '' || this.receipt_date === '' || this.banking_date === '' || this.description === "" || this.payment_method === ''
                || this.selectedLedger === '' || this.reference_no === ''|| this.received_amount === "" ){
                this.$toast.error("Please Enter Receipt Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            
            }
            else if(this.received_amount === 0 || this.received_amount === ""){
                this.$toast.error("Receipt Total Cannot Be 0",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else if(this.received_amount != 0 && this.received_amount != ""){
                this.txn_type = "RCPT";
                this.invoice_totals = 0;
                this.journalsArr = [];
                for(let i=0; i<this.transformedInvoiceArray.length; i++){
                    this.invoice_totals = this.invoice_totals + Number(this.transformedInvoiceArray[i].payment_allocation);
                    if(this.transformedInvoiceArray[i].bal_after_alloc == 0){
                        this.invoice_status = "Closed";
                        let journal = {
                            "journal_id": this.transformedInvoiceArray[i].journal_id,
                            "journal_no": this.transformedInvoiceArray[i].journal_no,
                            "total_paid": Number(this.transformedInvoiceArray[i].payment_allocation),
                            "due_amount": Number(this.transformedInvoiceArray[i].bal_after_alloc),
                            "status": this.invoice_status
                        }
                        this.journalsArr.push(journal)
                    }else{
                        this.invoice_status = "Open";
                        let journal = {
                            "journal_id": this.transformedInvoiceArray[i].journal_id,
                            "journal_no": this.transformedInvoiceArray[i].journal_no,
                            "total_paid": Number(this.transformedInvoiceArray[i].payment_allocation),
                            "due_amount": Number(this.transformedInvoiceArray[i].bal_after_alloc),
                            "status": this.invoice_status
                        }
                        this.journalsArr.push(journal)

                    }
                    
                }
                if(this.received_amount === this.invoice_totals){
                    let jnlEntry1 ={
                        "date": this.formatDate(this.receipt_date),
                        "description": this.description,
                        "txn_type": this.txn_type,
                        "posting_account": this.patientLedger,
                        "debit_amount": this.contra,
                        "credit_amount": this.received_amount,
                    }
                    let jnlEntry2 = {
                        "date": this.formatDate(this.receipt_date),
                        "description": "Payment of "+this.description +" for "+this.patientName,
                        "txn_type": this.txn_type,
                        "posting_account": this.ledgerID,
                        "debit_amount": this.received_amount,
                        "credit_amount": this.contra,
                    }
                    this.journalEntryArr.push(jnlEntry1,jnlEntry2);
                    console.log("The journal entry array is ",this.journalEntryArr);
                }else{

                }
                let formData = {
                    company: this.companyID,
                    client: this.patientName,
                    client_id: this.patientID,
                    description: this.description,
                    txn_type: this.txn_type,
                    payment_method: this.payment_method,
                    reference_no: this.reference_no,
                    done_by: this.done_by,
                    banking_date: this.formatDate(this.banking_date),
                    issue_date: this.formatDate(this.receipt_date),
                    total_amount: this.received_amount,
                    journal_entry_array: this.journalEntryArr,
                    journals_array : this.journalsArr
                }
                console.log("FORM DATA IS ",formData);
                this.axios
                .post("api/v1/create-journal/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Receipt Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.selectedPatient = "";
                        this.selectedLedger = "";
                        this.selectedPaymentMethod = "";
                        this.receipt_date = "";
                        this.banking_date = "";
                        this.description = "";
                        this.received_amount = 0;
                        this.reference_no = ""
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient Receipt",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.hideLoader();
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error(error.message,{
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
        searchReceipts(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.txn_type = "RCPT";
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('client', this.client_search);
            formData.append('journal_no', this.receipt_number_search);
            formData.append('reference_no', this.reference_no_search);
            formData.append('txn_type', this.txn_type);
            formData.append('payment_method', this.payment_method_search);
            formData.append('description', this.description_search);
            formData.append('min_amount', this.description_search);
            formData.append('max_amount', this.description_search);
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
                this.receiptList = response.data.results;
                this.receiptResults = response.data;
                this.receiptArrLen = this.receiptList.length;
                this.receiptCount = this.receiptResults.count;
                this.pageCount = Math.ceil(this.receiptCount / 10);

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
        removeReceipt() {
            let selectedItem = arguments[0];
            this.receiptID = this.receiptList[selectedItem].journal_id;
            this.receiptNumber = this.receiptList[selectedItem].journal_no;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.receiptNumber}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Receipt!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        company: this.companyID,
                        journal: this.receiptID
                    }
                    this.axios
                    .post("api/v1/delete-journal/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Receipt removed succesfully!", {
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
                    this.$swal(`${this.receiptNumber} has not been deleted!`);
                }
            });
        },
        showModal(){
            this.selectedPatient = "";
            this.scrollToTop();
            this.fetchPatients();
            this.fetchLedgers();
            if(this.isEditing == false){
                this.receipt_date = new Date();
                this.banking_date = "";
                this.selectedPatient = "";
                this.selectedLedger = "";
                this.reference_no = "";
                this.received_amount = 0;
                this.patientInvoices = [];
                this.transformedInvoiceArray = [];
            }
            this.isModalVisible = !this.isModalVisible;
        },
        closeModal(){
            this.isModalVisible = false;
            this.isEditing = false;
            this.$store.commit('reloadingPage');
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchReceipts();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchReceipts();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchReceipts();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchReceipts();
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
        this.searchReceipts();
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
    min-height: 25vh;
}

</style>