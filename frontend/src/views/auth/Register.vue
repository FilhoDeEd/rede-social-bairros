<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-end justify-center h-full">
      <div class="w-full lg:w-6/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
          <div class="flex-auto px-4 lg:px-10 py-10">
            <form @submit.prevent="handleSubmit">
              <div class="flex gap-4 space-x-4">
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Nome</label>
                  <input type="text" v-model="form.firstName" @change="validateField('firstName')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Nome" />
                  <p v-if="errors.firstName" class="text-red-500 text-xs">{{ errors.firstName }}</p>
                </div>
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Sobrenome</label>
                  <input type="text" v-model="form.lastName" @change="validateField('lastName')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Sobrenome" />
                  <p v-if="errors.lastName" class="text-red-500 text-xs">{{ errors.lastName }}</p>
                </div>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Data de Nascimento</label>
                <input type="date" v-model="form.birthDate" @change="validateField('birthDate')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150" />
                <p v-if="errors.birthDate" class="text-red-500 text-xs">{{ errors.birthDate }}</p>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Email</label>
                <input type="email" v-model="form.email" @change="validateField('email')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email" />
                <p v-if="errors.email" class="text-red-500 text-xs">{{ errors.email }}</p>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Nome de Usuário</label>
                <input type="text" v-model="form.username" @change="validateField('username')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Nome de Usuário" />
                <p v-if="errors.username" class="text-red-500 text-xs">{{ errors.username }}</p>
              </div>

              <div class="flex gap-4 space-x-4">
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Senha</label>
                  <input type="password" v-model="form.password" @change="validateField('password')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="" />
                  <p v-if="errors.password" class="text-red-500 text-xs">{{ errors.password }}</p>
                </div>
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Confirmar senha</label>
                  <input type="password" @change="validateField('confirmPassword')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="" />
                  <p v-if="errors.confirmPassword" class="text-red-500 text-xs">{{ errors.confirmPassword }}</p>
                </div>
              </div>

              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input id="customCheckLogin" type="checkbox" v-model="form.agree" @change="validateField('agree')"
                    class="form-checkbox border-0 rounded text-blueGray-700 ml-1 w-5 h-5 ease-linear transition-all duration-150" />
                  <span class="ml-2 text-sm font-semibold text-blueGray-600">
                    Concordo com as 
                    <a href="javascript:void(0)" class="text-emerald-500">Políticas de Privacidade</a>
                  </span>
                </label>
                <p v-if="errors.agree" class="text-red-500 text-xs">{{ errors.agree }}</p>
              </div>

              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-varela uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                  type="submit">
                  Criar conta
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>

      <div class="w-full lg:w-6/12 px-4">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
          <div class="flex-auto px-4 lg:px-10 py-10">
            <form @submit.prevent="handleLocationSubmit">
              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Selecione o Estado</label>
                <select v-model="selectedState" @change="fetchCities"
                  class="border-0 px-3 py-3 bg-white text-blueGray-600 rounded text-sm shadow focus:outline-none focus:ring w-full">
                  <option value="">-</option>
                  <option v-for="state in states" :key="state.id" :value="state.id">
                    {{ state.name }}
                  </option>
                </select>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Selecione a Cidade</label>
                <select v-model="selectedCity" @change="fetchNeighborhoods"
                  class="border-0 px-3 py-3 bg-white text-blueGray-600 rounded text-sm shadow focus:outline-none focus:ring w-full">
                  <option value="">Selecione uma Cidade</option>
                  <option v-for="city in cities" :key="city.id" :value="city.id">
                    {{ city.name }}
                  </option>
                </select>
              </div>

              <div class="relative w-full mt-4">
                <label class="block uppercase text-blueGray-600 text-xs font-varela mb-2">Bairros</label>
                <div class="overflow-auto bg-white rounded shadow-lg max-h-64">
                  <table class="w-full text-left">
                    <thead>
                      <tr>
                        <th class="px-4 py-2 border-b border-gray-200">Bairro</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="neighborhood in neighborhoods" :key="neighborhood.id">
                        <td class="px-4 py-2 border-b border-gray-200">{{ neighborhood.name }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </form>
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
        name: "",
        surname: "",
        birthday: "",
        email: "",
        username: "",
        password: "",
        agree_policy: false,
        state: "", // Estado selecionado
        locality: "", // Cidade selecionada
        neighborhood: "", // Bairro selecionado
      },
      errors: {},
      states: [], // Lista de estados
      cities: [], // Lista de cidades
      neighborhoods: [], // Lista de bairros
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  async mounted() {
    // Busca os estados ao carregar o componente
    await this.fetchStates();
  },
  methods: {
    async fetchStates() {
      try {
        const response = await fetch(ENDPOINTS.STATES);
        this.states = await response.json();
      } catch (error) {
        alert("Erro ao carregar os estados.");
      }
    },
    async fetchCities() {
      if (!this.form.state) {
        this.cities = [];
        this.neighborhoods = [];
        return;
      }
      try {
        const response = await fetch(`${ENDPOINTS.CITIES}?stateId=${this.form.state}`);
        this.cities = await response.json();
        this.neighborhoods = []; // Resetar bairros ao alterar a cidade
      } catch (error) {
        alert("Erro ao carregar as cidades.");
      }
    },
    async fetchNeighborhoods() {
      if (!this.form.locality) {
        this.neighborhoods = [];
        return;
      }
      try {
        const response = await fetch(`${ENDPOINTS.NEIGHBORHOODS}?cityId=${this.form.locality}`);
        this.neighborhoods = await response.json();
      } catch (error) {
        alert("Erro ao carregar os bairros.");
      }
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
        case "name":
          this.errors.firstName = this.form.name ? "" : "First Name is required.";
          break;
        case "surname":
          this.errors.lastName = this.form.surname ? "" : "Last Name is required.";
          break;
        case "birthday":
          if (!this.form.birthday) {
            this.errors.birthDate = "Birth Date is required.";
          } else if (calculateAge(this.form.birthday) < 16) {
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
        case "confirmPassword":
          if (!this.form.confirmPassword) {
            this.errors.confirmPassword = "Confirm Password is required.";
          } else if (this.form.password !== this.form.confirmPassword) {
            this.errors.confirmPassword = "Passwords do not match.";
          } else {
            this.errors.confirmPassword = "";
          }
          break;
        case "agree_policy":
          this.errors.agree = this.form.agree_policy ? "" : "You must agree to the Privacy Policy.";
          break;
        case "state":
          this.errors.state = this.form.state ? "" : "You must select a State.";
          break;
        case "locality":
          this.errors.city = this.form.locality ? "" : "You must select a City.";
          break;
        case "neighborhood":
          this.errors.neighborhood = this.form.neighborhood ? "" : "You must select a Neighborhood.";
          break;
      }
    },
    async handleSubmit() {
      // Validate all fields
      Object.keys(this.form).forEach((field) => this.validateField(field));

      if (Object.keys(this.errors).some((key) => this.errors[key])) return;

      try {
        const response = await fetch(ENDPOINTS.REGISTER, {
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
          throw new Error(data.message || "Failed to register.");
        }

        alert(data.message || "Account created successfully!");
        this.router.push(ENDPOINTS.LOGIN); // Redirecionar para a página de login
      } catch (error) {
        alert(error.message || "Something went wrong.");
      }
    },
  },
};
</script>

