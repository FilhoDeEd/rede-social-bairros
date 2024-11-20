<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
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
                  Email or Username
                </label>
                <input
                  type="text"
                  v-model="form.emailOrUsername"
                  @blur="validateField('emailOrUsername')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email or Username"
                />
                <span class="text-red text-xs">{{ errors.emailOrUsername }}</span>
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Password
                </label>
                <input
                  type="password"
                  v-model="form.password"
                  @blur="validateField('password')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password"
                />
              </div>
              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                  type="submit"
                >
                  Sign In
                </button>
              </div>
            </form>
          </div>
        </div>
        <div class="flex flex-wrap mt-6 relative">
          <div class="w-1/2">
            <a href="javascript:void(0)" class="text-blueGray-200">
              <small>Forgot password?</small>
            </a>
          </div>
          <div class="w-1/2 text-right">
            <router-link to="/auth/register" class="text-blueGray-200">
              <small>Create new account</small>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { useRouter } from 'vue-router';
import { ENDPOINTS } from '../../../../api.js';

export default {
  data() {
    return {
      form: {
        emailOrUsername: '',  // Pode ser email ou username
        password: ''
      },
      errors: {}
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    // Validação de campos
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

    // Função de login
    async handleLogin() {
      // Verificar qual campo foi preenchido: email ou username
      const isEmail = /\S+@\S+\.\S+/.test(this.form.emailOrUsername);

      // Validar os campos
      Object.keys(this.form).forEach((field) => this.validateField(field));

      // Verifica se há erros
      if (Object.keys(this.errors).some((key) => this.errors[key])) return;

      // Formatar o objeto a ser enviado: se for email, enviar como "email", senão enviar como "username"
      const loginData = isEmail ? { email: this.form.emailOrUsername } : { username: this.form.emailOrUsername };
      const dataToSend = { ...loginData, password: this.form.password };

      const response = await fetch(ENDPOINTS.LOGIN, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataToSend),
      });

      if (response.ok) {
        const data = await response.json();
        alert(data.message || 'Login successful!');
        this.router.push(ENDPOINTS.HOME); // Redireciona para a home ou outra página
      } else {
        const errorText = await response.text(); // Resposta como texto
        try {
          const errorData = JSON.parse(errorText); // Tenta fazer o parse manualmente
          alert(errorData.message || 'Something went wrong.');
        } catch (error) {
          console.error("Error parsing JSON:", errorText);
          alert('Unexpected error occurred.');
        }
      }
    }
  }
};
</script>
