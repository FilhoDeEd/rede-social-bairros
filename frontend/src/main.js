import { createApp } from "vue";
import { createPinia } from 'pinia'

/* eslint-disable */
// styles

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";

import App from "@/App.vue";
import axios from 'axios'
import router from "./router";
import Toast from 'vue-toastification'
import "vue-toastification/dist/index.css";

axios.defaults.baseURL = 'http//127.0.0.1:8000'

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)
app.use(Toast, { 
    position: "bottom-right",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: "button",
    icon: true,
    rtl: false
  });
  

app.mount("#app");
