<template>
  <footer class="sticky bg-blueGray-200 h-16 flex items-center">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-center">
        <div class="text-sm text-blueGray-500 font-semibold text-center">
          Copyright © {{ date }} <br />
          <p class="fredoka mt-1">Bonds</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      date: new Date().getFullYear(),
    };
  },
};
</script>

<style>
.fredoka {
  font-family: 'fredoka';
}
</style>
