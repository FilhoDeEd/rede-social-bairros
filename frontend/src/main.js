import { createApp } from "vue";
import { createPinia } from 'pinia'

/* eslint-disable */
// styles

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";

import App from "@/App.vue";
import axios from 'axios'
import router from "./router";

axios.defaults.baseURL = 'http//127.0.0.1:8000'

const app = createApp(App)

//app.config.globalProperties.$axios = axios; // Adiciona axios como global
app.use(createPinia())
app.use(router, axios) //app.use(router)

app.mount("#app");
