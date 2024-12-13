<template>
    <div v-if="isSimpleConfirmModalOpen" class="modal-overlay">
      <div class="modal-content">
        <button class="close-btn" @click="closeModal">X</button>
  
        <!-- Conteúdo do modal -->
        <form @submit.prevent="handleConfirm">
          <!-- Botão Confirmar -->
           <h2>Deseja mesmo Realizar a operação?</h2>
          <div class="text-center mt-6">
            <button
              type="submit"
              class="bg-indigo-500 text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none ease-linear transition-all duration-150"
            >
              Confirmar
            </button>
  
            <!-- Botão Cancelar -->
            <button
              type="button"
              @click="closeModal"
              class="bg-red-500 text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none ease-linear transition-all duration-150"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isSimpleConfirmModalOpen: Boolean, // Propriedade para controlar se o modal está aberto
    },
  
    methods: {
      // Fechar o modal
      closeModal() {
        this.$emit('close'); // Emite evento para o componente pai fechar o modal
      },
  
      // Submissão do formulário de confirmação
      handleConfirm() {
        this.$emit("confirm",true); // Emite evento de confirmação
        this.closeModal(); // Fecha o modal após confirmação
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilo para o modal */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5); /* Fundo opaco */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
    max-width: 90%;
    position: relative;
  }
  
  .close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: transparent;
    border: none;
    font-size: 18px;
    cursor: pointer;
    color: #333;
  }
  </style>
  