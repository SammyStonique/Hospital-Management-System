<template>
    <NavBar
    :title="title"
    />
    <SideBarFA />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection rounded bg-white p-3">
          <h2 class="text-center font-bold">Chart Of Accounts</h2>
          <div class="md:px-8 py-8 w-full">
              <div class="flex items-end pt-4 pb-3 w-full border-b-2 border-gray-300 mb-6">
              </div>
              <div class="shadow overflow-hidden rounded border-b border-gray-200 row-span-8">
                  <table class="min-w-full bg-white"> 
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
                      
                      <tr v-for="(coa,index) in chartOfAccountsList" :key="coa.chart_of_account_id" class="even:bg-gray-100">
                          <td>{{ index + 1 }}.</td>
                          <td class="text-left py-3 px-2">{{ coa.ledger_code }}</td>
                          <td class="text-left py-3 px-2">{{ coa.ledger_name }}</td>
                          <td class="text-left py-3 px-2">{{ coa.ledger_type }}</td>
                          <td class="text-left py-3 px-2">{{ coa.financial_statement }}</td>
                          <td class="text-left py-3 px-2">{{ coa.ledger_balance }}</td>
                          <td>
                              <div class="flex">
                                  <div class="basis-1/2">
                                      <button @click="editLedger(index)"><i class="fa fa-pencil" aria-hidden="true" title="Edit"></i></button>
                                  </div>
                                  <div class="basis-1/2">
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

import NavBar from '@/components/NavBar.vue'
import SideBarFA from '@/components/SideBarFA.vue'

export default{
    name: 'ChartOfAccountsView',
    data(){
    return{
      title: 'Financial Accounts/ Chart Of Accounts'
    }
  },
    components: {
        NavBar,
        SideBarFA   
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