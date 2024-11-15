import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css' // Using the default Vite CSS. Replace with your own global styles.
import router from './router'
import App from './App.vue'
import { useAuthStore } from './store/auth'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const authStore = useAuthStore()
authStore.setCsrfToken()

app.mount('#app')

