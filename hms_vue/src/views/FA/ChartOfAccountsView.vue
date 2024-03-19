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
          <h2 class="text-center font-bold">Chart Of Accounts</h2>
          <div class="md:px-8 py-8 w-full">
            <div class="mb-4 flex items-end h-24 border-b-2 border-gray-300 mb-6 pb-6">
                    <div class="basis-1/6">
                        <button class="rounded bg-green-400 text-white px-2 py-2" @click="showModal"><i class="fa fa-plus" aria-hidden="true"></i> New Ledger</button>
                    </div>
                    <div class="basis-3/4">
                        <div class="flex items-end">
                            <div class="basis-1/3 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="code" id="" placeholder="Code..." v-model="ledger_code_search" @keyup.enter="searchLedgers">
                            </div>
                            <div class="basis-1/3 pl-3 items-center">
                                <input type="text" class="rounded pl-3 border-2 border-gray-200 text-lg w-52" name="name" id="" placeholder="Name..." v-model="ledger_name_search"  @keyup.enter="searchLedgers">
                            </div>
                            <div class="basis-1/3 pl-3 items-center">
                                <select name="" id="" class="rounded border border-gray-200 bg-white  text-lg pl-2 pt-2 w-52" placeholder="Financial Statement...." v-model="financial_statement_search">
                                        <option value="" selected disabled>Financial Statement</option>
                                        <option value="Balance Sheet">Balance Sheet</option>
                                        <option value="Income Statement">Income Statement</option>
                                    </select>
                            </div>
                        </div>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="searchLedgers"><i class="fa fa-binoculars" aria-hidden="true"></i> Search</button>
                    </div>
                    <div class="basis-1/8 pl-3 w-36">
                        <div class="print-dropdown">
                            <button class="rounded-lg bg-green-400 text-white px-3 py-2" @click="showDropdown">Options<i class="fa fa-caret-down pl-2" aria-hidden="true"></i></button>
                            <button class="fixed inset-button inset-0 bg-gray-50 opacity-25 cursor-default w-full" v-if="showOptions" @click="showOptions = !showOptions"></button>
                        </div>
                        <div class="options-container absolute right-25 pt-4 pb-2 rounded border border-gray-200 bg-white shadow-slate-400 shadow-xl" v-if="showOptions">
                            <button class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Print List</button><br />
                            <button @click="exportLedgersPDF" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export PDF</button><br />
                            <button @click="exportLedgersExcel" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export Excel</button>
                            <button @click="exportLedgersCSV" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Export CSV</button>
                            <button @click="showImportModal" class="pl-3 hover:bg-slate-500 hover:rounded hover:w-full">Import Excel</button>
                        </div>
                    </div>
            </div>
                <!-- MODAL component for adding a new ledger -->
                <Modal v-show="isModalVisible" @close="closeModal" :index="index">
                    <template v-slot:header> Ledger Details </template>
                    <template v-slot:body>
                    <form action="" @submit.prevent="">
                        <div class="flex mb-6">
                            <div class="basis-1/2 mx-12">
                                <label for="">Account Type<em>*</em></label><br />
                                <select name="" ref="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60"  v-model="ledger_type">
                                  <option value="" selected disabled>---Select Account Type</option>
                                  <option value="Cashbook">Cashbook</option>
                                  <option value="Current Asset">Current Asset</option> 
                                  <option value="Fixed Asset">Fixed Asset</option>
                                  <option value="Current Liability">Current Liability</option>
                                  <option value="Longterm Liability">Longterm Liability</option>
                                  <option value="Owner Equity">Owners Equity</option>
                                  <option value="Income">Income</option>
                                  <option value="Expenses">Expenses</option>
                                </select>
                            </div>
                            <div class="basis-1/2">
                                
                            </div>
                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mx-12">
                                <label for="">Account Code<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="ledger_code">
                            </div>
                            <div class="basis-1/2">
                            </div>

                        </div>
                        <div class="flex mb-6">
                            <div class="basis-1/2 mx-12">
                                <label for="">Account Name<em>*</em></label><br />
                                <input type="text" name="" id="" class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2" v-model="ledger_name">
                            </div>
                            <div class="basis-1/2">
                            </div>
                        </div>
                        
                        <div class="text-center" v-if="isEditing">
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="updateLedger">Update</button>
                        </div>
                        <div class="text-center" v-else>
                            <button class="rounded border bg-green-400 w-36 py-2 px-4 text-white text-lg" @click="createLedger">Save</button>
                        </div>

                    </form>
                    </template>
                    <template v-slot:footer>We Value Your Partnership </template>
                </Modal>
        
              <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                  <table class="min-w-full bg-white chart-of-accounts-table"> 
                      <thead class="bg-gray-800 text-white">
                          <tr class="rounded bg-slate-800 text-white font-semibold text-sm uppercase">
                              <th>#</th>
                              <th class="text-left py-3 px-4">Code</th>
                              <th class="text-left py-3 px-4">Account Name</th>
                              <th class="text-left py-3 px-4">Type</th>
                              <th class="text-left py-3 px-4">Financial Statement</th>
                              <th class="text-left py-3 px-4">Balance</th>
                              <th class="text-left py-3 px-4">Actions</th>
                          </tr>
                      </thead>
                      <tbody>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td>Assets</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td class="pl-4">Bank/Cash Accounts</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Cashbook'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Cashbook'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Cashbook'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Cashbook'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Cashbook'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Cashbook'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Cashbook'">
                              <div class="flex">
                                  <div class="basis-1/3">
                                      <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-if="led.status === 'Active'">
                                      <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-else>
                                      <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                  </div>
                                  <div class="basis-1/3">
                                      <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                  </div>
                              </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td class="pl-4">Current Assets</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Current Asset'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Asset'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Current Asset'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Asset'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Asset'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Asset'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Current Asset'">
                            <div class="flex">
                                  <div class="basis-1/3">
                                      <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-if="led.status === 'Active'">
                                      <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-else>
                                      <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                  </div>
                                  <div class="basis-1/3">
                                      <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                  </div>
                              </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td class="pl-4">Fixed Assets</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Fixed Asset'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Fixed Asset'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Fixed Asset'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Fixed Asset'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Fixed Asset'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Fixed Asset'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Fixed Asset'">
                            <div class="flex">
                                  <div class="basis-1/3">
                                      <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-if="led.status === 'Active'">
                                      <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-else>
                                      <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                  </div>
                                  <div class="basis-1/3">
                                      <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                  </div>
                              </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-sm uppercase">
                            <td></td>
                            <td></td>
                            <td>Liabilities</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td class="pl-4">Current Liabilities</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Current Liability'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Liability'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Current Liability'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Liability'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Liability'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Current Liability'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Current Liability'">
                            <div class="flex">
                                  <div class="basis-1/3">
                                      <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-if="led.status === 'Active'">
                                      <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                  </div>
                                  <div class="basis-1/3" v-else>
                                      <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                  </div>
                                  <div class="basis-1/3">
                                      <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                  </div>
                              </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-xs uppercase">
                            <td></td>
                            <td></td>
                            <td class="pl-4">Long Term Liabilities</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Longterm Liability'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Longterm Liability'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Longterm Liability'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Longterm Liability'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Longterm Liability'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Longterm Liability'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Longterm Liability'">
                            <div class="flex">
                                <div class="basis-1/3">
                                    <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                </div>
                                <div class="basis-1/3" v-if="led.status === 'Active'">
                                    <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                </div>
                                <div class="basis-1/3" v-else>
                                    <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                </div>
                                <div class="basis-1/3">
                                    <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                </div>
                            </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-sm uppercase">
                            <td></td>
                            <td></td>
                            <td>Owner's Equity</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Owner Equity'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Owner Equity'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Owner Equity'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Owner Equity'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Owner Equity'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Owner Equity'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Owner Equity'">
                            <div class="flex">
                                <div class="basis-1/3">
                                    <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                </div>
                                <div class="basis-1/3" v-if="led.status === 'Active'">
                                    <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                </div>
                                <div class="basis-1/3" v-else>
                                    <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                </div>
                                <div class="basis-1/3">
                                    <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                </div>
                            </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-sm uppercase">
                            <td></td>
                            <td></td>
                            <td>Income</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type === 'Income'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type === 'Income'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type === 'Income'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type === 'Income'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type === 'Income'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type === 'Income'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type === 'Income'">
                            <div class="flex">
                                <div class="basis-1/3">
                                    <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                </div>
                                <div class="basis-1/3" v-if="led.status === 'Active'">
                                    <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                </div>
                                <div class="basis-1/3" v-else>
                                    <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                </div>
                                <div class="basis-1/3">
                                    <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                </div>
                            </div>
                          </td>
                      </tr>
                      <tr class="font-semibold text-sm uppercase">
                            <td></td>
                            <td></td>
                            <td>Expenses</td>
                            <td></td>
                            <td></td>
                            <td></td>
                      </tr>
                      <tr v-for="(led,index) in chartOfAccountsList" :key="led.ledger_id" class="even:bg-gray-100 text-xs">
                          <td v-if="led.ledger_type=='Expenses'"></td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Expenses'">{{ led.ledger_code }}</td>
                          <td class="text-left py-2 px-2 pl-4" v-if="led.ledger_type=='Expenses'">{{ led.ledger_name }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Expenses'">{{ led.ledger_type }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Expenses'">{{ led.financial_statement }}</td>
                          <td class="text-left py-2 px-2" v-if="led.ledger_type=='Expenses'">{{ led.balance }}</td>
                          <td v-if="led.ledger_type=='Expenses'">
                            <div class="flex">
                                <div class="basis-1/3">
                                    <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                </div>
                                <div class="basis-1/3" v-if="led.status === 'Active'">
                                    <button @click="blockLedger(index)"><i class="fa fa-circle-o" aria-hidden="true" title="Block"></i></button>
                                </div>
                                <div class="basis-1/3" v-else>
                                    <button @click="unblockLedger(index)"><i class="fa fa-ban" aria-hidden="true" title="Unblock"></i></button>
                                </div>
                                <div class="basis-1/3">
                                    <button @click="removeLedger(index)"><i class="fa fa-trash-o" aria-hidden="true" title="Delete"></i></button>
                                </div>
                            </div>
                          </td>
                      </tr>
                      </tbody>
                  </table>   
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

export default{
    name: 'ChartOfAccountsView',
    props: ['scrollToTop','loader','showLoader','hideLoader',],
    data(){
    return{
      title: 'Financial Accounts/ Chart Of Accounts',
      companyID: "",
      chartOfAccountsList: [],
      currentPage: 1,
      ledger_code_search: "",
      ledger_name_search: "",
      financial_statement_search: "",
      ledger_type: "",
      isModalVisible: false,
      isEditing: false,
      showOptions: false,
      ledger_type: "",
      ledger_code: "",
      ledger_name: "",
      ledgerID: "",
      ledgerName: "",
      balance_sheet: "Balance Sheet",
      income_statement: "Income Statement"
    }
  },
    components: {
        NavBar,
        SideBarFA  ,
        Loader, 
        Modal
   },
   methods:{
    showModal(){
        this.scrollToTop();
        if(this.isEditing == false){
            this.ledger_code = "";
            this.ledger_name = "";
            this.ledger_type = "";
        }
        this.isModalVisible = !this.isModalVisible;
    },
    closeModal(){
        this.isModalVisible = false;
        this.isEditing = false;
    },
    createLedger(){
        this.showLoader();
        if(this.ledger_type === '' || this.ledger_code === '' || this.ledger_name === ''){
            this.$toast.error("Please Enter Ledger Details",{
                duration: 3000,
                dismissible: true
            })
            this.hideLoader();
        }
        else{
            let formData = new FormData();
            formData.append('ledger_type', this.ledger_type);
            formData.append('ledger_code', this.ledger_code);
            formData.append('ledger_name', this.ledger_name);
            if(this.ledger_type === 'Income' || this.ledger_type === 'Expenses'){
                formData.append('financial_statement', this.income_statement);
            }
            else{
                formData.append('financial_statement', this.balance_sheet);
            }
            formData.append('company', this.companyID);
            
            this.axios
            .post("api/v1/create-ledger/", formData)
            .then((response)=>{
                this.$toast.success("Ledger Succesfully Created",{
                    duration: 3000,
                    dismissible: true
                })
            })
            .catch((error)=>{
                console.log(error.message);
            })
            .finally(()=>{
                this.hideLoader();
                this.closeModal();
                this.ledger_code = "";
                this.ledger_name = "";
                this.ledger_type = "";
                this.$store.commit('reloadingPage');
            })
        }
    },
    searchLedgers(){
        this.isSearching = true;
        let formData = {
            ledger_code: this.ledger_code_search,
            ledger_name: this.ledger_name_search,
            financial_statement: this.financial_statement_search,
            company_id: this.companyID
        }
        this.axios
        .post(`api/v1/chart-of-accounts-search/?page=${this.currentPage}`,formData)
        .then((response)=>{
            this.chartOfAccountsList = response.data.results;
            console.log(this.chartOfAccountsList);
        })
        .catch((error)=>{
            console.log(error);
        })
    },
    editLedger(){
        this.showModal();
        this.isEditing = true;
        let selectedLedger = arguments[0];
        this.ledgerID = this.chartOfAccountsList[selectedLedger].ledger_id;
        this.ledger_name = this.chartOfAccountsList[selectedLedger].ledger_name;
        this.ledger_code = this.chartOfAccountsList[selectedLedger].ledger_code;
        this.ledger_type = this.chartOfAccountsList[selectedLedger].ledger_type;
        console.log()
        
    },
    updateLedger(){
        this.showLoader();
        if(this.ledger_type === '' || this.ledger_code === '' || this.ledger_name === ''){
            this.$toast.error("Please Enter Ledger Details",{
                duration: 3000,
                dismissible: true
            })
            this.hideLoader();
        }
        else{
            let formData = new FormData();
            formData.append('ledger', this.ledgerID);
            formData.append('ledger_type', this.ledger_type);
            formData.append('ledger_code', this.ledger_code);
            formData.append('ledger_name', this.ledger_name);
            if(this.ledger_type === 'Income' || this.ledger_type === 'Expenses'){
                formData.append('financial_statement', this.income_statement);
            }
            else{
                formData.append('financial_statement', this.balance_sheet);
            }
            formData.append('company', this.companyID);

            this.axios
            .put("api/v1/update-ledger/", formData)
            .then((response)=>{
                this.$toast.success("Ledger Updated Succesfully",{
                    duration: 3000,
                    dismissible: true
                })
            })
            .catch((error)=>{
                console.log(error.message);
            })
            .finally(()=>{
                this.ledger_code = "";
                this.ledger_name = "";
                this.ledger_type = "";
                this.hideLoader();
                this.closeModal();
                this.$store.commit('reloadingPage')
            })
        }
    },
    removeLedger() {
        let selectedItem = arguments[0];
        this.ledgerID = this.chartOfAccountsList[selectedItem].ledger_id;
        this.ledgerName = this.chartOfAccountsList[selectedItem].ledger_name;
        this.$swal({
            title: "Are you sure?",
            text: `Do you wish to delete ${this.ledgerName}?`,
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
                    ledger: this.ledgerID
                }
                this.axios
                .post("api/v1/delete-ledger/", formData)
                .then((response)=>{
                    this.$swal("Poof! Ledger removed succesfully!", {
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
                this.$swal(`${this.ledgerName} has not been deleted!`);
            }
        });
    },
    showDropdown(){
        this.showOptions = !this.showOptions;
    },
    exportLedgersPDF(){
        this.showLoader();
        let formData = {
            ledger_code: this.ledger_code_search,
            ledger_name: this.ledger_name_search,
            financial_statement: this.financial_statement_search,
            company_id: this.companyID
        }
        this.axios
        .post("api/v1/export-ledgers-pdf/", formData, { responseType: 'blob' })
        .then((response)=>{
            if(response.status == 200){
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'Chart Of Accounts.pdf');
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
    exportLedgersExcel(){
        this.showLoader();
        let formData = {
            ledger_code: this.ledger_code_search,
            ledger_name: this.ledger_name_search,
            financial_statement: this.financial_statement_search,
            company_id: this.companyID
        }
        this.axios
        .post("api/v1/export-ledgers-excel/", formData, { responseType: 'blob' })
        .then((response)=>{
            if(response.status == 200){
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'Chart Of Accounts.xls');
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
    exportLedgersCSV(){
        this.showLoader();
        let formData = {
            ledger_code: this.ledger_code_search,
            ledger_name: this.ledger_name_search,
            financial_statement: this.financial_statement_search,
            company_id: this.companyID
        }
        this.axios
        .post("api/v1/export-ledgers-csv/", formData, { responseType: 'blob' })
        .then((response)=>{
            if(response.status == 200){
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'Chart Of Accounts.csv');
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
        this.searchLedgers();
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
.chart-of-accounts-table{
    min-height: 100vh;
    max-height: 100vh;
    overflow-y: scroll;
    overflow-x: scroll;
}
</style>