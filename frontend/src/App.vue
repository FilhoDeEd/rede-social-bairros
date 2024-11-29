
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
</style>

<script>
import { onBeforeMount } from 'vue';
import { useUserStore } from './store/user';
import axios from 'axios';

export default {
  setup() {
    const userStore = useUserStore();
    
    onBeforeMount(() => {
      userStore.initStore();

      const token = userStore.user.access;

      if (token) {
        axios.defaults.headers.common["Authorization"] = "Bearer " + token;
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