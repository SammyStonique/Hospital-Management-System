<template>
    <NavBar
    :title="title"
    />
    <SideBarHMS />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection">

      </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBarHMS from '@/components/SideBarHMS.vue'

export default{
    name: 'LabManagementView',
    data(){
    return{
      title: 'Hospital Management/ Lab Management'
    }
  },
    components: {
        NavBar,
        SideBarHMS
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