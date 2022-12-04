<template>
  <div>
    <h1>Workspace</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            workspace: {}
        }
    },

    methods: {
        async getWorkspace() {
            axios
                .get(`/api/workspace/get/$`)
        }
    },

    props: {
        workspaceId: Number
    }
}
</script>

<style>

</style>