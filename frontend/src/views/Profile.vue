<template>
  <div>
    <navbar />
    <main class="profile-page">
      <section class="relative block h-600-px">
        <div class="absolute top-0 w-full h-full bg-center bg-cover" style="
            background-image: url('https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2710&q=80');
          ">
          <span id="blackOverlay" class="w-full h-full absolute opacity-50 bg-black"></span>
        </div>
        <div class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
          style="transform: translateZ(0);">
          <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"
            version="1.1" viewBox="0 0 2560 100" x="0" y="0">
            <polygon class="text-blueGray-200 fill-current" points="2560 0 2560 100 0 100"></polygon>
          </svg>
        </div>
      </section>

      <section id="dataProfile" class="relative py-16 bg-blueGray-200">

        <div class="container mx-auto px-4" id="infoProfile">
          <form @submit.prevent="handleSubmit">
            <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64">
              <div class="px-6 justify-end">
                <div class="flex flex-wrap justify-end">
                  <div class="w-full lg:w-3/12 lg:order-2" style="padding-left: 100px;">
                    <div class="relative group">
                      <!-- Exibe a imagem de perfil -->
                      <img alt="Profile Picture" :src="profileImage || team2"
                        class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />

                      <!-- Botão de upload visível no modo de edição -->
                      <div v-if="editMode"
                        class="absolute inset-0 bg-black bg-opacity-30 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300">
                        <label for="uploadImage" class="flex flex-col items-center cursor-pointer">
                          <i class="fas fa-upload text-white text-2xl"></i>
                          <span class="text-white text-sm">Editar</span>
                        </label>
                        <!-- Input oculto -->
                        <input id="uploadImage" type="file" accept="image/*" @change="handleImageUpload"
                          class="hidden" />
                      </div>
                    </div>



                  </div>

                  <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                    <div class="py-6 px-3 mt-32 sm:mt-0">
                      <button id="editButton"
                        class="bg-emerald-500 active:bg-emerald-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150"
                        type="button" @click="toggleEdition">
                        {{ editMode ? 'Salvar' : 'Editar' }} <!-- Mudança aqui -->
                      </button>
                    </div>
                  </div>
                </div>

                <div class="text-center mt-12">
                  <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                    Nome
                  </h3>
                  <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                    <i class="fas mr-2 text-lg text-blueGray-400"></i>
                    <input type="text" :placeholder="editMode ? '' : 'username'" id="username-input"
                      v-model="form.username"
                       :readonly="!editMode"
                       :value="userStore.user.access ? userStore.user.name :''"
                      @focus="onFocus" @blur="onBlur"

                      class="border-none outline-none text-blueGray-400 font-bold uppercase focus:ring-0 focus:outline-none text-center"
                     />
                  </div>
                </div>
                <!-- Biografia -->
                <div class="relative mt-6">
                  <label for="bio-textarea" class="block mb-2 text-sm font-medium text-blueGray-700">Biografia</label>
                  <div class="overflow-hidden">
                    <textarea id="bio-textarea" v-model="form.bio" :readonly="!editMode"
                      class="w-full resize-none border border-gray-300 rounded-lg px-3 py-2 align-top sm:text-sm focus:ring-blue-500 focus:border-blue-500"
                      rows="4" placeholder="Escreva sua biografia aqui..."></textarea>
                  </div>
                  <p v-if="errors.bio" class="text-red-500 text-xs mt-2">{{ errors.bio }}</p>
                </div>


                <!-- Linha superior: div1, div2, div3 -->
                <div class="rowForProfile mt-10 py-10 border-t border-blueGray-200 text-center">

                  <!-- Phone -->
                  <div class="itemForProfile">
                    <label for="phone-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone
                      number:</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 start-0 flex items-center pl-4 pointer-events-none">
                        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                          xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 19 18">
                          <path
                            d="M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z" />
                        </svg>
                      </div>
                      <input type="text" id="phone-input" :readonly="!editMode" v-model="form.phone"
                        @change="validateField('phone')" aria-describedby="helper-text-explanation"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required />
                      <p v-if="errors.phone" class="text-red-500 text-xs">{{ errors.phone }}</p>
                    </div>
                  </div>

                  <!-- Email -->
                  <div class="itemForProfile">
                    <label for="UserEmail"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email:</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 start-0 flex items-center pl-4 pointer-events-none">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-gray-500 dark:text-gray-400"
                          fill="currentColor" viewBox="0 0 20 20">
                          <path d="M2.94 6.94A2.5 2.5 0 015.5 5h9a2.5 2.5 0 012.5 1.94l-7 4.2-7-4.2z" />
                          <path d="M18 8.9l-7 4.2-7-4.2V14.5a2.5 2.5 0 002.5 2.5h9a2.5 2.5 0 002.5-2.5V8.9z" />
                        </svg>
                      </div>
                      <input type="email" id="UserEmail" :readonly="!editMode" v-model="form.email"
                        @change="validateField('email')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required />
                      <p v-if="errors.email" class="text-red-500 text-xs">{{ errors.email }}</p>
                    </div>
                  </div>

                  <!-- Senha -->
                  <div class="itemForProfile">
                    <label for="password-input"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Senha:</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 start-0 flex items-center pl-4 pointer-events-none">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-gray-500 dark:text-gray-400"
                          fill="currentColor" viewBox="0 0 20 20">
                          <path
                            d="M10 2a4 4 0 00-4 4v2a2 2 0 01-2 2v4a4 4 0 004 4h4a4 4 0 004-4v-4a2 2 0 01-2-2V6a4 4 0 00-4-4zm-1 6V6a1 1 0 112 0v2h-2z" />
                        </svg>
                      </div>
                      <input type="password" id="password-input" :readonly="!editMode" v-model="form.password"
                        @change="validateField('password')" placeholder="Senha"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required />
                      <p v-if="errors.password" class="text-red-500 text-xs">{{ errors.password }}</p>
                    </div>
                  </div>
                </div>

                <!-- Linha inferior -->
                <div class="rowForProfile mt-10 py-10 text-center">

                  <!-- Data de Nascimento -->
                  <div class="itemForProfile">
                    <label for="birthdate-input"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Data
                      de Nascimento:</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 start-0 flex items-center pl-4 pointer-events-none">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-gray-500 dark:text-gray-400"
                          fill="currentColor" viewBox="0 0 20 20">
                          <path
                            d="M6 2a2 2 0 00-2 2v1H2v2h2v9a2 2 0 002 2h8a2 2 0 002-2V7h2V5h-2V4a2 2 0 00-2-2H6zm8 15H6v-9h8v9z" />
                        </svg>
                      </div>
                      <input type="date" id="birthdate-input" :readonly="!editMode" v-model="form.birthDate"
                        @change="validateField('birthDate')"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required />
                      <p v-if="errors.birthDate" class="text-red-500 text-xs">{{ errors.birthDate }}</p>
                    </div>
                  </div>

                  <!-- Gênero -->
                  <div class="itemForProfile">
                    <label for="gender-select"
                      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Gênero:</label>
                    <div class="relative">
                      <select id="gender-select" name="gender" :disabled="!editMode"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value="" disabled selected>Selecione um gênero</option>
                        <option value="male">Masculino</option>
                        <option value="female">Feminino</option>
                        <option value="nonbinary">Não-Binário</option>
                      </select>
                    </div>
                  </div>

                </div>
              </div>
            </div>
          </form>
        </div>
      </section>

      <section id="dataLocation" class="relative py-16 bg-blueGray-200">
        <div class="container mx-auto px-4">
          <form @submit.prevent="handleSubmit">
            <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64">
              <div class="px-6 justify-end">
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Estado</label>
                  <select v-model="form.state" @change="[fetchCities, validateField('state')]" :disabled="!editMode"
                    class="border-0 px-3 py-3 bg-white text-blueGray-600 rounded text-sm shadow focus:outline-none focus:ring w-full">
                    <option value="">Selecione um Estado</option>
                    <option v-for="state in states" :key="state.code" :value="state.code">
                      {{ state.name }}
                    </option>
                  </select>
                </div>

                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Cidade</label>
                  <select v-model="form.locality" @change="[fetchNeighborhoods, validateField('locality')]" :disabled="!editMode"
                    class="border-0 px-3 py-3 bg-white text-blueGray-600 rounded text-sm shadow focus:outline-none focus:ring w-full">
                    <option value="" >Selecione uma Cidade</option>
                    <option v-for="city in cities" :key="city.name" :value="city.name">
                      {{ city.name }}
                    </option>
                  </select>
                </div>

                <div class="relative w-full mt-4">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Bairro</label>
                  <select v-model="form.neighborhood" @change="validateField('neighborhood')" :disabled="!editMode"
                    class="w-full bg-white border border-gray-300 rounded px-4 py-2 text-gray-700 focus:outline-none focus:ring focus:border-blue-500">
                    <option value="">Selecione um Bairro</option>
                    <option v-for="neighborhood in neighborhoods" :key="neighborhood.name" :value="neighborhood.name">
                      {{ neighborhood.name }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </form>
        </div>
      </section>

    </main>
    <footer-component />
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";
import onBeforeMount from "vue"
import team2 from "@/assets/img/team-2-800x800.jpg";
import { ENDPOINTS } from '../../../api.js';
import { useUserStore } from '../../store/user.js';


export default {
  components: {
    Navbar,
    FooterComponent
  },
  data() {
    return {
      form: {
        phone: "",
        email: "",
        username: "",
        password: "",
      },
      profileImage: null, // Variável para armazenar a nova imagem ou a atual
      errors: {},
      editMode: false, // Determina se o formulário está em modo de edição
      team2,
    };
  },

  onBeforeMount(){
      this.userStore.initStore()

      const token = this.userStore.user.access

      if (token){
        axios.defaults.headers.common["Authorization"] = "Bearer " + token;
      }
      else{
        axios.defaults.headers.common["Authorization"] = "";
      }

    }

  async mounted() {
    await this.fetchState();
  },
  methods: {
    setup(){
      const userStore = useUserStore()
      return{
        userStore
      } 
    },

    async fetchState() {
      try {
        const response = await axios.get(ENDPOINTS.USERS);
        this.state = response.data;
      } catch (error) {
        alert("Erro ao carregar o estado.");
      }
    },

    toggleEdition() {
      if (this.editMode) {
        // Salvar: valida campos antes de alternar
        Object.keys(this.form).forEach((field) => this.validateField(field));
        if (Object.keys(this.errors).some((key) => this.errors[key])) {
          alert("Por favor, corrija os erros antes de salvar.");
          return;
        }
      }
      this.editMode = !this.editMode;
    },
    onFocus() {
      // Quando o campo ganha foco, removemos o placeholder
      if (this.editMode) {
        this.username = ''; // Se o editMode estiver ativo, limpamos o valor.
      }
    },
    onBlur() {
      // Quando o campo perde o foco, você pode restaurar o valor padrão ou realizar outras ações
    },

    async handleImageUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      // Validação opcional para tipo e tamanho do arquivo
      if (!file.type.startsWith("image/")) {
        alert("Por favor, selecione um arquivo de imagem válido.");
        return;
      }
      if (file.size > 5 * 1024 * 1024) {
        alert("A imagem deve ter no máximo 5MB.");
        return;
      }

      // Pré-visualização da imagem
      const reader = new FileReader();
      reader.onload = (e) => {
        this.profileImage = e.target.result;
      };
      reader.readAsDataURL(file);

      // Caso queira enviar a imagem ao servidor:
      // const formData = new FormData();
      // formData.append("profileImage", file);
      // await axios.post(ENDPOINTS.UPLOAD_PROFILE_IMAGE, formData);
    },


    validateField(field) {
      const calculateAge = (birthDate) => {
        const today = new Date();
        const birth = new Date(birthDate);
        let age = today.getFullYear() - birth.getFullYear();
        const monthDifference = today.getMonth() - birth.getMonth();
        if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birth.getDate())) {
          age--;
        }
        return age;
      };

      switch (field) {
        case "birthDate":
          if (!this.form.birthDate) {
            this.errors.birthDate = "Birth Date is required.";
          } else if (calculateAge(this.form.birthDate) < 16) {
            this.errors.birthDate = "You must be at least 16 years old.";
          } else {
            this.errors.birthDate = "";
          }
          break;
        case "email":
          if (!this.form.email) {
            this.errors.email = "Email is required.";
          } else if (!/\S+@\S+\.\S+/.test(this.form.email)) {
            this.errors.email = "Invalid email format.";
          } else {
            this.errors.email = "";
          }
          break;
        case "username":
          this.errors.username = this.form.username ? "" : "Username is required.";
          break;
        case "password":
          this.errors.password = this.form.password
            ? (/[A-Z]/.test(this.form.password) ? "" : "A senha deve conter ao menos uma letra maiúscula.") ||
              (/[a-z]/.test(this.form.password) ? "" : "A senha deve conter ao menos uma letra minúscula.") ||
              (/\d/.test(this.form.password) ? "" : "A senha deve conter ao menos um número.") ||
              (/[\W_]/.test(this.form.password) ? "" : "A senha deve conter ao menos um caractere especial.") ||
              (this.form.password.length >= 8 ? "" : "A senha deve ter no mínimo 8 caracteres.")
            : "A senha é obrigatória.";
            break;
      }

    },
    async handleSubmit() {
      // Validate all fields
      Object.keys(this.form).forEach((field) => this.validateField(field));

      if (Object.keys(this.errors).some((key) => this.errors[key])) return;

      try {
        const response = await fetch(ENDPOINTS.PROFILE, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form),
        });

        const data = await response.json();

        if (!response.ok) {
          if (data.errors) {
            for (const [field, messages] of Object.entries(data.errors)) {
              this.errors[field] = messages.join(" ");
            }
          }
          throw new Error(data.message || "Failed to save.");
        }
      } catch (error) {
        alert(error.message || "Something went wrong.");
      }
    },

  }
};
</script>

<style scoped>
#dataLocation {
  /* Cria espaço suficiente entre dataProfile e dataLocation */
  padding-top: 200px;
}

.bg-white {
  padding-top: 20px;
  padding-bottom: 2rem;
  /* Adiciona um espaço interno inferior */
}
</style>
