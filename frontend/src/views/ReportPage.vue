<template>
  <main-layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold text-gray-800 mb-8">Denúncias</h1>

      <!-- Seção de Nova Denúncia -->
      <div class="mb-8">
        <button 
          class="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition duration-300"
        >
          Fazer Nova Denúncia
        </button>
      </div>

      <!-- Lista de Denúncias -->
      <div class="grid grid-cols-1 gap-4">
        <!-- Card de Denúncia -->
        <div 
          v-for="n in 5" 
          :key="n"
          class="bg-white rounded-lg shadow-md p-6"
        >
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-xl font-semibold mb-2">Título da Denúncia</h3>
              <p class="text-gray-600">
                Descrição detalhada da denúncia feita pelo usuário...
              </p>
            </div>
            <span class="px-3 py-1 rounded-full text-sm" 
                  :class="{
                    'bg-yellow-100 text-yellow-800': n % 3 === 0,
                    'bg-red-100 text-red-800': n % 3 === 1,
                    'bg-green-100 text-green-800': n % 3 === 2
                  }"
            >
              {{ n % 3 === 0 ? 'Em Análise' : n % 3 === 1 ? 'Pendente' : 'Resolvido' }}
            </span>
          </div>
          <div class="flex items-center text-gray-500 mb-2">
            <span class="material-icons mr-2 text-sm">person</span>
            <span>Usuário Denunciante</span>
          </div>
          <div class="flex items-center text-gray-500">
            <span class="material-icons mr-2 text-sm">calendar_today</span>
            <span>{{ new Date().toLocaleDateString('pt-BR') }}</span>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/mainLayout.vue";
</script>
