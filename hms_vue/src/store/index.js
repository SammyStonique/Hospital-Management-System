import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
  },
  getters: {
  },
  mutations: {
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
