<template>
  <MainLayout>
    <div class="w-8/12 h-full py-8 pr-20 pl-20 bg-gray-50 space-y-4">
      <main>
        <section id="conteudo">
          <h1 class="text-xl font-bold mb-4">Discussões</h1>
          <div class="space-y-4">
            <article v-for="forum in forumStore.forums" :key="forum.forum_id"
              class="p-4 shadow rounded hover:shadow-lg transition-shadow duration-200 bg-white cursor-pointer"
              @click="navigateToForum(forum.forum_id)">
              <div class="flex justify-between items-start">
                <div class="flex-1">
                  <h2 class="text-2xl font-semibold mb-2 hover:text-blue-600">{{ forum.title }}</h2>
                  <p class="text-gray-600 mb-4">{{ forum.description }}</p>
                  <div class="flex items-center text-sm text-gray-500">
                    <span class="mr-4">Criado por: {{ forum.creator_username }}</span>
                    <span>Data: {{ formatDate(forum.created_at) }}</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-sm text-gray-500">{{ forum.reply_count || 0 }} respostas</span>
                </div>
              </div>
            </article>
          </div>
        </section>
      </main>
    </div>
  </MainLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useForumStore } from '@/store/forum.js';
import MainLayout from '../layouts/mainLayout.vue';

const router = useRouter();
const forumStore = useForumStore();

// Função para navegar para a página do fórum específico
const navigateToForum = (forumId) => {
  router.push(`/forum/${forumId}`);
};

// Função para formatar a data
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR');
};

// Carregar os fóruns quando o componente for montado
onMounted(async () => {
  await forumStore.fetchForums();
});
</script>

<style scoped>
.bg-white {
  background-color: #ffffff;
}

.cursor-pointer {
  cursor: pointer;
}

h2:hover {
  transition: color 0.2s ease;
}
</style>
