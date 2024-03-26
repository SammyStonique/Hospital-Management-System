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
            <div class="md:px-2 py-8 w-full">
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
                                    <select name="" ref="" id="" class="rounded border-2  border-gray-200 bg-white text-lg pl-2 pt-2 w-52"  placeholder="Gender...." v-model="gender_search">
                                        <option value="" selected disabled>Gender</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option> 
                                        <option value="Other">Other</option>
                                    </select>
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
                                <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
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
                            <div class="basis-1/3 mr-6">
                                <label for="">First Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="first_name" required>
                            </div>
                            <div class="basis-1/3 mr-6">
                                <label for="">Last Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="last_name" required>
                            </div>
                            <div class="basis-1/3 mr-3">
                                <label for="">Email<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" v-model="email" :style="{borderColor: eStyle,borderWidth: bWidth+'px' }" required><br />
                                <span v-if="watcherMsg.email" :style="{color: eStyle, fontSize:10 + 'px'}">{{watcherMsg.email}}</span>
                            </div>
                        </div>
                        <div class="flex mb-6">   
                            <div class="basis-1/3 mr-6">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 focus:outline-none w-60" placeholder="e.g 07XXXX" v-model="phone_number" :style="{borderColor: nStyle,borderWidth: bWidth+'px' }" required><br />
                                <span v-if="watcherMsg.phone_number" :style="{color: nStyle, fontSize:10 + 'px'}">{{watcherMsg.phone_number}}</span>
                            </div>
                            <div class="basis-1/3 mr-6">
                                <label for="">Birth Date<em>*</em></label><br />
                                <datepicker  placeholder="Birth Date...." v-model="birth_date" clearable :clear-button="clearButton">
                                </datepicker>
                            </div> 
                            <div class="basis-1/3 mr-3">
                                <label for="">ID Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="id_number">
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/3 mr-6">
                                <label for="">Gender<em>*</em></label><br />
                                <select name="" ref="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60"  v-model="gender">
                                  <option value="" selected disabled>---Select Gender</option>
                                  <option value="Male">Male</option>
                                  <option value="Female">Female</option> 
                                  <option value="Other">Other</option>
                                </select>
                            </div>
                            <div class="basis-1/3 mr-6">
                                <label for="">City/Town<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="city">
                            </div>
                            <div class="basis-1/3 mr-3">
                                <label for="">Country<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="country">
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Address<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="address">
                            </div>
                            <div class="basis-1/2 mr-6" v-if="!isEditing">
                                <label for=""><em></em></label><br />
                                <input type="checkbox" name="" id="" class="rounded border border-gray-600 text-lg pl-2 mr-3" @click="showVisitCreationOption">
                                <label for="">Create Visit<em></em></label>
                            </div>
                        </div>
                        <div v-if="visit_creation && !isEditing">
                            <div class="border-b border-gray-400 pb-3">
                                <p class="font-bold">Visitation Details</p>
                            </div>
                            <div class="flex mb-6 mt-6">
                                <div class="basis-1/2 mr-6">
                                    <label for="">Doctor<em>*</em></label><br />
                                    <select name="doctor" ref="doctorSelect" id="selectDoctor" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setDoctorID" onfocus="this.selectedIndex = -1;" v-model="doctor">
                                        <option value="" disabled selected>---Select Doctor---</option> 
                                        <option v-for="doct in doctorsArray">Dr. {{doct.first_name}}  {{doct.last_name}}</option> 
                                    </select>
                                </div>
                                <div class="basis-1/2">
                                    <label for="">Staff<em>*</em></label><br />
                                    <select name="user" ref="userSelect" id="selectUser" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60" @change="setUserID" onfocus="this.selectedIndex = -1;" v-model="staff">
                                        <option value="" disabled selected>---Select Staff---</option> 
                                        <option v-for="stf in staffArray">{{stf.first_name}}  {{stf.last_name}} - #{{ stf.identification_no }}</option> 
                                    </select>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="basis-1/2">
                                    <label for="">Notes<em>*</em></label><br />
                                    <textarea id="notes" name="visit_notes" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="visit_notes" rows="4" cols="50"></textarea>
                                </div>
                            </div>
                            <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8 mb-8 w-2/3 fees-table">
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
        
                                            <td class="text-left border border-black">
                                                <select v-model="fee.type" ref="feesSelect" @change="setFeesID" onfocus="this.selectedIndex = -1;" class="bg-white text-left pl-2 px-2 w-full">
                                                    <option v-for="feeType in feesArray" :key="feeType.fees_id" :value="feeType.fees_id">{{ feeType.fee_name }}</option>
                                                </select>
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
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mr-6">
                                <label for="">Email<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_email" required>
                            </div>
                            <div class="basis-1/2">
                                <label for="">Phone Number<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 text-lg pl-2 w-60" v-model="contact_person_phone_number" required>
                            </div>
                        </div>
                        <div class="text-center" v-if="isEditing && !isAddingContactPerson">
                            <button class="rounded border bg-green-400 w-42 py-2 px-4 text-white text-lg" @click="updatePatient">Update Patient</button>
                        </div>
                        <div class="text-center" v-else-if="isAddingContactPerson && isEditing">
                            <button class="rounded border bg-green-400 w-48 py-2 px-4 text-white text-lg" @click="updatePatient">Add Kin & Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createPatient">Save Patient</button>
                        </div>

                    </form>
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
                </Modal>
                <!-- MODAL component for importing patients -->
                <Modal v-show="importModalVisible" @close="closeImportModal" :index="index">
                    <template v-slot:header> Import Patients </template>
                    <template v-slot:body>
                    
                    <form action="" @submit.prevent="importPatientsExcel" enctype="multipart/form-data" class="import-form">
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
                                        <th class="text-left py-3 px-2">F. Name</th>
                                        <th class="text-left py-3 px-2">L. Name</th>
                                        <th class="text-left py-3 px-2">Email</th>
                                        <th class="text-left py-3 px-2">ID No.</th>
                                        <th class="text-left py-3 px-2">Phone No</th>
                                        <th class="text-left py-3 px-2">DOB</th>
                                        <th class="text-left py-3 px-2">City</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(pat,index) in excelPatList" :key="pat.patient_id" class="even:bg-gray-100">
                                        <td>{{ index + 1 }}.</td>
                                        <td class="text-left">{{ pat.first_name }}</td>
                                        <td class="text-left">{{ pat.last_name }}</td>
                                        <td class="text-left">{{ pat.email }}</td>
                                        <td class="text-left">{{ pat.id_number }}</td>
                                        <td class="text-left">{{ pat.phone_number }}</td>
                                        <td class="text-left">{{ pat.birth_date }}</td>
                                        <td class="text-left">{{ pat.city }}</td>
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
                <!-- MODAL component for showing patient statement -->
                <Modal v-show="statementModalVisible" @close="closeStatementModal" :index="index">
                    <template v-slot:header> Patient Statement Details </template>
                    <template v-slot:body>
                        <div class="statements-table">
                            <table class="w-full mb-6">
                                <tr>
                                    <td class="font-bold">Patient Name:</td>
                                    <td> {{ first_name }} {{ last_name }}</td>
                                    <td></td>
                                    <td></td>
                                    <td class="font-bold">Patient Code:</td>
                                    <td>{{ patient_code }}</td>
                                </tr>
                                <tr>
                                    <td class="font-bold">ID Number:</td>
                                    <td>{{ id_number }}</td>
                                    <td></td>
                                    <td></td>
                                    <td class="font-bold">Phone Number:</td>
                                    <td>{{ phone_number }}</td>
                                </tr>
                                <tr>
                                    <td class="font-bold">Start Date:</td>
                                    <td>{{ start_date }}</td>
                                    <td></td>
                                    <td></td>
                                    <td class="font-bold">Email:</td>
                                    <td>{{ email }}</td>
                                </tr>
                            </table>
                            <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8 statement-table">
                                <table class="min-w-full bg-white"> 
                                    <thead class="bg-gray-800 text-white">
                                        <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                            <th>#</th>
                                            <th class="text-left py-2 px-2">Date</th>
                                            <th class="text-left py-2 px-2">Ref No.</th>
                                            <th class="text-left py-2 px-2">Txn No.</th>
                                            <th class="text-left py-2 px-2">Details</th>
                                            <th class="text-left py-2 px-2">Charges</th>
                                            <th class="text-left py-2 px-2">Payments</th>
                                            <th class="text-left py-2 px-2">Balance</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    
                                    <tr v-for="(jnl,index) in jnlArray" :key="jnl.journal_entry_id" class="even:bg-gray-100">
                                        <td></td>
                                        <td class="text-left">{{ jnl.date }}</td>
                                        <td class="text-left">{{ jnl.reference_no }}</td>
                                        <td class="text-left">{{ jnl.journal_no }}</td>
                                        <td class="text-left">{{ jnl.description }}</td>
                                        <td class="text-left" v-if="jnl.debit_amount != 0">{{ Number(jnl.debit_amount).toLocaleString() }}</td>
                                        <td class="text-left" v-else>-</td>
                                        <td class="text-left" v-if="jnl.credit_amount != 0">{{ Number(jnl.credit_amount).toLocaleString() }}</td>
                                        <td class="text-left" v-else>-</td>
                                        <td class="text-left">{{ Number(jnl.running_balance).toLocaleString() }}</td>
                                       
                                    </tr>
                                    </tbody>
                                </table>   
                            </div>
                        </div>
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
                </Modal>
                <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                    <table class="min-w-full bg-white"> 
                        <thead class="bg-gray-800 text-white">
                            <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                                <th>#</th>
                                <th class="text-left py-3 px-2">Code</th>
                                <th class="text-left py-3 px-2">Name</th>
                                <th class="text-left py-3 px-2">Email</th>
                                <th class="text-left py-3 px-2">ID No</th>
                                <th class="text-left py-3 px-2">Phone No</th>
                                <th class="text-left py-3 px-2">Birth Date</th>
                                <th class="text-left py-3 px-2">City</th>
                                <th class="text-left py-3 px-2">Contact Person</th>
                                <th class="text-left py-3 px-2">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                        <tr v-for="(pat,index) in patientList" :key="pat.patient_id" class="even:bg-gray-100">
                            <td>{{ index + 1 }}.</td>
                            <td class="text-left py-2">{{ pat.patient_code }}</td>
                            <td class="text-left py-2">{{ pat.first_name }} {{ pat.last_name }}</td>
                            <td class="text-left py-2">{{ pat.email }}</td>
                            <td class="text-left py-2">{{ pat.id_number }}</td>
                            <td class="text-left py-2">{{ pat.phone_number }}</td>
                            <td class="text-left py-2">{{ pat.birth_date }}</td>
                            <td class="text-left py-2">{{ pat.city }}</td>
                            <td class="text-left py-2">{{ pat.emergency_contact_person_name }}</td>
                            <td>
                                <div class="flex">
                                    <div class="basis-1/3">
                                        <button @click="editPatient(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                    </div>
                                    <div class="basis-1/3">
                                        <button @click="showStatementModal(index)"><i class="fa fa-file-pdf-o" aria-hidden="true" title="Statement"></i></button>
                                    </div>
                                    <div class="basis-1/3">
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
        patient_code: "",
        first_name: "",
        last_name: "",
        birth_date: null,
        city: "",
        gender: "",
        phone_number: "",
        id_number: "",
        email: "",
        country: "",
        address: "",
        first_name_search: "",
        last_name_search: "",
        id_number_search: "",
        phone_number_search: "",
        gender_search: "",
        birth_date_search: null,
        patientModalVisible: false,
        statementModalVisible:false,
        importModalVisible: false,
        isEditing: false,
        isSearching: false,
        isAddingContactPerson: false,
        pageCount: 0,
        showNextBtn: false,
        showPreviousBtn: false,
        showOptions: false,
        currentPage: 1,
        pageCount: 0,
        patientID: "",
        patientName: "",
        patientLedger: "",
        patientList: [],
        journalsArray: [],
        jnlArray: [],
        patientDetails: [],
        emergencyContactDetails: [],
        emergencyContactID: "",
        patientResults: [],
        patientArr: [],
        patientArrLen: [],
        patientCount: 0,
        patientEditing: "",
        clearButton: true,
        contact_personID: "",
        contact_person_first_name: "",
        contact_person_last_name: "",
        contact_person_email: "",
        contact_person_phone_number: "",
        doctorsArray : [],
        doctorID: "",
        staffID: "",
        feesID: "",
        feesArray: [],
        fees_amount: 0,
        staffArray: [],
        watcherMsg: [],
        eStyle: null, nStyle:null, bWidth: null,
        excelPatList: [],
        excel_file: "",
        filePath: "",
        axiosError: [],
        visit_creation: false,
        visitation_fees: "",
        visit_notes: "",
        fees: [
        {itemIndex:0, type: null, amount: null, fee_name: null, fee_ledger: null}
        ],
        itemInd: 0,
        txn_type: "",
        journalEntryArr: [],
        contra: 0,
        invoice_description: [],
        invDescr: "",
        invoice_totals: 0,
        journalDetails: [],
        today_date: new Date()
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
    computed:{
        feesAmount(){
            return this.fees_amount;
        }
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
            }
        },     
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
        onFileChange(e){
            this.excel_file = e.target.files[0];
            this.filePath = "C:\\fakepath\\"+ this.excel_file.name; 
        },
        onFileAdd(item){
            this.excel_file = item.file;
            this.filePath = "C:\\fakepath\\"+ this.excel_file.name; 
            this.displayExcelData();
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
        fetchFees(){
            this.feesArray = [];
            let formData = {
                hospital: this.hospitalID,
            }
            this.axios
            .post("api/v1/get-medical-fees/", formData)
            .then((response)=>{
                this.feesArray = response.data;
                
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
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        fetchJournals(patientID){
            this.journalsArray = [];
            let formData = {
                company: this.hospitalID,
                patient: patientID
            }
            this.axios
            .post("api/v1/ledger-journal-entries-search/", formData)
            .then((response)=>{
                this.jnlArray = [];
                let running_balance = 0;
                this.journalsArray = response.data.results;
                for(let i=0; i<this.journalsArray.length; i++){
                    if(this.journalsArray[i].debit_amount != 0){
                        running_balance += this.journalsArray[i].debit_amount;
                        this.journalsArray[i]['running_balance'] = running_balance;
                        this.jnlArray.push(this.journalsArray[i])
                    }
                    else if(this.journalsArray[i].credit_amount != 0){
                        running_balance -= this.journalsArray[i].credit_amount;
                        this.journalsArray[i]['running_balance'] = running_balance;
                        this.jnlArray.push(this.journalsArray[i])
                    }
                }
                console.log("The jnlArray consists of ",this.jnlArray);
            })
            .catch((error)=>{
            console.log(error.message)
            })
            .finally(()=>{
            
            })
        },
        setDoctorID(){
            this.doctorID = "";
            if(this.$refs.doctorSelect.selectedIndex > 0){
                let selectedDoctor = this.$refs.doctorSelect.selectedIndex - 1;
                this.doctorID = this.doctorsArray[selectedDoctor].user;
            }
        },
        setUserID(){
            this.userID = "";
            if(this.$refs.userSelect.selectedIndex > 0){
                this.selectedDep = this.$refs.userSelect.selectedIndex - 1;
                this.userID = this.staffArray[this.selectedDep].user_id;
            }
        },
        setFeesID(){
            this.feesID = "";
            if(this.$refs.feesSelect[this.itemInd].selectedIndex >= 0){
                let selectedFee = this.$refs.feesSelect[this.itemInd].selectedIndex;
                this.feesID = this.feesArray[selectedFee].fees_id;
                this.fees[this.itemInd].fee_ledger = this.feesArray[selectedFee].posting_account;
                this.fees[this.itemInd].fee_name = this.feesArray[selectedFee].fee_name;
                this.fees[this.itemInd].amount = this.feesArray[selectedFee].default_amount;
            }
        },
        createPatient(){
            this.axiosError = [];
            this.showLoader();
            if(this.first_name === '' || this.last_name === '' || this.email === '' || this.birth_date === '' || this.city === '' || this.gender === ''
                 || this.phone_number === '' || this.id_number === '' || this.address === '' || this.country === '' || this.contact_person_first_name === ''
                 || this.contact_person_last_name === '' || this.contact_person_email === '' || this.contact_person_phone_number === ''){
                this.$toast.error("Please Enter Patient Details",{
                    duration: 3000,
                    dismissible: true
                })
                this.hideLoader();
            }
            else if(this.visit_creation && this.fees[0].type != null && this.fees[0].amount != null && this.visit_notes && ((this.staff != '' || this.staff != null) || (this.doctor != ''|| this.doctor != null))){
                this.txn_type = "INV";
                this.invoice_description = [];
                for(let i=0; i<this.fees.length; i++){
                    if(this.fees[i].amount != null){
                        this.invoice_totals += Number(this.fees[i].amount);
                        this.invoice_description.push(this.fees[i].fee_name +" for "+this.first_name+" "+this.last_name);
                        let jnlEntry1 ={
                            "date": this.formatDate(this.today_date),
                            "description": this.fees[i].fee_name +" for "+this.first_name+" "+this.last_name,
                            "txn_type": this.txn_type,
                            "posting_account": this.patientLedger,
                            "debit_amount": this.fees[i].amount,
                            "credit_amount": this.contra,
                        }
                        let jnlEntry2 = {
                            "date": this.formatDate(this.today_date),
                            "description": this.fees[i].fee_name +" for "+this.first_name+" "+this.last_name,
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
                    contact_first_name: this.contact_person_first_name,
                    contact_last_name: this.contact_person_last_name,
                    contact_email: this.contact_person_email,
                    contact_phone_number: this.contact_person_phone_number,
                    patient: this.first_name + " "+ this.last_name,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    birth_date: this.formatDate(this.birth_date),
                    phone_number: this.phone_number,
                    city: this.city,
                    gender: this.gender,
                    id_number: this.id_number,
                    address: this.address,
                    country: this.country,
                    doctor: this.doctorID,
                    staff: this.userID,
                    visit_notes: this.visit_notes,
                    company: this.hospitalID,
                    client: this.first_name+" "+this.last_name,
                    description: this.invDescr,
                    txn_type: this.txn_type,
                    issue_date: this.formatDate(this.today_date),
                    total_amount: this.invoice_totals,
                    journal_entry_array: this.journalEntryArr,
                }
                this.axios
                .post("api/v1/create-patient-with-visit/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.city = "";
                        this.gender = "",
                        this.address = "";
                        this.country = "";
                        this.contact_person_first_name = "";
                        this.contact_person_last_name = "";
                        this.contact_person_email = "";
                        this.contact_person_phone_number = "";
                        this.visit_notes = "";
                        this.visit_creation = false;
                        this.fees = [{itemIndex:0, type: null, amount: null , fee_name: null, fee_ledger: null}];
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient",{
                            duration: 3000,
                            dismissible: true
                        })
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .finally(()=>{

                })    
            }
            else if(this.visit_creation && this.visit_notes && ((this.staff != '' || this.staff != null) || (this.doctor != ''|| this.doctor != null)) && this.fees[0].type == null && this.fees[0].amount == null){
                let formData = {
                    hospital: this.hospitalID,
                    contact_first_name: this.contact_person_first_name,
                    contact_last_name: this.contact_person_last_name,
                    contact_email: this.contact_person_email,
                    contact_phone_number: this.contact_person_phone_number,
                    patient: this.first_name + " "+ this.last_name,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    birth_date: this.formatDate(this.birth_date),
                    phone_number: this.phone_number,
                    city: this.city,
                    gender: this.gender,
                    id_number: this.id_number,
                    address: this.address,
                    country: this.country,
                    doctor: this.doctorID,
                    staff: this.userID,
                    visit_notes: this.visit_notes,
                    issue_date: this.formatDate(this.today_date)
                }
                this.axios
                .post("api/v1/create-patient-with-visit/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.city = "";
                        this.gender = "",
                        this.address = "";
                        this.country = "";
                        this.contact_person_first_name = "";
                        this.contact_person_last_name = "";
                        this.contact_person_email = "";
                        this.contact_person_phone_number = "";
                        this.visit_notes = "";
                        this.visit_creation = false;
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient",{
                            duration: 3000,
                            dismissible: true
                        })
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient",{
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
                    contact_first_name: this.contact_person_first_name,
                    contact_last_name: this.contact_person_last_name,
                    contact_email: this.contact_person_email,
                    contact_phone_number: this.contact_person_phone_number,
                    patient: this.first_name + " "+ this.last_name,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    birth_date: this.formatDate(this.birth_date),
                    phone_number: this.phone_number,
                    city: this.city,
                    gender: this.gender,
                    id_number: this.id_number,
                    address: this.address,
                    country: this.country,
                }
                this.axios
                .post("api/v1/create-patient-with-visit/", formData)
                .then((response)=>{
                    console.log(response.data);
                    if (response.status == 200){
                        this.$toast.success("Patient Added Succesfully",{
                            duration: 3000,
                            dismissible: true
                        })
                        this.first_name = "";
                        this.last_name = "";
                        this.email = "";
                        this.birth_date = "";
                        this.id_number = "";
                        this.phone_number = "";
                        this.city = "";
                        this.gender = "",
                        this.address = "";
                        this.country = "";
                        this.contact_person_first_name = "";
                        this.contact_person_last_name = "";
                        this.contact_person_email = "";
                        this.contact_person_phone_number = "";
                        this.hideLoader();
                        this.closeModal();
                        this.$store.commit('reloadingPage');
                    }
                    else{
                        this.$toast.error("Error Adding Patient",{
                            duration: 3000,
                            dismissible: true
                        })
                    }
                    
                })
                .catch((error)=>{
                    console.log(error.message);
                    this.$toast.error("Error Adding Patient",{
                        duration: 3000,
                        dismissible: true
                    })
                })
                .finally(()=>{
                    
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
            formData.append('gender', this.gender_search);
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
        removePatient() {
            let selectedItem = arguments[0];
            this.patientID = this.patientList[selectedItem].patient_id;
            this.contact_personID = this.patientList[selectedItem].emergency_contact_person_id;
            this.patientName = this.patientList[selectedItem].first_name + " " +this.patientList[selectedItem].last_name ;
            this.$swal({
                title: "Are you sure?",
                text: `Do you wish to delete ${this.patientName}?`,
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
            this.fees = [{itemIndex:0, type: null, amount: null , fee_name: null, fee_ledger: null}];
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
                this.contact_person_email = "";
                this.contact_person_first_name = "";
                this.contact_person_last_name = "";
                this.contact_person_phone_number = "";
            }
            this.patientModalVisible = !this.patientModalVisible;
        },
        showStatementModal(){
            let selectedPatient = arguments[0];
            this.patientID = this.patientList[selectedPatient].patient_id;
            this.first_name = this.patientList[selectedPatient].first_name;
            this.last_name = this.patientList[selectedPatient].last_name;
            this.patient_code = this.patientList[selectedPatient].patient_code;
            this.email = this.patientList[selectedPatient].email;
            this.id_number = this.patientList[selectedPatient].id_number;
            this.phone_number = this.patientList[selectedPatient].phone_number;
            this.start_date = this.formatDate(this.patientList[selectedPatient].start_date);
            this.fetchJournals(this.patientID);
            this.scrollToTop();
            this.statementModalVisible = !this.statementModalVisible;
        },
        showImportModal(){
            this.showOptions = false;
            this.importModalVisible = ! this.importModalVisible;
            this.scrollToTop();
        },
        showVisitCreationOption(){
            this.visit_creation = !this.visit_creation;
            this.fetchDoctors();
            this.fetchStaff();
            this.fetchFees();
        },
        closeModal(){
            this.patientModalVisible = false;
            this.isEditing = false;
        },
        closeImportModal(){
            this.importModalVisible = false;
        },
        closeStatementModal(){
            this.statementModalVisible = false;
        },
        loadNext(){
            if(this.currentPage >= this.pageCount){
                this.currentPage = this.pageCount;
            }else if(this.currentPage < this.pageCount){
                this.currentPage += 1;
            }
            
            this.searchPatients();
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
    min-height: 20vh;
    max-height: 20vh;
    overflow-y: scroll;
    overflow-x: scroll;
}
.statements-table{
    min-width: 70vw;
}
.statement-table{
    min-height: 50vh;
}
</style>