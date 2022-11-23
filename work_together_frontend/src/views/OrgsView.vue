<template>
  <div class="mt-3">
    <h5 class="text-center">Your Organizations</h5>

    <div class="container text-center mt-3 border p-3">
      <div class="row row-cols-3">
        <div class="card m-3" v-for="org in organizations" :key="org.id">
          <div class="card-header">
            {{ org.name }}
          </div>
          <div class="card-body">
            <h5 class="card-title">Description</h5>
            <p class="card-text">{{ org.description }}</p>
            <router-link :to="org.get_absolute_url" class="btn btn-primary">Visit</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";
export default {
  name: "OrgsView",

  data() {
    return {
      organizations: [],
    };
  },

  methods: {
    getOrganizations() {
      axios
        .get("/api/orgs/")
        .then((response) => {
          this.organizations = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getOrganizations();
    document.title = "Organizations | WorkTogehter";
  },
};
</script>