<template>
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content bg-gray-100 px-4 py-4"></div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

export default{
    name: 'PayrollView',
    data(){
    return{
      title: 'Payroll'
    }
  },
    components: {
        NavBar,
        SideBar
    }
}
</script>

<style scoped>
.main-content{
  z-index: -1;
  margin-left: 338px;
  margin-top: 65px;
}
</style>