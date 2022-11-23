<template>
  <div class="mt-3">
    <h5 class="text-center">Create Organization</h5>

    <div class="container border p-3">
      <form @submit.prevent="submitForm" method="post">
        <label for="orgName" class="form-label">Organization Name*</label>
        <input
          type="text"
          id="orgName"
          class="form-control"
          v-model="name"
        />

        <label for="desc" class="form-label">Description*</label>
        <textarea
          id="desc"
          cols="30"
          rows="10"
          class="form-control"
          v-model="desc"
        ></textarea>

        <div
          class="bg-danger text-white p-3 mb-3 mt-3 rounded"
          v-if="errors.length"
        >
          <p v-for="error in errors" :key="error">{{ error }}</p>
        </div>

        <button class="btn btn-success mt-3">Create</button>
      </form>
    </div>
  </div>
</template>
  
  <script>
import axios from "axios";

export default {
  name: "CreateOrgView",

  data() {
    return {
      name: "",
      desc: "",
      errors: [],
    };
  },

  methods: {
    async submitForm() {
      this.errors = [];

      if (this.name.trim() === "") {
        this.errors.push("The name field is empty");
      }

      if (this.desc.trim() === "") {
        this.errors.push("The description field is empty");
      }

      if (!this.errors.length) {
        const formData = {
          name: this.name,
          description: this.desc,
        };

        await axios
          .post("/api/org/create/", formData)
          .then((response) => {
            this.$router.push('/organizations')
          })
          .catch((error) => {
            console.log(error);

            if (error.response.data.name) {
                this.errors.push('An organization with this name already exists!')
                this.name = ''
                this.desc = ''
            } else {
                this.errors.push("Something went wront please try again");
            }
          });
      }
    },
  },
};
</script>