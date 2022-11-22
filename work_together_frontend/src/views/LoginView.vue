<template>
  <div>
      <div class="d-flex justify-content-center mt-3">
          <div class="container">
              <h3 class="text-center">Login</h3>
  
              <form @submit.prevent="submitForm">
                  <div class="border p-3">
                      <div class="mb-3">
                          <label for="username" class="form-label">Username*</label>
                          <input type="text" id="username" class="form-control" v-model="username">
  
                          <label for="password1" class="form-label">Password*</label>
                          <input type="password" id="password1" class="form-control" v-model="password">
                      </div>
  
                      <div class="bg-danger text-white p-3 mb-3 rounded" v-if="errors.length">
                          <p v-for="error in errors" :key="error">{{ error }}</p>
                      </div>
  
                      <button class="btn btn-success">Login</button>
  
                      <hr/>
  
                      Or <router-link to="/register">click here</router-link> to register!
                  </div>
              </form>
              
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'LoginView',

  data() {
      return {
          username: '',
          password: '',
          errors: []
      }
  },

  mounted() {
      document.title = 'Log In | WorkTogether'
  },

  methods: {
      async submitForm() {
          this.errors = []
          axios.defaults.headers.common['Authorization'] = ''

          localStorage.removeItem('token')

          const formData = {
              username: this.username,
              password: this.password
          }

          await axios
              .post('/api/login/', formData)
              .then(response => {
                  const token = response.data.token
                  this.$store.commit('setToken', token)

                  axios.defaults.headers.common['Authorization'] = 'Token ' + token

                  localStorage.setItem('token', token)
                  localStorage.setItem('username', response.data.user_info.username)

                  const toPath = this.$route.query.to || '/'
                  this.$router.push(toPath)
              })
              .catch(error => {
                  if (error.response) {
                      for (const property in error.response.data) {
                          this.errors.push(`${property}: ${error.response.data[property]}`)
                      }

                      console.log(JSON.stringify(error.response.data))
                  } else if (error.message) {
                      this.errors.push('Something went wrong, Please try again')

                      console.log(JSON.stringify(error))
                  }
              })
      },
      }
}
</script>