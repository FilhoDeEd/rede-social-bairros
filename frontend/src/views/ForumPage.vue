<template>
  <MainLayout>
    <div class="w-8/12 h-full py-8 pr-20 pl-20 bg-gray-50 space-y-4">
      <main>
        <section id="conteudo">
          <h1 class="text-xl font-bold mb-4">Discussões</h1>
          <div class="space-y-4">
            <article class="p-4 shadow rounded hover:shadow-lg transition-shadow duration-200 bg-white">
              <div class="flex justify-between items-start">
                <div class="flex-1">
                  <h2 class="text-2xl font-semibold mb-2">Título da Discussão</h2>
                  <p class="text-gray-600 mb-4">Descrição da discussão aqui...</p>
                  <div class="flex items-center text-sm text-gray-500">
                    <span class="mr-4">Criado por: Usuário</span>
                    <span>Data: 01/01/2024</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-sm text-gray-500">10 respostas</span>
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
import MainLayout from '../layouts/mainLayout.vue'
</script>

<style scoped>
.bg-white {
  background-color: #ffffff;
}
</style>
