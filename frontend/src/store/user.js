import { defineStore } from "pinia";
import axios from "axios";
import { ENDPOINTS } from "../../../api";

// Criação da instância global do axios
const apiClient = axios.create({
  timeout: 10000, // Timeout opcional para requisições
});

// Store do usuário
export const useUserStore = defineStore({
  id: "user",

  state: () => ({
    user: {
      isAuthenticated: false,
      access: null,
      refresh: null,

      id: null,
      name: null,
      surname: null,
      email: null,
      username: null,
      cellphone: null,
      gender: null,
      biography: null,
      birthday: null,
      status: null,

      state: null,
      locality: null,
      neighborhood: null,
      neighborhood_id: null,
    },
  }),

  actions: {
    initStore() {
      if (localStorage.getItem("user.access")) {
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");

        this.user.id = localStorage.getItem("user.id");
        this.user.email = localStorage.getItem("user.email");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.username = localStorage.getItem("user.username");
        this.user.cellphone = localStorage.getItem("user.cellphone");
        this.user.gender = localStorage.getItem("user.gender");
        this.user.biography = localStorage.getItem("user.biography");
        this.user.birthday = localStorage.getItem("user.birthday");
        this.user.status = localStorage.getItem("user.status");

        this.user.state = localStorage.getItem("user.state");
        this.user.locality = localStorage.getItem("user.locality");
        this.user.neighborhood = localStorage.getItem("user.neighborhood");
        this.user.neighborhood_id = localStorage.getItem("user.neighborhood_id");

        this.user.isAuthenticated = true;

        // Configurar o cabeçalho Authorization no formato "Token <token>"
        apiClient.defaults.headers.common["Authorization"] = `Token ${this.user.access}`;
        console.log("User initialized", this.user);
      }
    },

    setToken(data) {
      console.log("setToken", data);

      this.user.access = data.access;
      this.user.isAuthenticated = true;
      localStorage.setItem("user.access", data.access);

      // Atualizar o cabeçalho Authorization no formato "Token <token>"
      apiClient.defaults.headers.common["Authorization"] = `Token ${data.access}`;
    },

    removeToken(){
        this.user.access = null
        this.user.refresh = null
        this.user.isAutheticated = false
        this.user.id = false
        this.user.name = false
        this.user.email = false
        this.user.surname= false
        this.user.username= false
        this.user.cellphone= false
        this.user.gender= false
        this.user.biography= false
        this.user.birthday= false
        this.user.status= false

        
        this.user.state= false
        this.user.locality= false
        this.user.neighborhood= false
        this.user.neighborhood_id= false


        localStorage.setItem('user.access','')
        localStorage.setItem('user.refresh','')

        localStorage.setItem('user.id','')
        localStorage.setItem('user.name','')
        localStorage.setItem('user.email','')
        localStorage.setItem('user.surname','')
        localStorage.setItem('user.username','')
        localStorage.setItem('user.cellphone','')
        localStorage.setItem('user.gender','')
        localStorage.setItem('user.biography','')
        localStorage.setItem('user.birthday','')
        localStorage.setItem('user.status','')

        localStorage.setItem('user.state','')
        localStorage.setItem('user.locality','')
        localStorage.setItem('user.neighborhood','')
        localStorage.setItem('user.neighborhood_id','')

        delete apiClient.defaults.headers.common["Authorization"];
        console.log("Logged Out")
    },

    setUserInfo(user){
        console.log("setUserInfo",user)

        this.user.id = user.id
        this.user.name = user.name
        this.user.email = user.email
        this.user.surname = user.surname
        this.user.username = user.username
        this.user.cellphone = user.cellphone
        this.user.gender = user.gender
        this.user.biography = user.biography
        this.user.birthday = user.birthday
        this.user.status = user.status

        
        this.user.state= user.state
        this.user.locality= user.locality
        this.user.neighborhood= user.neighborhood
        this.user.neighborhood_id= user.neighborhood_id

        localStorage.setItem('user.id', this.user.id)
        localStorage.setItem('user.name', this.user.name)
        localStorage.setItem('user.email', this.user.email)
        localStorage.setItem('user.surname', this.user.surname)
        localStorage.setItem('user.username', this.user.username)
        localStorage.setItem('user.cellphone', this.user.cellphone)
        localStorage.setItem('user.gender', this.user.gender)
        localStorage.setItem('user.biography', this.user.biography)
        localStorage.setItem('user.birthday', this.user.birthday)
        localStorage.setItem('user.status', this.user.status)

        localStorage.setItem('user.state', this.user.state)
        localStorage.setItem('user.locality', this.user.locality)
        localStorage.setItem('user.neighborhood', this.user.neighborhood)
        localStorage.setItem('user.neighborhood_id', this.user.neighborhood_id)

        console.log('User', this.user)
    },

    async refreshToken() {
      try {
        const response = await apiClient.post(ENDPOINTS.REFRESH, {
          refresh: this.user.refresh,
        });

        this.user.access = response.data.access;
        localStorage.setItem("user.access", response.data.access);

        // Atualizar o cabeçalho Authorization no formato "Token <token>"
        apiClient.defaults.headers.common["Authorization"] = `Token ${response.data.access}`;
      } catch (error) {
        console.error(error);
        this.removeToken();
      }
    },
  },
});

// Exportar a instância personalizada para outros arquivos
export { apiClient };
