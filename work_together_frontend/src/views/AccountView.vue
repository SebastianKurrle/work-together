<template>
  <div class="container mt-3">
    <h3>Your Account</h3>

    <p>Loged in as {{ username }}</p>

    <button class="btn btn-danger" @click="logout">Logout</button>
  </div>
</template>
  
  <script>
import axios from "axios";

export default {
  name: "AccountView",

  data() {
    return {
      username: localStorage.getItem("username"),
    };
  },

  methods: {
    logout() {
      axios
        .post("/api/logout/")
        .then((response) => {
          console.log(response);
          this.$router.push("/login");
        })
        .catch((error) => {
          console.log(error);
        });

      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },

  mounted() {
    document.title = "Account | WorkTogehter";
  },
};
</script>