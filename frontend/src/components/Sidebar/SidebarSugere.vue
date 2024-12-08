<template>
  <nav
    class="md:right-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6"
  >
    <div
      class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
    >
      <!-- Toggler -->
    </div>
  </nav>
</template>

<script>
/*import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";*/
import { ref } from "vue";

export default {
  name: "Sidebar",
  components: {
    /*NotificationDropdown,
    UserDropdown,*/
  },
  setup() {
    const collapseShow = ref("hidden");

    function toggleCollapseShow() {
      collapseShow.value =
        collapseShow.value === "hidden" ? "block" : "hidden";
    }

    return {
      collapseShow,
      toggleCollapseShow,
    };
  },
};
</script>

<style scoped>
/* Custom styles for sidebar positioning on the right */
.md\\:right-0 {
  right: 0 !important;
}

.md\\:fixed {
  position: fixed !important;
}

.md\\:w-64 {
  width: 16rem !important;
}
</style>
