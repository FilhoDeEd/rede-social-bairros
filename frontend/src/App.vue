
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
</style>

<script>
  import axios from 'axios';
  import { useUserStore } from '@/store/user';
  import { onBeforeMount } from 'vue';

  export default {
    setup() {
      const userStore = useUserStore();
      
      onBeforeMount(() => {
        userStore.initStore();

        const token = userStore.user.access;

        if (token) {
          axios.defaults.headers.common["Authorization"] = "Token " + token;
        } else {
          axios.defaults.headers.common["Authorization"] = "";
        }
      });

      return {
        userStore
      };
    }
  };
</script>