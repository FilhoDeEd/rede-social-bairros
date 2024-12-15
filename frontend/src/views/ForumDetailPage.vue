<template>
  <MainLayout>
    <div class="w-8/12 h-full py-8 pr-20 pl-20 bg-gray-50">
      <!-- Banner Section -->
      <div class="bg-white h-400-px p-6 rounded-lg shadow mb-8">
        <div class="relative h-full">
          <!-- Área colorida do banner - aumentada para 85% -->
          <div class="absolute top-0 left-0 right-0 h-85" 
               style="background-color: rgba(124, 122, 187, 1);">
          </div>

          <!-- Conteúdo do banner -->
          <div class="relative h-full flex flex-col justify-between">
            <!-- Área de título e descrição -->
            <div class="px-6 py-8">
              <div class="container mx-auto flex flex-col items-start">
                <!-- Título editável -->
                <input 
                  type="text" 
                  v-model="forumData.title" 
                  :readonly="!editMode"
                  class="text-white text-3xl font-bold mb-4 bg-transparent border-none w-full"
                  :class="{'hover:bg-gray-700/30': editMode}"
                  placeholder="Título do Fórum"
                >
                
                <!-- Descrição editável -->
                <textarea 
                  v-model="forumData.description" 
                  :readonly="!editMode"
                  class="text-white text-base mb-4 bg-transparent border-none w-full resize-none"
                  :class="{'hover:bg-gray-700/30': editMode}"
                  placeholder="Descrição do fórum"
                  rows="3"
                ></textarea>
              </div>
            </div>

            <!-- Botões alinhados ao bottom -->
            <div class="px-6 pb-4 flex space-x-4 relative z-10">
              <button type="button" 
                class="px-6 py-3 rounded-lg hover:bg-gray-100 text-white transition-colors duration-200"
                style="background-color: rgb(252, 3, 94);">
                Participar
              </button>
              
              <button type="button" 
                @click="toggleEdition"
                class="px-6 py-3 rounded-lg hover:bg-gray-100 text-white transition-colors duration-200"
                style="background-color: rgb(252, 3, 94);">
                {{ editMode ? 'Salvar' : 'Editar' }}
              </button>

              <button type="button" 
                class="px-6 py-3 rounded-lg hover:bg-gray-100 text-white transition-colors duration-200"
                style="background-color: rgb(252, 3, 94);">
                Denunciar
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow mb-8">
        <div class="container mx-auto">
          <h2 class="text-2xl font-bold mb-4">Engaje no forum!</h2>

          <!-- Área de criação de post -->
          <div class="border rounded-lg p-4">
            <div class="flex items-start space-x-4">
              <img src="https://via.placeholder.com/40" class="w-10 h-10 rounded-full" alt="Seu perfil">
              <div class="flex-1">
                <textarea
                  class="w-full p-3 rounded-lg border border-gray-200 focus:outline-none focus:border-gray-300 resize-none"
                  placeholder="No que você está pensando?" rows="3"></textarea>

                <!-- Botões de ação -->
                <div class="flex items-center mt-4 pt-3 border-t">
                  <div class="flex space-x-2">
                    <button class="p-2 hover:bg-gray-100 rounded-full" title="Adicionar foto/vídeo">
                      <span>📷</span>
                    </button>
                    <button class="p-2 hover:bg-gray-100 rounded-full" title="Localização">
                      <span>📍</span>
                    </button>
                  </div>

                  <button class="ml-auto px-6 py-2 bg-blue-500 text-Black rounded-lg hover:bg-blue-600 font-semibold">
                    Publicar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Section with Posts and Sidebar -->
      <div class="flex gap-8 space-x-4 ">
        <!-- Posts Section -->
        <div class="w-3/4">
          <div class="space-y-4">
            <article v-for="forum in forumStore.forums" :key="forum.forum_id"
              class="p-4 shadow rounded hover:shadow-lg transition-shadow duration-200"
              style="background-color: rgba(124, 122, 187, 1);">
              <div class="flex h-full">
                <div class="w-1/4 flex items-center">
                  <img src="https://via.placeholder.com/300x200" alt="Forum image" class="object-cover w-full"
                    style="height: 70%;">
                </div>
                <div class="flex-1 pl-8 text-right flex flex-col justify-between h-full">
                  <a href="#" class="text-white flex flex-col h-full justify-between">
                    <h2 :value="forum.title" class="text-4xl font-semibold mb-8">
                      {{ forum.title }}
                    </h2>
                    <div class="text-2xl text-gray-100 flex flex-col justify-between flex-grow">
                      <p class="mb-auto leading-relaxed">{{ forum.description }}</p>
                      <p class="mt-8">Popularidade: {{ forum.popularity }}</p>
                    </div>
                  </a>
                </div>
              </div>
            </article>
          </div>
        </div>

        <!-- Sidebar -->
        <aside class="w-1/4 bg-white p-4 rounded-lg shadow-lg h-fit">
          <h3 class="text-lg font-semibold mb-4">Informações Adicionais</h3>
          <div class="space-y-4">
            <div class="p-3 bg-gray-50 rounded">
              <h4 class="font-medium">Participantes</h4>
              <p class="text-gray-600">150 membros ativos</p>
            </div>
            <div class="p-3 bg-gray-50 rounded">
              <h4 class="font-medium">Criado em</h4>
              <p class="text-gray-600">15 de Janeiro, 2024</p>
            </div>
            <div class="p-3 bg-gray-50 rounded">
              <h4 class="font-medium">Criado por</h4>
              <p class="text-gray-600">Usuário</p>
            </div>
            <div class="p-3 bg-gray-50 rounded">
              <h4 class="font-medium">Popularidade</h4>
              <div class="flex flex-wrap gap-2 mt-2">
                <span class="px-2 py-1 bg-blue-100 text-blue-800 rounded text-sm">Alta</span>
              </div>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </MainLayout>
</template>

<script setup>
import MainLayout from '../layouts/mainLayout.vue';
import { useForumStore } from '@/store/forum.js';
import { onBeforeMount, ref } from 'vue';

const forumStore = useForumStore();
const editMode = ref(false);
const forumData = ref({
  title: 'Como melhorar a segurança do nosso bairro?',
  description: 'Participe da discussão e compartilhe suas ideias para uma comunidade mais segura'
});

const toggleEdition = () => {
  if (editMode.value) {
    // Aqui você implementaria a lógica para salvar as alterações
    saveChanges();
  }
  editMode.value = !editMode.value;
};

const saveChanges = async () => {
  try {
    // Implementar a lógica de salvamento aqui
    // await forumStore.updateForumDetails(forumData.value);
    alert('Alterações salvas com sucesso!');
  } catch (error) {
    alert('Erro ao salvar as alterações');
  }
};

onBeforeMount(() => {
  forumStore.fetchForums(1);
});
</script>

<style scoped>
.h-85 {
  height: 85%;
}

.h-400-px {
  height: 400px;
}

input:focus, textarea:focus {
  outline: none;
}

input::placeholder, textarea::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

/* Adicionando transição suave para hover dos botões */
button {
  transition: all 0.2s ease-in-out;
}

button:hover {
  transform: translateY(-1px);
}
</style>
