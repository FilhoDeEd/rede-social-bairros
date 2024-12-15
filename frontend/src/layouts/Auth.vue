<template>
  <main class="relative min-h-screen">
    <navbar/>
    <section class="relative w-full h-full pb-32   min-h-screen">
      <div
        class="absolute top-0 w-full h-full bg-blueGray-800 bg-no-repeat bg-full"
        :style="`background-image: url('${registerBg2}');`"
      ></div>
      <router-view />
      <footer-small absolute />
    </section>
  </main>
</template>

<script>
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterSmall from "@/components/Footers/FooterSmall.vue";
import registerBg2 from "@/assets/img/register_bg_2.png";

export default {
  data() {
    return {
      registerBg2,
    };
  },
  components: {
    Navbar,
    FooterSmall,
  },
};
</script>
