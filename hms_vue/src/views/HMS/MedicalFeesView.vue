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
            <h2 class="text-center font-bold">Medical Fees & Charges</h2>
            <div class="md:px-4 pt-4 pb-1 w-full">
                <div class="mb-4 flex items-end h-24 border-b-2 border-gray-300 mb-6 pb-6">
                    <div class="basis-1/4 pl-3">
                        <button class="rounded bg-green-400 text-white px-3 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Fees</button>
                    </div>
                    <div class="basis-3/4">
                        <div class="flex items-end">
                            <div class="basis-1/2 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg" name="name" id="" placeholder="Name..." v-model="fees_name_search"  @keyup.enter="searchMedicalFees">
                            </div>
                        </div>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchMedicalFees"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportMedicalFeesPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportMedicalFeesExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportMedicalFeesCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                        </div>
                    </div>
                </div>
                <!-- MODAL component for adding a new medical fees -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Medical Fees Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                    <div class="flex mb-6">
                        <div class="basis-1/2 mx-12">
                            <label for="">Name<em>*</em></label><br />
                            <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="fees_name">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2 mx-12"  v-if="isEditing">
                            <label for="">Posting Account<em>*</em></label><br />
                            <select name="ledgerUpdate" ref="ledgerUpdateSelect" id="selectUpdateledger" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUpdateLedgerID" onfocus="this.selectedIndex = -1;" v-model="ledgerEditing">
                                <option v-for="led in ledgersArray" :key="led.ledger_id" :value="(led.ledger_code+'-'+led.ledger_name)" :label="(led.ledger_code+'-'+led.ledger_name)" :selected="((led.ledger_code+'-'+led.ledger_name)===ledgerEditing)">{{led.ledger_code}} - {{led.ledger_name}}</option> 
                            </select>
                        </div>
                        <div class="basis-1/2 mx-12" v-else>    
                            <label for="">Posting Account<em>*</em></label><br />
                            <select name="ledger" ref="ledgerSelect" id="selectLedger" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setLedgerID" onfocus="this.selectedIndex = -1;" v-model="posting_account">
                                <option value="" disabled selected>---Select Posting Account---</option> 
                                <option v-for="led in ledgersArray">{{led.ledger_code}} - {{led.ledger_name}}</option> 
                            </select>
                        </div>
                        <div class="basis-1/2">
                        </div>
                    </div>
                    <div class="flex mb-6">
                        <div class="basis-1/2 mx-12">
                            <label for="">Default Amount<em>*</em></label><br />
                            <input type="number" name="" id="" class="rounded border border-gray-600 text-lg pl-2" v-model="fees_amount">
                        </div>
                        <div class="basis-1/2">

                        </div>
                    </div>
                    <div class="text-center" v-if="isEditing">
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateMedicalFees(index)">Update</button>
                    </div>
                    <div class="text-center" v-else>
                        <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createMedicalFees">Save</button>
                    </div>

                    </form>
                    </template>
                    <template v-slot:footer> We Value Your Partnership </template>
                </Modal>

                <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                    <table class="min-w-full bg-white"> 
                        <thead class="bg-gray-800 text-white">
                            <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                <th>#</th>
                                <th class="text-left py-3 px-4">Name</th>
                                <th class="text-left py-3 px-4">Posting Account</th>
                                <th class="text-center py-3 px-4">Default Amount</th>
                                <th class="text-left py-3 px-4">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(fee,index) in feesList" :key="fee.fees_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-3 px-4">{{ fee.fees_name }}</td>
                            <td class="text-left py-3 px-4">{{ fee.posting_account_name }}</td>
                            <td class="text-center py-3 px-4">{{ Number(fee.fees_amount).toLocaleString() }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/2">
                                        <button @click="editMedicalFee(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/2">
                                        <button @click="removeMedicalFee(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>   
                </div>
                <div class="pagination row-span-2">
                    <MyPagination 
                    :count="feesCount"
                    :currentPage="currentPage"
                    :result="feesArrLen"
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


export default{
    name: 'MedicalFeesView',
    props:['scrollToTop','loader','showLoader','hideLoader',],
    data(){
        return{
            title: 'Hospital Management/ Medical Fees',
            isModalVisible: false,
            fees_name: "",
            posting_account: "",
            fees_amount: 0,
            fees_name_search: "",
            isEditing: false,
            isSearching: false,
            feesID: "",
            feesName: "",
            hospitalID: "",
            currentPage: 1,
            feesCount: 0,
            feesArrLen: 0,
            feesResults: [],
            feesList: [],
            feesDetails: [],
            pageCount: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            showOptions: false,
            ledgersArray: [],
            ledgerID: "",
            ledgerUpdateID: "",
            ledgerName: "",
            ledgerUpdateName: "",
            ledgerEditing: "",
            ledger_type: "Income"
        }
    },
    components: {
        NavBar,
        SideBarHMS,
        Modal,
        MyPagination,
        Loader,
    },

    methods:{
        fetchLedgers(){
            this.ledgersArray = [];
            let formData = {
                company: this.hospitalID,
                ledger_type: this.ledger_type
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
        showModal(){
            this.scrollToTop();
            if(this.isEditing == false){
             this.fees_name = "";
             this.fees_amount = "";
             this.posting_account = "";
            }
            this.isModalVisible = !this.isModalVisible;
            this.fetchLedgers();
        },
        closeModal(){
            this.isModalVisible = false;
            this.isEditing = false;
        },

        createMedicalFees(){
            this.showLoader();
            if(this.fees_name === '' || this.posting_account === ""){
                this.$toast.error("Please Enter Medical Fees Details",{
                    duration: 3000,
                    dismissible: true
                })
            }
            else{
                let new_fees_name = "";
                let x = this.fees_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_fees_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }
                let formData = {
                    fee_name: new_fees_name,
                    posting_account: this.ledgerID,
                    default_amount: this.fees_amount,
                    hospital: this.hospitalID
                }
                this.axios
                .post("api/v1/create-medical-fee/", formData)
                .then((response)=>{
                    this.$toast.success("Fee Successfully Added",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .catch((error)=>{
                    console.log(error.message);
                })
                .finally(()=>{
                    this.hideLoader();
                    this.fees_name = "";
                    this.posting_account = "";
                    this.fees_amount = "";
                })
            }
        },
        editMedicalFee(){
            this.isEditing = true;
            let selectedFee = arguments[0];
            this.feesID = this.feesList[selectedFee].fees_id;
            this.fees_name = this.feesList[selectedFee].fees_name;
            this.ledgerID = this.feesList[selectedFee].posting_account_id;
            this.ledgerEditing = this.feesList[selectedFee].posting_account_code+ '-'+this.feesList[selectedFee].posting_account_name ;
            this.fees_amount = this.feesList[selectedFee].fees_amount;
            this.showModal();
            this.scrollToTop();
            console.log("The edit is ",this.ledgerEditing);
        },
        updateMedicalFees(){
            this.showLoader();
            if(this.fees_name === '' || this.ledgerEditing === ""){
                this.$toast.error("Please Enter Medical Fees Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else{
                let new_fees_name = "";
                let x = this.fees_name.split(" ");
                for(let i=0; i<x.length; i++){
                    new_fees_name += x[i][0].toUpperCase()+ x[i].slice(1).toLowerCase() + " ";
                }

                let formData = new FormData();
                formData.append('fees', this.feesID);
                formData.append('fee_name', new_fees_name);
                formData.append('default_amount', this.fees_amount);
                if(this.ledgerUpdateID != 0){
                    formData.append('posting_account', this.ledgerUpdateID);
                }else{
                    formData.append('posting_account', this.ledgerID);
                }
                formData.append('hospital', this.hospitalID);


                this.axios
                .put("api/v1/update-medical-fee/", formData)
                .then((response)=>{
                    this.$toast.success("Fees Succesfully Updated",{
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
        removeMedicalFee() {
            let selectedItem = arguments[0];
            this.feesID = this.feesList[selectedItem].fees_id;
            this.feesName = this.feesList[selectedItem].fees_name;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.feesName}?`,
                type: 'warning',
                showCloseButton: true,
                showCancelButton: true,
                confirmButtonText: 'Yes Delete it!',
                cancelButtonText: 'Cancel!',
                showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    let formData = {
                        fees: this.feesID,
                        hospital: this.hospitalID
                    }
                    this.axios
                    .post("api/v1/delete-medical-fee/", formData)
                    .then((response)=>{
                        this.$swal("Poof! Fee removed succesfully!", {
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
                    this.$swal(`${this.feesName} has not been deleted!`);
                }
            });
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchMedicalFees();
            this.scrollToTop();           
        },
        loadPrev(){
            if (this.currentPage <= 1){
                this.currentPage = 1;
            }else{
                this.currentPage -= 1;
            }
            
            this.searchMedicalFees();
            this.scrollToTop();
        },
        firstPage(){
            this.currentPage = 1;
            this.searchMedicalFees();
            this.scrollToTop();
        },
        lastPage(){
            this.currentPage = this.pageCount;
            this.searchMedicalFees();
            this.scrollToTop();
        },
        searchMedicalFees(){
            this.isSearching = true;
            this.showNextBtn = false;
            this.showPreviousBtn = false;
            let formData = {
                fees_name: this.fees_name_search,
                hospital_id: this.hospitalID
            }
            this.axios
            .post(`api/v1/medical-fees-search/?page=${this.currentPage}`,formData)
            .then((response)=>{
                this.feesList = response.data.results;
                this.feesResults = response.data;
                this.feesArrLen = this.feesList.length;
                this.feesCount = this.feesResults.count;
                this.pageCount = Math.ceil(this.feesCount / 10);

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
        setLedgerID(){
            this.ledgerID = "";
            if(this.$refs.ledgerSelect.selectedIndex > 0){
                let selectedLedger = this.$refs.ledgerSelect.selectedIndex - 1;
                this.ledgerID = this.ledgersArray[selectedLedger].ledger_id;
                this.ledgerName = this.ledgersArray[selectedLedger].ledger_name;
            }
        },
        setUpdateLedgerID(){
            this.ledgerUpdateID = "";
            if(this.$refs.ledgerUpdateSelect.selectedIndex >= 0){
                let selectedUpdateLedger = this.$refs.ledgerUpdateSelect.selectedIndex;
                this.ledgerUpdateID = this.ledgersArray[selectedUpdateLedger].ledger_id;
                this.ledgerUpdateName = this.ledgersArray[selectedUpdateLedger].ledger_name;

            }
        },
        exportMedicalFeesPDF(){
            this.showLoader();
            let formData = {
                fees_name: this.fees_name_search,
                hospital_id: this.hospitalID
            }
            this.axios
            .post("api/v1/export-medical-fees-pdf/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Medical Fees.pdf');
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
        exportMedicalFeesExcel(){
            this.showLoader();
            let formData = {
                fees_name: this.fees_name_search,
                hospital_id: this.hospitalID
            }
            this.axios
            .post("api/v1/export-medical-fees-excel/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Medical Fees.xls');
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
        exportMedicalFeesCSV(){
            this.showLoader();
            let formData = {
                fees_name: this.fees_name_search,
                hospital_id: this.hospitalID
            }
            this.axios
            .post("api/v1/export-medical-fees-csv/", formData, { responseType: 'blob' })
            .then((response)=>{
                if(response.status == 200){
                  const url = window.URL.createObjectURL(new Blob([response.data]));
                  const link = document.createElement('a');
                  link.href = url;
                  link.setAttribute('download', 'Medical Fees.csv');
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
        this.searchMedicalFees();
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