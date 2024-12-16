<template>
  <router-link :to="path" class="block">
    <div 
      class="flex items-center px-4 py-2 text-gray-100 transition-all duration-300 ease-in-out hover:scale-105 cursor-pointer hover:bg-white/10"
    >
      <span class="material-icons mr-3">{{ icon }}</span>
      <span class="font-medium">{{ title }}</span>
    </div>
  </router-link>
</template>

<style scoped>
.router-link-active div {
  transform: scale(1);
  background-color: rgba(224, 82, 74, .30);
}
</style>

<script>
export default {
  props: {
    icon: String,
    title: String,
    path: String,
    active: Boolean,
  },
};
</script> 