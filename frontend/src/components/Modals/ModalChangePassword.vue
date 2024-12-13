<template>
    <div v-if="isModalChangePasswordOpen" class="modal-overlay">
      <div class="modal-content">
        <button class="close-btn" @click="closeModal">X</button>
  
        <!-- Conteúdo do modal -->
        <form @submit.prevent="handlePasswordChange">
            <div class="flex gap-4 space-x-4">

                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Senha</label>
                  <input
                    type="password"
                    v-model="form.password"
                    @change="validateField('password')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  />
                  <p v-if="errors.password" class="text-red-500 text-xs">{{ errors.password }}</p>
                </div>
                
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Confirmar senha</label>
                  <input
                    type="password"
                    v-model="form.confirm_password"
                    @change="validateField('confirm_password')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  />
                  <p v-if="errors.confirm_password" class="text-red-500 text-xs">{{ errors.confirm_password }}</p>
                </div>

              </div>
            <!-- Botão Confirmar -->
            <div class="text-center mt-6">
                <button
                type="submit"
                class="bg-indigo-500 text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none ease-linear transition-all duration-150"
                >
                Confirmar
                </button>
            </div>
        </form>
      </div>
    </div>
  </template>
  
  

  <script>
  /* eslint-disable */

  import axios from 'axios';
  import { router } from "../../router/index.js";
  import { ENDPOINTS } from '../../../../api.js';
  import { useUserStore } from '../../store/user.js';
  
  export default {
    data() {
      return {
        userStore: useUserStore(),
        form: {
            password:"",
            confirm_password:"",
        },
        errors: {}, // Erros de validação
        router,
      };
    },
    props: {
        isModalChangePasswordOpen: Boolean, // Propriedade para controlar se o modal está aberto
    },
  
    methods: {

    closeModal() {
      this.$emit('close'); // Emite evento para o componente pai fechar o modal
    },
  
    // Validação de campo
    validateField(field) {
        // Verifica se o campo está vazio
        if (!this.form[field]) {
            this.errors[field] = 'Campo obrigatório.';
        } else if (field === 'confirm_password') {
            // Verifica se as senhas coincidem
            if (this.form.confirm_password !== this.form.password) {
            this.errors['confirm_password'] = 'Senhas não coincidem';
            } else {
            // Remove o erro de confirmação de senha se as senhas coincidirem
            delete this.errors['confirm_password'];
            }
        } else {
            // Caso o campo seja válido, remove qualquer erro anterior
            delete this.errors[field];
        }
    },
  
    // Submissão do formulário
    async handlePasswordChange() {
        this.errors = {}; // Limpar erros anteriores
        this.validateField('password');

        if (Object.keys(this.errors).length > 0) return; // Não continuar se houver erros

        try {
            const response = await axios.post(ENDPOINTS.EDIT_PASSWORD, {
            password: this.form.password,
            });

            if (response.status === 200) {
            this.userStore.removeToken();
            this.router.push('/login');
            } else {
            alert('Erro ao salvar a senha. Tente novamente.');
            }
        } catch (error) {
            console.error('Erro de comunicação com o servidor:', error);
            alert('Erro de comunicação com o servidor.');
        }
    },
},

  };
  </script>
  
  <style scoped>
/* Estilo para o modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5); /* Fundo opaco */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  max-width: 90%;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: transparent;
  border: none;
  font-size: 18px;
  cursor: pointer;
  color: #333;
}
</style>