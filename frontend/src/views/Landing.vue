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
      <button @click="fetchForums(forumStore.currentPage - 1, token)" 
              :disabled="!forumStore.previous || forumStore.isLoading">
        Página Anterior
      </button>
      <button @click="fetchForums(forumStore.currentPage + 1, token)" 
              :disabled="!forumStore.next || forumStore.isLoading">
        Próxima Página
      </button>
    </div>

    <!-- Mensagem de erro -->
    <p v-if="forumStore.error" class="error">{{ forumStore.error }}</p>
  </div>
</template>

<script>
import { useForumStore } from '@/stores/forumStore'; // Certifique-se de ajustar o caminho
import { useUserStore } from '../../store/user.js';

export default {
  setup() {
    const forumStore = useForumStore();
    const userStore = useUserStore()


    // Carrega os fóruns na montagem do componente
    onBeforeMount(() => {
      userStore.initStore();
      if (userStore.user.isAutheticated) {
        fetchForums(page=1)
      } else {
        alert("Usuário Não Autorizado")
      }    
    });

    return {
      forumStore,
      fetchForums,
      userStore,
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
