<template>
    <div class="login">
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="email">Email:</label>
          <input v-model="email" id="email" type="text" required
                 @input="resetError">
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="password" id="password" type="password" required
                 @input="resetError">
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import { useAuthStore } from '../store/auth'
  
  export default {
    setup() {
      const authStore = useAuthStore()
      return {
        authStore
      }
    },
    data() {
      return {
        email: "",
        password: "",
        error: ""
      }
    },
    methods: {
      async login(){
        await this.authStore.login(this.email, this.password, this.$router)
        if (!this.authStore.isAuthenticated){
          this.error = 'Login failed. Please check your credentials.'
        }
      },
      resetError(){
        this.error = ""
      }
    }
  }
  </script>
  