<template>
  <MainLayout>
    <div class="w-8/12 h-full py-8 pr-20 pl-20 bg-gray-50">
      <div v-if="currentForum" class="bg-white p-6 rounded-lg shadow">
        <!-- Cabeçalho do Fórum -->
        <div class="mb-6">
          <h1 class="text-3xl font-bold mb-4">{{ currentForum.title }}</h1>
          <p class="text-gray-600 mb-4">{{ currentForum.description }}</p>
          <div class="flex items-center text-sm text-gray-500">
            <span class="mr-4">Criado por: {{ currentForum.creator_username }}</span>
            <span>Data: {{ formatDate(currentForum.created_at) }}</span>
          </div>
        </div>

        <!-- Seção de Respostas -->
        <div class="space-y-4 mt-8">
          <h2 class="text-xl font-semibold mb-4">Respostas</h2>
          <div v-if="currentForum.replies && currentForum.replies.length > 0"
            class="space-y-4">
            <div v-for="reply in currentForum.replies" :key="reply.id"
              class="p-4 bg-gray-50 rounded-lg">
              <div class="flex justify-between items-start">
                <p class="text-gray-800">{{ reply.content }}</p>
                <div class="text-sm text-gray-500">
                  <p>{{ reply.author }}</p>
                  <p>{{ formatDate(reply.created_at) }}</p>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="text-gray-500 text-center py-4">
            Ainda não há respostas nesta discussão.
          </div>
        </div>

        <!-- Formulário de Nova Resposta -->
        <div class="mt-8">
          <h3 class="text-lg font-semibold mb-4">Adicionar Resposta</h3>
          <form @submit.prevent="submitReply" class="space-y-4">
            <textarea
              v-model="newReply"
              class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500"
              rows="4"
              placeholder="Digite sua resposta..."
            ></textarea>
            <button
              type="submit"
              class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
            >
              Enviar Resposta
            </button>
          </form>
        </div>
      </div>
      <div v-else class="text-center py-8">
        <p class="text-gray-600">Carregando...</p>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useForumStore } from '@/store/forum.js';
import MainLayout from '../layouts/mainLayout.vue';

const route = useRoute();
const forumStore = useForumStore();
const currentForum = ref(null);
const newReply = ref('');

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR');
};

const loadForumDetails = async () => {
  const forumId = route.params.id;
  currentForum.value = await forumStore.fetchForumDetails(forumId);
};

const submitReply = async () => {
  if (!newReply.value.trim()) return;
  
  try {
    await forumStore.submitReply({
      forumId: route.params.id,
      content: newReply.value
    });
    newReply.value = '';
    await loadForumDetails(); // Recarrega os detalhes do fórum para mostrar a nova resposta
  } catch (error) {
    console.error('Erro ao enviar resposta:', error);
    alert('Erro ao enviar resposta. Tente novamente.');
  }
};

onMounted(() => {
  loadForumDetails();
});
</script>
