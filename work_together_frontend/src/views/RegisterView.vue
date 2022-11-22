<template>
  <div>
    <div class="d-flex justify-content-center mt-3">
      <div class="container">
        <h3 class="text-center">Register</h3>

        <form @submit.prevent="submitForm">
          <div class="border p-3">
            <div class="mb-3">
              <label for="username" class="form-label">Username*</label>
              <input
                type="text"
                id="username"
                class="form-control"
                v-model="username"
              />

              <label for="email" class="form-label">Email*</label>
              <input
                type="email"
                id="email"
                class="form-control"
                v-model="email"
              />

              <label for="firstnaem" class="form-label">First Name*</label>
              <input
                type="text"
                id="firstname"
                class="form-control"
                v-model="first_name"
              />

              <label for="lastname" class="form-label">Last Name*</label>
              <input
                type="text"
                id="lastname"
                class="form-control"
                v-model="last_name"
              />

              <label for="password1" class="form-label">Password*</label>
              <input
                type="password"
                id="password1"
                class="form-control"
                v-model="password"
              />

              <label for="password2" class="form-label"
                >Password Confrime*</label
              >
              <input
                type="password"
                id="password2"
                class="form-control"
                v-model="password2"
              />
            </div>

            <div
              class="bg-danger text-white p-3 mb-3 rounded"
              v-if="errors.length"
            >
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <button class="btn btn-success">Register</button>

            <hr />

            Or <router-link to="/login">click here</router-link> to log in!
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
  <script>
import axios from "axios";
import Toastify from "toastify-js";

export default {
  name: "RegisterView",

  data() {
    return {
      username: "",
      email: "",
      first_name: "",
      last_name: "",
      password: "",
      password2: "",
      errors: [],
    };
  },

  mounted() {
    document.title = "Register | WorkTogether";
  },

  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }

      if (this.email === '') {
        this.errors.push('The email field is missing')
      }

      if (this.first_name === '') {
        this.errors.push('The first name field is missing')
      }

      if (this.last_name === '') {
        this.errors.push('The last name field is missing')
      }

      if (this.password === "") {
        this.errors.push("The password is missing");
      }

      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn`t match");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        };

        axios 
          .post('/api/register/', formData)
          .then((response) => {
            Toastify({
              text: "Account has been created",
              duration: 3000,
              close: true,
              gravity: "bottom",
              position: "right",
              stopOnFocus: true,

              style: {
                background: "green",
              },
            }).showToast();
            
            console.log(response)

            this.$router.push("/login");
          })
          .catch((error) => {
            console.log(error);

            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }

              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong, Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>