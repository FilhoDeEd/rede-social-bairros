<template>
  <main-layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold text-gray-800 mb-8">Eventos da Comunidade</h1>

      <!-- Seção de Criação de Evento -->
      <div class="mb-8">
        <button 
          class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition duration-300"
        >
          Criar Novo Evento
        </button>
      </div>

      <!-- Lista de Eventos -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Card de Evento -->
        <div 
          v-for="n in 6" 
          :key="n"
          class="bg-white rounded-lg shadow-md overflow-hidden"
        >
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2">Nome do Evento</h3>
            <p class="text-gray-600 mb-4">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
              Sed do eiusmod tempor incididunt ut labore.
            </p>
            <div class="flex items-center text-gray-500 mb-4">
              <span class="material-icons mr-2">calendar_today</span>
              <span>20 de Dezembro, 2023</span>
            </div>
            <div class="flex items-center text-gray-500 mb-4">
              <span class="material-icons mr-2">location_on</span>
              <span>Local do Evento</span>
            </div>
            <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition duration-300">
              Ver Detalhes
            </button>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/mainLayout.vue";
</script>
