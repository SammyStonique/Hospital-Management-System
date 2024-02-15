import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    reloaded: false,
  },
  getters: {
  },
  mutations: {
    //Reloading The Page
    reloadingPage(state){
      if (localStorage.getItem('reloaded')) {
        // The page was just reloaded. Clear the value from local storage
        // so that it will reload the next time this page is visited.
        localStorage.removeItem('reloaded', 'false');
        console.log('Value of reload in store set to false')
        } else {
            // Set a flag so that we know not to reload the page twice.
            localStorage.setItem('reloaded', 'true');
            console.log(state.reloaded,'Reload')
            window.location.reload();
        }
    },
    //Initializing The Local Storage
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token');
        state.isAuthenticated = true;
      }else{
        state.token = '';
        state.isAuthenticated = false;
      }
    },
    //Setting Auth Token
    setToken(state,token){
      state.token = token;
      state.isAuthenticated = true
    },
    //REMOVING AUTHENTICATION TOKEN
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
      localStorage.removeItem('token')
    },
  },
  actions: {
  },
  modules: {
  }
})
