<template>
  <div>
    <h1>Workspace</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'WorkspaceDetailView',

    data() {
        return {
            workspace: {}
        }
    },

    methods: {
        async getWorkspace() {
            const org_slug = this.$route.params.org_slug
            const workspace_slug = this.$route.params.workspace_slug

            axios
                .get(`/api/workspace/get/${org_slug}/${workspace_slug}/`)
                .then(response => {
                    this.workspace = response.data
                    console.log(this.workspace)
                })
        }
    },

    mounted() {
        this.getWorkspace()
    },
}
</script>

<style>

</style>