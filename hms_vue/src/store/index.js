import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
  },
  getters: {
  },
  mutations: {
    //Setting Auth Token
    setToken(state,token){
      state.token = token;
      state.isAuthenticated = true
    },
  },
  actions: {
  },
  modules: {
  }
})
