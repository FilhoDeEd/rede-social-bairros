<template>
  <main-layout>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold text-gray-800 mb-8">Sobre Nós</h1>

      <div class="bg-white rounded-lg shadow-md p-8">
        <section class="mb-8">
          <h2 class="text-2xl font-semibold mb-4">Nossa Missão</h2>
          <p class="text-gray-600 leading-relaxed">
            Somos dedicados a criar um espaço seguro e acolhedor para a comunidade LGBTQIA+, 
            promovendo inclusão, respeito e apoio mútuo através de nossa plataforma digital.
          </p>
        </section>

        <section class="mb-8">
          <h2 class="text-2xl font-semibold mb-4">O Que Fazemos</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-4 bg-gray-50 rounded-lg">
              <h3 class="text-xl font-medium mb-2">Comunidade</h3>
              <p class="text-gray-600">
                Facilitamos conexões significativas através de nosso fórum e eventos comunitários.
              </p>
            </div>
            <div class="p-4 bg-gray-50 rounded-lg">
              <h3 class="text-xl font-medium mb-2">Suporte</h3>
              <p class="text-gray-600">
                Oferecemos um sistema de denúncias e moderação para manter nossa comunidade segura.
              </p>
            </div>
          </div>
        </section>

        <section>
          <h2 class="text-2xl font-semibold mb-4">Entre em Contato</h2>
          <p class="text-gray-600 mb-4">
            Tem alguma dúvida ou sugestão? Ficaremos felizes em ouvir você.
          </p>
          <button class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition duration-300">
            Contate-nos
          </button>
        </section>
      </div>
    </div>
  </main-layout>
</template>

<script setup>
import MainLayout from "@/layouts/mainLayout.vue";
</script>
