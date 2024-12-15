<template>
  <MainLayout>
    <div class="w-8/12 h-full py-8 pr-20 pl-20 bg-gray-50 space-y-4">
      <main>
        <section id="conteudo">
          <h1 class="text-xl font-bold mb-4">Seus Fóruns</h1>
          <div class="space-y-4">
            <article 
              @click="goToForumDetail"
              class="p-4 shadow rounded hover:shadow-lg transition-shadow duration-200 bg-white cursor-pointer"
            >
              <div class="flex justify-between items-start">
                <div class="flex-1">
                  <h2 class="text-2xl font-semibold mb-2">Título do Fórum</h2>
                  <p class="text-gray-600 mb-4">Descrição do Fórum</p>
                  <div class="flex items-center text-sm text-gray-500">
                    <span class="mr-4">Criado por: Usuário</span>
                    <span>Data: 01/01/2024</span>
                  </div>
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
import { useRouter } from 'vue-router'
import MainLayout from '../layouts/mainLayout.vue'

const router = useRouter()

const goToForumDetail = () => {
  router.push('/forum-detail-page')
}
</script>

<style scoped>
.bg-white {
  background-color: #ffffff;
}

article:hover {
  cursor: pointer;
  transform: translateY(-2px);
  transition: all 0.2s ease;
}
</style>
