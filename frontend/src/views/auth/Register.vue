<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-6/12 px-4">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
          <div class="flex-auto px-4 lg:px-10 py-10">
            <form @submit.prevent="handleSubmit">
              <div class="flex gap-4 space-x-4">
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">First Name</label>
                  <input
                    type="text"
                    v-model="form.firstName"
                    @change="validateField('firstName')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="First Name"
                  />
                  <p v-if="errors.firstName" class="text-red-500 text-xs">{{ errors.firstName }}</p>
                </div>
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Last Name</label>
                  <input
                    type="text"
                    v-model="form.lastName"
                    @change="validateField('lastName')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Last Name"
                  />
                  <p v-if="errors.lastName" class="text-red-500 text-xs">{{ errors.lastName }}</p>
                </div>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Data de Nascimento</label>
                <input
                  type="date"
                  v-model="form.birthDate"
                  @change="validateField('birthDate')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                />
                <p v-if="errors.birthDate" class="text-red-500 text-xs">{{ errors.birthDate }}</p>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Email</label>
                <input
                  type="email"
                  v-model="form.email"
                  @change="validateField('email')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email"
                />
                <p v-if="errors.email" class="text-red-500 text-xs">{{ errors.email }}</p>
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Username</label>
                <input
                  type="text"
                  v-model="form.username"
                  @change="validateField('username')"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Username"
                />
                <p v-if="errors.username" class="text-red-500 text-xs">{{ errors.username }}</p>
              </div>

              <div class="flex gap-4 space-x-4">
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Password</label>
                  <input
                    type="password"
                    v-model="form.password"
                    @change="validateField('password')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Password"
                  />
                  <p v-if="errors.password" class="text-red-500 text-xs">{{ errors.password }}</p>
                </div>
                <div class="relative w-full mb-3">
                  <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2">Confirm Password</label>
                  <input
                    type="password"
                    v-model="form.confirmPassword"
                    @change="validateField('confirmPassword')"
                    class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                    placeholder="Confirm Password"
                  />
                  <p v-if="errors.confirmPassword" class="text-red-500 text-xs">{{ errors.confirmPassword }}</p>
                </div>
              </div>

              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input
                    id="customCheckLogin"
                    type="checkbox"
                    v-model="form.agree"
                    @change="validateField('agree')"
                    class="form-checkbox border-0 rounded text-blueGray-700 ml-1 w-5 h-5 ease-linear transition-all duration-150"
                  />
                  <span class="ml-2 text-sm font-semibold text-blueGray-600">
                    I agree with the
                    <a href="javascript:void(0)" class="text-emerald-500">Privacy Policy</a>
                  </span>
                </label>
                <p v-if="errors.agree" class="text-red-500 text-xs">{{ errors.agree }}</p>
              </div>

              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                  type="submit"
                >
                  Create Account
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      form: {
        firstName: "",
        lastName: "",
        birthDate: "",
        email: "",
        username: "",
        password: "",
        confirmPassword: "",
        agree: false,
      },
      errors: {},
    };
  },
  methods: {
    validateField(field) {
      // Helper function para calcular idade
      const calculateAge = (birthDate) => {
        const today = new Date();
        const birth = new Date(birthDate);
        let age = today.getFullYear() - birth.getFullYear();
        const monthDifference = today.getMonth() - birth.getMonth();
        if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birth.getDate())) {
          age--;
        }
        return age;
      };

      switch (field) {
        case "firstName":
          this.errors.firstName = this.form.firstName ? "" : "First Name is required.";
          break;
        case "lastName":
          this.errors.lastName = this.form.lastName ? "" : "Last Name is required.";
          break;
        case "birthDate":
          if (!this.form.birthDate) {
            this.errors.birthDate = "Birth Date is required.";
          } else if (calculateAge(this.form.birthDate) < 16) {
            this.errors.birthDate = "You must be at least 16 years old.";
          } else {
            this.errors.birthDate = "";
          }
          break;
        case "email":
          if (!this.form.email) {
            this.errors.email = "Email is required.";
          } else if (!/\S+@\S+\.\S+/.test(this.form.email)) {
            this.errors.email = "Invalid email format.";
          } else {
            this.errors.email = "";
          }
          break;
        case "username":
          this.errors.username = this.form.username ? "" : "Username is required.";
          break;
        case "password":
          this.errors.password = this.form.password ? "" : "Password is required.";
          break;
        case "confirmPassword":
          if (!this.form.confirmPassword) {
            this.errors.confirmPassword = "Confirm Password is required.";
          } else if (this.form.password !== this.form.confirmPassword) {
            this.errors.confirmPassword = "Passwords do not match.";
          } else {
            this.errors.confirmPassword = "";
          }
          break;
        case "agree":
          this.errors.agree = this.form.agree ? "" : "You must agree to the Privacy Policy.";
          break;
      }
    },
    async handleSubmit() {
      // Validate all fields before submission
      Object.keys(this.form).forEach((field) => this.validateField(field));

      if (Object.keys(this.errors).some((key) => this.errors[key])) return;

      try {
        const response = await fetch("http://sua-api.com/api/register/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form),
        });
        if (!response.ok) throw new Error("Failed to register.");
        alert("Account created successfully!");
      } catch (error) {
        alert(error.message);
      }
    },
  },
};
</script>
