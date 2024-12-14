import { defineStore } from 'pinia';
import { ENDPOINTS } from '../../../api';
import axios from 'axios';
export const useForumStore = defineStore('forum', {
  state: () => ({
    forums: [], 
    currentPage: 1, 
    totalForums: 0, 
    pageSize: 10, 
    next: null, 
    previous: null, 
    isLoading: false, 
    error: null, 
    currentForum: null,
  }),
  actions: {
    async fetchForums(page = 1) {
      this.isLoading = true;
      this.error = null;

      try {
        const response = await axios.get(`${ENDPOINTS.LIST_FORUNS}?page=${page}`);
        //a rever - André
        console.log('Dados recebidos da API:', response.data.results); // Debug
        this.forums = response.data.results;
        this.totalForums = response.data.count;
        this.currentPage = page;
        this.next = response.data.next;
        this.previous = response.data.previous;
        console.log(this.forums)
      } catch (error) {
        this.error = 'Erro ao carregar os fóruns.';
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },

    async searchForums(query) {
      this.isLoading = true;
      try {
        const response = await axios.get(`${ENDPOINTS.LIST_FORUNS}?search=${query}`);
        this.forums = response.data.forums;
        this.totalForums = response.data.count;
        this.currentPage = 1; // Reinicia para a página inicial após a busca
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (error) {
        this.error = 'Erro ao buscar fóruns.';
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },

    //a rever - André
    async fetchForumDetails(slug) {
      this.isLoading = true;
      this.error = null;

      try {
        console.log('Buscando fórum com slug:', slug); // Debug
        const response = await axios.get(`${ENDPOINTS.FORUM_DETAIL}/${slug}`);
        console.log('Resposta da API:', response.data); // Debug
        this.currentForum = response.data;
        return response.data;
      } catch (error) {
        console.error('URL completa:', `${ENDPOINTS.FORUM_DETAIL}/${slug}`); // Debug
        console.error('Erro completo:', error); // Debug
        this.error = 'Erro ao carregar os detalhes do fórum.';
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async submitReply(payload) {
      try {
        const response = await axios.post(ENDPOINTS.FORUM_REPLY, payload);
        return response.data;
      } catch (error) {
        console.error('Erro ao enviar resposta:', error);
        throw error;
      }
    }
  },
  getters: {
    totalPages: (state) => Math.ceil(state.totalForums / state.pageSize),
  },
});
