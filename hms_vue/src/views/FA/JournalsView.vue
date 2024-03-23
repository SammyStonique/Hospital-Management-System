<template>
    <Loader
    :loader="loader"
    :showLoader="showLoader"
    :hideLoader="hideLoader"
    />
    <NavBar
    :title="title"
    />
    <SideBarFA />
    <div class="main-content bg-gray-100 px-4 py-4">
        <div class="subsection rounded bg-white p-3">
            <h2 class="text-center font-bold">Journals</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
                    <div class="mb-4 flex items-end h-24">
                        <div class="basis-1/6">
                            <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Journal</button>
                        </div>
                        <div class="basis-3/4">
                            <div class="flex mb-3">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="number" id="" placeholder="Journal No..." v-model="journal_no_search" @keyup.enter="searchJournals">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="min_amount" id="" placeholder="Min Amount..." v-model="min_amount_search"  @keyup.enter="searchJournals">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="max_amount" id="" placeholder="Max Amount..." v-model="max_amount_search"  @keyup.enter="searchJournals">
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/3 pl-3 items-center">
                                    <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="description" id="" placeholder="Description..." v-model="description_search"  @keyup.enter="searchJournals">
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Date From...." v-model="date_from" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                                <div class="basis-1/3 pl-3 items-center">
                                    <datepicker  placeholder="Date To...." v-model="date_to" clearable :clear-button="clearButton">
                                    </datepicker>
                                </div>
                            </div>
                        </div>
                        
                        <div class="basis-1/8 pl-3 w-36">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchJournals"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                        </div>
                        <div class="basis-1/8 pl-3 w-36">
                            <div class="print-dropdown">
                                <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                                <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                            </div>
                            <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                                <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                                <button @click="exportJournalsPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                                <button @click="exportJournalsExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                                <button @click="exportJournalsCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new journal -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Journal Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/3 mr-4">
                                <label for="">Date<em>*</em></label><br />
                                <datepicker  placeholder="Date...." v-model="journal_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div>
                            <div class="basis-2/3">
                                <label for="">Description<em>*</em></label><br />
                                <textarea id="description" name="description" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="description" rows="4" cols="40"></textarea>
                            </div>
                        </div>
                        <div class="shadow overflow-hidden rounded border-b border-gray-200 mb-8 w-full fees-table">
                                <table class="min-w-full bg-white" style="width:100%"> 
                                    <thead class="bg-gray-800 text-white static">
                                        <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                            <th class="text-left px-2" style="width:30%">Posting Account</th>
                                            <th class="text-left px-2" style="width:40%">Description</th>
                                            <th class="text-left px-2">Debit</th>
                                            <th class="text-left px-2">Credit</th>
                                            <th class="text-left px-2"></th>
                                            <th class="text-left px-2"></th>
                                        </tr>
                                    </thead>
                                    <tbody class="">
                                        <tr v-for="(led, index) in ledgers" :key="index">
        
                                            <td class="text-left border border-black">
                                                <select v-model="led.account" ref="ledgerSelect" @change="setLedgerID" onfocus="this.selectedIndex = -1;" class="bg-white text-left pl-2 px-2 w-full">
                                                    <option v-for="ledger in ledgersArray" :key="ledger.ledger_id" :value="ledger.ledger_id">{{ ledger.ledger_code }} - {{ ledger.ledger_name }}</option>
                                                </select>
                                            </td>
                                            <td class="text-left border border-black"><input type="text" class="text-left w-full" v-model="led.details" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.debit" /></td>
                                            <td class="text-left border border-black"><input type="number" class="text-left w-full" v-model="led.credit" /></td>
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
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createJournal">Save</button>
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
                                <th class="text-left py-3 px-4">Journal No</th>
                                <th class="text-left py-3 px-4">Date</th>
                                <th class="text-left py-3 px-4">Description</th>
                                <th class="text-left py-3 px-4">Amount</th>
                                <th class="text-left py-3 px-4">Done By</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(jnl,index) in journalsList" :key="jnl.journal_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ jnl.journal_no }}</td>
                            <td class="text-left py-3 px-4">{{ jnl.issue_date }}</td>
                            <td class="text-left py-3 px-4">{{ jnl.description }}</td>
                            <td class="text-left py-3 px-4">{{ Number(jnl.total_amount).toLocaleString() }}</td>
                            <td class="text-left py-3 px-4">{{ jnl.done_by }}</td>
                            <td>
                                <div class="flex">
                                    <div class="">
                                        <button @click="removeJournal(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="journalCount"
                    :currentPage="currentPage"
                    :result="journalArrLen"
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
import SideBarFA from '@/components/SideBarFA.vue'
import Modal from '@/components/Modal.vue'
import MyPagination from '@/components/MyPagination.vue'
import Datepicker from 'vuejs3-datepicker';


export default{
    name: 'ManagerView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Financial Accounts/ Journals',
            companyID: "",
            description: "",
            journal_date: null,
            txn_type: "",
            description_search: "",
            date_from: null,
            date_to: null,
            journal_no_search: "",
            min_amount_search: "",
            max_amount_search: "",
            isModalVisible: false,
            isEditing: false,
            isSearching: false,
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            showOptions: false,
            currentPage: 1,
            pageCount: 0,
            journalID: "",
            journalNo: "",
            journalsList: [],
            journalDetails: [],
            journalResults: [],
            journalArr: [],
            journalArrLen: [],
            journalCount: 0,
            clearButton: true,
            ledgersArray: [],
            ledgerID: "",
            ledgerName: "",
            ledgers: [
                { account: null, details: null, debit: null, credit: null }
            ],
            debit_totals: 0,
            credit_totals: 0,
            done_by: "user",
        }
    },
    components:{
        NavBar,
        SideBarFA,
        Modal,
        Loader,
        MyPagination,
        Datepicker
    },
    computed:{
        journalDebitTotal(){
            this.debit_totals = 0;
            if(this.ledgers.length > 1 && (this.ledgers[0].debit != null || this.ledgers[0].credit != null) ){
                for(let i=0; i < this.ledgers.length; i++){
                    if(this.ledgers[i].debit == null){
                        this.ledgers[i].debit = 0;                       
                    }
                    else{
                       this.debit_totals +=  this.ledgers[i].debit;
                    }
                }
                return this.debit_totals;
            }
        },
        journalCreditTotal(){
            this.credit_totals = 0;
            if(this.ledgers.length > 1 && (this.ledgers[0].debit != null || this.ledgers[0].credit != null) ){
                for(let i=0; i < this.ledgers.length; i++){
                    if(this.ledgers[i].credit == null){
                        this.ledgers[i].credit = 0;                       
                    }
                    else{
                       this.credit_totals +=  this.ledgers[i].credit;
                    }
                }
                return this.credit_totals;
            }
        },
        journalTotal(){
            if(this.journalDebitTotal == this.journalCreditTotal){
                return this.journalDebitTotal;
            }
            else{
                return 0;
            }
            
        }

    },
    methods:{
        addRow() {
            this.ledgers.push({account: null, details: null, debit: null, credit: null});

        },
        removeRow(){
            if(this.ledgers.length > 1){
                let selectedLedger = arguments[0];
                this.ledgers.splice(selectedLedger, 1);
                
            }else{
                this.ledgers = [{account: null, details: null, debit: null, credit: null}];
      
            }
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            const year = date.getFullYear().toString()
            const month = ('0' + (date.getMonth() + 1)).slice(-2);
            const day = ('0' + date.getDate()).slice(-2);
            return `${year}-${month}-${day}`;
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
                
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        setLedgerID(){
            this.ledgerID = "";
            if(this.$refs.ledgerSelect.selectedIndex > 0){
                let selectedLedger = this.$refs.ledgerSelect.selectedIndex - 1;
                this.ledgerID = this.ledgersArray[selectedLedger].ledger_id;
                this.ledgerName = this.ledgersArray[selectedLedger].ledger_name;
            }
        },
        createJournal(){
            this.showLoader();
            
            if(this.description === '' || this.journal_date === '' || this.ledgers[0].account === null
                 || this.ledgers.length < 2 || this.journalTotal === 0 || this.journalTotal === undefined){
                this.$toast.error("Please Enter Journal Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{

                this.txn_type = "JNL";
                let formData = {
                    company: this.companyID,
                    description: this.description,
                    txn_type: this.txn_type,
                    issue_date: this.formatDate(this.journal_date),
                    total_amount: this.journalTotal,
                    done_by: this.done_by,
                }

                this.axios
                .post("api/v1/create-journal/", formData)
                .then((response)=>{
                    this.journalDetails = response.data;
                    this.$toast.success("Journal Added Succesfully",{
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
                    this.hideLoader();
                })
                .finally(()=>{
                    for(let i=0; i<this.ledgers.length; i++){
                        let formData = new FormData();
                        formData.append('journal', this.journalDetails.journal_id);
                        formData.append('date',this.formatDate(this.journal_date));
                        formData.append('txn_type',this.journalDetails.txn_type);
                        formData.append('posting_account',this.ledgers[i].account);
                        formData.append('debit_amount',this.ledgers[i].debit);
                        formData.append('credit_amount',this.ledgers[i].credit);
                        if(this.ledgers[i].details != null){
                            formData.append('description',this.ledgers[i].details);
                        }else{
                            formData.append('description',this.journalDetails.description);
                        }
                        formData.append('company',this.companyID);

                        console.log("FormDDAAATAAA", formData);

                        this.axios
                        .post("api/v1/create-journal-entry/", formData)
                        .then((response)=>{
                            
                        })
                        .catch((error)=>{
                            console.log(error.message);
                        })
                    }
                   this.hideLoader();
                   this.journal_date = "";
                   this.description = "";
                   this.journalCreditTotal = 0;
                   this.journalDebitTotal = 0;
                   this.journalTotal = 0;
                   this.ledgers = [{account: null, details: null, debit: null, credit: null}];
                   this.$store.commit('reloadingPage');
                })
            }
        },
        searchJournals(){
            this.txn_type = 'JNL';
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = new FormData();
            formData.append('txn_type', this.txn_type);
            formData.append('description', this.description_search);
            if((this.date_from !=null) && (typeof(this.date_from) == "object")){
                formData.append('date_from', this.formatDate(this.date_from));
            }else{
                this.date_from = "";
                formData.append('date_from', this.date_from);
            }   
            if((this.date_to !=null) && (typeof(this.date_to) == "object")){
                formData.append('date_to', this.formatDate(this.date_to));
            }else{
                this.date_to = "";
                formData.append('date_to', this.date_to);
            } 
            formData.append('journal_no', this.journal_no_search);
            formData.append('min_amount', this.min_amount_search);
            formData.append('max_amount', this.max_amount_search);
            formData.append('company_id', this.companyID);                 

            this.axios
            .post(`api/v1/journals-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.journalsList = response.data.results;
                this.journalResults = response.data;
                this.journalArrLen = this.journalsList.length;
                this.journalCount = this.journalResults.count;
                this.pageCount = Math.ceil(this.journalCount / 10);

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
        removeJournal() {
            let selectedItem = arguments[0];
            this.journalID = this.journalsList[selectedItem].journal_id;
            this.journalNo = this.journalsList[selectedItem].journal_no;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.journalNo}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete Journal!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        company: this.companyID,
                        journal: this.journalID
                    }
                    this.axios
                    .post("api/v1/delete-journal/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Journal removed succesfully!", {
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
                    this.$swal(`${this.journalNo} has not been deleted!`);
                }
            });
        },
        showModal(){
            this.scrollToTop();
            this.fetchLedgers();
            this.ledgers = [{ account: null, details: null, debit: null, credit: null }];
            if(this.isEditing == false){
                this.journal_date = "";
                this.description = "";
                this.ledgers = [{ account: null, details: null, debit: null, credit: null }];
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
            
            this.searchJournals();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchJournals();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchJournals();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchJournals();
            this.scrollToTop();
        },
        showDropdown(){
            this.showOptions = !this.showOptions;
        },
        exportJournalsPDF(){
            this.txn_type = 'JNL';
            this.showLoader();
            let formData = new FormData();
            formData.append('txn_type', this.txn_type);
            formData.append('description', this.description_search);
            if((this.date_from !=null) && (typeof(this.date_from) == "object")){
                formData.append('date_from', this.formatDate(this.date_from));
            }else{
                this.date_from = "";
                formData.append('date_from', this.date_from);
            }   
            if((this.date_to !=null) && (typeof(this.date_to) == "object")){
                formData.append('date_to', this.formatDate(this.date_to));
            }else{
                this.date_to = "";
                formData.append('date_to', this.date_to);
            } 
            formData.append('journal_no', this.journal_no_search);
            formData.append('min_amount', this.min_amount_search);
            formData.append('max_amount', this.max_amount_search);
            formData.append('company_id', this.companyID); 

            this.axios
            .post("api/v1/export-journals-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Journals.pdf');
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
        exportJournalsExcel(){
            this.showLoader();
            this.txn_type = 'JNL';
            let formData = new FormData();
            formData.append('txn_type', this.txn_type);
            formData.append('description', this.description_search);
            if((this.date_from !=null) && (typeof(this.date_from) == "object")){
                formData.append('date_from', this.formatDate(this.date_from));
            }else{
                this.date_from = "";
                formData.append('date_from', this.date_from);
            }   
            if((this.date_to !=null) && (typeof(this.date_to) == "object")){
                formData.append('date_to', this.formatDate(this.date_to));
            }else{
                this.date_to = "";
                formData.append('date_to', this.date_to);
            } 
            formData.append('journal_no', this.journal_no_search);
            formData.append('min_amount', this.min_amount_search);
            formData.append('max_amount', this.max_amount_search);
            formData.append('company_id', this.companyID);

            this.axios
            .post("api/v1/export-journals-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Journals.xls');
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
        exportJournalsCSV(){
            this.showLoader();
            this.txn_type = 'JNL';
            let formData = new FormData();
            formData.append('txn_type', this.txn_type);
            formData.append('description', this.description_search);
            if((this.date_from !=null) && (typeof(this.date_from) == "object")){
                formData.append('date_from', this.formatDate(this.date_from));
            }else{
                this.date_from = "";
                formData.append('date_from', this.date_from);
            }   
            if((this.date_to !=null) && (typeof(this.date_to) == "object")){
                formData.append('date_to', this.formatDate(this.date_to));
            }else{
                this.date_to = "";
                formData.append('date_to', this.date_to);
            } 
            formData.append('journal_no', this.journal_no_search);
            formData.append('min_amount', this.min_amount_search);
            formData.append('max_amount', this.max_amount_search);
            formData.append('company_id', this.companyID);

            this.axios
            .post("api/v1/export-journals-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Journals.csv');
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
        this.companyID = localStorage.getItem("company_id")
        this.searchJournals();
    }
}
</script>

<style>
.main-content{
  z-index: -1;
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
em{
  color: red;
}
.vuejs3-datepicker__value{
    padding: 4px 4px !important;
    min-width: 210px;
    border-color: gray;
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
.fees-table{
    min-height: 25vh;
    max-height: 50vh;
    overflow-y: scroll;
    overflow-x: scroll;
}
</style>