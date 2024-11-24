<template>
  <div>
    <navbar />
    <main class="profile-page">
      <section class="relative block h-500-px">
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
      <section class="relative py-16 bg-blueGray-200">

        <div class="container mx-auto px-4" id="infoProfile">

          <form @submit.prevent="handleSubmit">
            <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64">
            <div class="px-6 justify-end">
              <div class="flex flex-wrap justify-end">
                <div class="w-full lg:w-3/12 lg:order-2" style="padding-left: 100px;">
                  <div class="relative">
                    <img alt="..." :src="team2"
                      class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
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
                  <input type="text" v-model="form.username" :readonly="!editMode"
                    class="border-none outline-none text-blueGray-400 font-bold uppercase focus:ring-0 focus:outline-none text-center"
                    placeholder="Username"/>
                </div>
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
                  <label for="birthdate-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Data
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
    </main>
    <footer-component />
  </div>
</template>
<script>

import axios from 'axios';

import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";

import team2 from "@/assets/img/team-2-800x800.jpg";


import { ENDPOINTS } from '../../../api.js';

export default {
  data() {
    return {
      form: {
        phone: "",
        email: "",
        username: "",
        password: "",
      },
      errors: {},
      editMode: false, // Inicialmente, os campos são somente leitura
      team2,
    };
  },
  methods: {
    toggleEdition() {
      this.editMode = !this.editMode; // Alterna entre editar e salvar
      this.type = "submit";
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
          this.errors.password = this.form.password ? "" : "Password is required.";
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
    components: {
      Navbar,
      FooterComponent
    },
  }
};
</script>
