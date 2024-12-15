<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">

      <div class="w-1/2 bg-transparent p-4">
        <img> 
        <div>

        </div>
      </div>


      <div class="w-full lg:w-4/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-6">
           
            <form @submit.prevent="handleLogin">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                Usuário ou
                Email
                </label>
                <input
                  type="text"
                  v-model="form.emailOrUsername"
                  @blur="validateField('emailOrUsername')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Usuário ou Email"
                />
                <span class="text-red text-xs">{{ errors.emailOrUsername }}</span>
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Senha
                </label>
                <input
                  type="password"
                  v-model="form.password"
                  @blur="validateField('password')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Senha"
                />
              </div>
              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                  type="submit"
                >
                  Logar
                </button>
              </div>
            </form>

            <div class="mt-6 text-center">
              <div class="flex justify-center items-center mb-4">
                <div class="border-t border-blueGray-300 flex-grow mr-8"></div>
                <div class="border-t border-blueGray-300 flex-grow ml-8"></div>
              </div>

              <!-- Links Esqueci minha senha e Criar conta -->
              <div class="border-0 px-3 py-3 placeholder-blueGray-300 text-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              style="background-color: #451724;">  
               
                <a href="javascript:void(0)" class="text-black-200">
                  <small>Esqueci minha senha</small>
                </a>
               
              </div>

             
              <div class="flex justify-center items-center mb-4 mt-4">
                <div class="border-t border-blueGray-300 flex-grow mr-2"></div>
                <span class="text-xs text-blueGray-600">ou</span>
                <div class="border-t border-blueGray-300 flex-grow ml-2"></div>
              </div>
             

              <div class="border-0 px-3 py-3 placeholder-blueGray-300 text-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              style="background-color: #142045;">  
               
                <router-link to="/auth/register" class="text-black-200">
                  <small>Quero criar uma conta</small>
                </router-link>
              
             </div>


            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
/* eslint-disable */
import router from '../../router/index.js';
import { ENDPOINTS } from '../../../../api.js';
import { useUserStore } from '../../store/user.js';
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        emailOrUsername: '',
        password: ''
      },
      errors: {},
      router
    };
  },

  setup() {
    const userStore = useUserStore()
    return { userStore };
  },

  methods: {
    validateField(field) {
      switch (field) {
        case 'emailOrUsername':
          if (!this.form.emailOrUsername) {
            this.errors.emailOrUsername = 'Email or Username is required.';
          } else if (!/\S+@\S+\.\S+/.test(this.form.emailOrUsername) && this.form.emailOrUsername.includes('@')) {
            this.errors.emailOrUsername = 'Invalid email format.';
          } else {
            this.errors.emailOrUsername = '';
          }
          break;
        case 'password':
          this.errors.password = this.form.password ? '' : 'Password is required.';
          break;
      }
    },

    async handleLogin() {

      Object.keys(this.form).forEach((field) => this.validateField(field));

      if (Object.keys(this.errors).some((key) => this.errors[key])) return;
      
      try {
        console.log("Vasco")
        const loginResponse = await axios.post(ENDPOINTS.LOGIN, this.form);
        console.log(loginResponse.data)
        console.log(loginResponse.errors)
        console.log("Flamengo")
        this.userStore.setToken(loginResponse.data);

        const userDetailsResponse = await axios.get(ENDPOINTS.DETAIL);
        this.userStore.setUserInfo(userDetailsResponse.data);

        router.push('/home');
      } catch (error) {

        if (error.response) {
          const errorMessage = error.response.data.message || 'Usuário inválido ou não existente.';
          alert(errorMessage);
        } else {
          console.error("Error:", error.message);
          alert('Unexpected error occurred.');
        }
      }
    }
  }
};
</script>

