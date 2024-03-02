<template>
    <NavBar
    :title="title"
    />
    <SideBarHR />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection">

      </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBarHR from '@/components/SideBarHR.vue'

export default{
    name: 'PayrollView',
    data(){
    return{
      title: 'Payroll'
    }
  },
    components: {
        NavBar,
        SideBarHR
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