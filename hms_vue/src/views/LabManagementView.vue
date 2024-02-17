<template>
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection">

      </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

export default{
    name: 'LabManagementView',
    data(){
    return{
      title: 'Lab Management'
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
  margin-left: 227px;
  margin-top: 65px;
  min-height: 100vh;
}
.subsection{
    min-height: 100vh;
}
</style>