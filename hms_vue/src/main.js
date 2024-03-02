import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import DropZone from 'dropzone-vue';
import 'dropzone-vue/dist/dropzone-vue.common.css';
import './index.css'

const options = {
    confirmButtonColor: '#41b882',
    cancelButtonColor: '#ff7674',
  };

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(store).use(router).use(VueAxios, axios).use(VueToast,{position:'top'}).use(VueSweetalert2, options).use(DropZone).mount('#app')
