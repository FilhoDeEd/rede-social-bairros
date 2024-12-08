<template>
  <nav
    class="top-0 fixed z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg bg-white shadow">
    <div class="container px-4 mx-auto flex flex-wrap items-start justify-between">
      <div class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
        <router-link
          class="fredoka text-black text-smleading-relaxed inline-block mr-2 py-2 whitespace-nowrap uppercase " to="/">
          Bonds
        </router-link>
        <button
          class="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button" v-on:click="setNavbarOpen">
          <i class="fas fa-bars"></i>
        </button>
      </div>

      <div class="search-bar">
        <input type="email" placeholder="Search Something..." />
        <button type='button'>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192.904 192.904">
            <path
              d="m190.707 180.101-47.078-47.077c11.702-14.072 18.752-32.142 18.752-51.831C162.381 36.423 125.959 0 81.191 0 36.422 0 0 36.423 0 81.193c0 44.767 36.422 81.187 81.191 81.187 19.688 0 37.759-7.049 51.831-18.751l47.079 47.078a7.474 7.474 0 0 0 5.303 2.197 7.498 7.498 0 0 0 5.303-12.803zM15 81.193C15 44.694 44.693 15 81.191 15c36.497 0 66.189 29.694 66.189 66.193 0 36.496-29.692 66.187-66.189 66.187C44.693 147.38 15 117.689 15 81.193z">
            </path>
          </svg>
        </button>
      </div>



    </div>
  </nav>
</template>

<script>


export default {
  data() {
    return {
      navbarOpen: false,
    };
  },
  methods: {
    setNavbarOpen: function () {
      this.navbarOpen = !this.navbarOpen;
    },
  },
  components: {

  },
};
</script>

<style>
.search-bar {
  width: 100%;
  max-width: 500px;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  border: 2px solid #007bff;
  margin: 0 auto;
}

.search-bar input {
  flex: 1;
  padding: 16px;
  font-size: 16px;
  border: none;
  outline: none;
}

.search-bar button {
  background-color: #007bff;
  color: white;
  padding: 0 20px;
  border: none;
  cursor: pointer;
}

.search-bar button svg {
  width: 20px;
}
</style>