<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-1/2 bg-transparent p-4">
        <div>
          <img alt="..." class="w-full" :src="logo" />
        </div>
      </div>

      <div class="w-full lg:w-4/12 px-4">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
          <div class="rounded-t mb-0 px-6 py-6">
            <form @submit.prevent="handleLogin">
              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
                  Usuário ou Email
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
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">
                  Senha
                </label>
                <input
                  type="password"
                  v-model="form.password"
                  @blur="validateField('password')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Senha"
                />
                <span class="text-red text-xs">{{ errors.password }}</span>
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

              <!-- Link Esqueci minha senha -->
              <button
                @click="openModal('Esqueci Minha Senha')"
                class="border-0 px-3 py-3 text-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                style="background-color: #451724;"
              >
                <small>Esqueci minha senha</small>
              </button>

              <!-- Componente do modal -->
              <ForgotPassword
                :isVisible="isModalVisible"
                :title="modalTitle"
                @close="isModalVisible = false"
              />

              <div class="flex justify-center items-center mb-4 mt-4">
                <div class="border-t border-blueGray-300 flex-grow mr-2"></div>
                <span class="text-xs text-blueGray-600">ou</span>
                <div class="border-t border-blueGray-300 flex-grow ml-2"></div>
              </div>

              <!-- Link Criar Conta -->
              <router-link to="/auth/register">
                <button
                  class="border-0 px-3 py-3 text-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  style="background-color: #142045;"
                >
                  <small>Quero criar uma conta</small>
                </button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import ForgotPassword from "../../components/Modal/ForgotPassword.vue";
import logo from "@/assets/img/logo-alternative-medium.png";
import { ENDPOINTS } from "../../../../api.js";

export default {
  components: {
    ForgotPassword,
  },
  data() {
    return {
      form: {
        emailOrUsername: "", // Pode ser email ou username
        password: "",
      },
      errors: {},
      isModalVisible: false,
      modalTitle: "",
      logo,
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    openModal(title) {
      this.modalTitle = title;
      this.isModalVisible = true;
    },
    validateField(field) {
      if (field === "emailOrUsername") {
        const value = this.form.emailOrUsername;
        if (!value) {
          this.errors.emailOrUsername = "Email ou Usuário é obrigatório.";
        } else if (value.includes("@") && !/\S+@\S+\.\S+/.test(value)) {
          this.errors.emailOrUsername = "Formato de email inválido.";
        } else {
          this.errors.emailOrUsername = "";
        }
      }
      if (field === "password") {
        this.errors.password = this.form.password ? "" : "Senha é obrigatória.";
      }
    },
    async handleLogin() {
      const isEmail = /\S+@\S+\.\S+/.test(this.form.emailOrUsername);
      const loginData = isEmail
        ? { email: this.form.emailOrUsername }
        : { username: this.form.emailOrUsername };
      const dataToSend = { ...loginData, password: this.form.password };

      // Validar campos antes de enviar
      Object.keys(this.form).forEach((field) => this.validateField(field));
      if (Object.keys(this.errors).some((key) => this.errors[key])) return;

      try {
        const response = await fetch(ENDPOINTS.LOGIN, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(dataToSend),
        });

        if (response.ok) {
          const data = await response.json();
          alert(data.message || "Login realizado com sucesso!");
          this.router.push(ENDPOINTS.HOME);
        } else {
          const errorText = await response.text();
          const errorData = JSON.parse(errorText);
          alert(errorData.message || "Erro durante o login.");
        }
      } catch (error) {
        console.error("Erro no login:", error);
        alert("Erro inesperado.");
      }
    },
  },
};
</script>
