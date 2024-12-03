<template>
  <div>
    <ul>
      <li v-for="forum in forumStore.forums" :key="forum.id">
        <div>
          <h4>{{ forum.title }}</h4>
          <p>{{ forum.description }}</p>
          <p>{{ forum.popularity }}</p>
        </div>
      </li>
    </ul>

    <!-- Botões de Paginação -->
    <div>
      <button @click="fetchForums(forumStore.currentPage - 1)"  
              :disabled="!forumStore.previous || forumStore.isLoading">
        Página Anterior
      </button>
      <button @click="fetchForums(forumStore.currentPage + 1)"
              :disabled="!forumStore.next || forumStore.isLoading">
        Próxima Página
      </button>
    </div>

    <!-- Mensagem de erro -->
    <p v-if="forumStore.error" class="error">{{ forumStore.error }}</p>
  </div>
</template>

<script>
import { useForumStore } from '../store/forum.js';
import { useUserStore } from '../store/user.js';
import { onBeforeMount } from 'vue';

export default {
  setup() {
    const forumStore = useForumStore();
    const userStore = useUserStore();

    // Carrega os fóruns na montagem do componente
    onBeforeMount(() => {
      userStore.initStore();
      if (userStore.user.isAuthenticated) {
        forumStore.fetchForums(1); // Chama a função para carregar os fóruns
      } else {
        alert("Usuário Não Autorizado");
      }
    });

    // Função para chamar a fetch de fóruns
    const fetchForums = (page) => {
      forumStore.fetchForums(page);
    };

    return {
      forumStore,
      userStore,
      fetchForums, // Adiciona a função fetchForums ao template
    };
  },
};
</script>

<style>
.error {
  color: red;
  font-weight: bold;
}
</style>
