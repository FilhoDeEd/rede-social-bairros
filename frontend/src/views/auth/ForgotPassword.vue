<template>
    <div v-if="isVisible" class="modal-overlay">
      <div class="modal-content">
        <button @click="closeModal" class="close-button">X</button>
        <h2>{{ title }}</h2>
  
        <!-- Formulário -->
        <div>
          <label for="email">Email:</label>
          <input 
            type="email" 
            v-model="email" 
            :disabled="isSending" 
            placeholder="Digite seu email" 
            class="input-field" 
          />
        </div>
  
        <div class="mt-4">
          <label for="token">Token de autenticação:</label>
          <input 
            type="text" 
            v-model="token" 
            :disabled="!isEmailSent" 
            placeholder="Digite o token recebido" 
            class="input-field" 
          />
        </div>
  
        <!-- Botão de enviar -->
        <div class="mt-6">
          <button 
            @click="handleSubmit" 
            :disabled="isSending" 
            class="submit-button"
          >
            {{ isEmailSent ? "Enviar Token" : "Enviar Email" }}
          </button>
        </div>
  
        <!-- Link de Reenvio -->
        <div class="mt-4">
          <a 
            href="javascript:void(0)" 
            @click="handleResendCode" 
            :class="{ disabled: isResendDisabled }"
            :style="{ color: isResendDisabled ? '#999' : '#007bff' }"
          >
            Reenviar código
          </a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ENDPOINTS } from '../../../../api';
  export default {
    props: {
      title: {
        type: String,
        default: "Esqueci minha senha",
      },
      isVisible: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        email: "",
        token: "",
        isEmailSent: false,
        isSending: false,
        isResendDisabled: false,
      };
    },
    methods: {
      closeModal() {
        this.$emit("close");
      },
      async handleSubmit() {
        this.isSending = true;
  
        if (!this.isEmailSent) {
          // Enviar email
          try {
            await this.sendEmail(this.email);
            this.isEmailSent = true;
          } catch (error) {
            alert("Erro ao enviar email: " + error);
          }
        } else {
          // Enviar token
          try {
            await this.verifyToken(this.token);
            alert("Token verificado com sucesso!");
            this.closeModal();
          } catch (error) {
            alert("Erro ao verificar token: " + error);
          }
        }
  
        this.isSending = false;
      },
      async handleResendCode() {
        if (this.isResendDisabled) return;
  
        this.isResendDisabled = true;
        try {
          await this.sendEmail(this.email);
          alert("Código reenviado com sucesso!");
        } catch (error) {
          alert("Erro ao reenviar código: " + error);
        }
  
        // Desabilitar reenvio por 30 segundos
        setTimeout(() => {
          this.isResendDisabled = false;
        }, 30000);
      },
      async sendEmail(email) {
       const dataToSend = { email };
  
        const response = await fetch(ENDPOINTS.VERIFYTOKEN, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(dataToSend),
        });
  
        if (response.ok) {
          const data = await response.json();
          return data.message || "E-mail enviado com sucesso!";
        } else {
          const errorText = await response.text();
          throw errorText;
        }
      },
      async verifyToken(token) {
        const dataToSend = { token };
  
        const response = await fetch(ENDPOINTS.VERIFYTOKEN, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(dataToSend),
        });
  
        if (response.ok) {
          const data = await response.json();
          return data.message || "Token verificado!";
        } else {
          const errorText = await response.text();
          throw errorText;
        }
      },
    },
  };
  </script>
  
  <style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
    color: black;
    position: relative;
  }
  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
  }
  .input-field {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .submit-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .submit-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  .disabled {
    pointer-events: none;
  }
  </style>
  