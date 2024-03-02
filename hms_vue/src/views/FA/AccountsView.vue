<template>
    <NavBar
    :title="title"
    />
    <SideBarFA />
    <div class="main-content bg-gray-100 px-4 py-4">
      <div class="subsection">

      </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBarFA from '@/components/SideBarFA.vue'

export default{
    name: 'AccountsView',
    data(){
    return{
      title: 'Accounts'
    }
  },
    components: {
        NavBar,
        SideBarFA    }
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