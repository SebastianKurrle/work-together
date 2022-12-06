<template>
  <div class="mt-3 container">
    <h4 class="text-center">{{ workspace.name }}</h4>
    <p class="text-center"><b>Description:</b> {{ workspace.description }}</p>

    <div class="border p-3 mb-3">
        <div class="d-flex flex-column">
            <button class="btn btn-success mb-3">Show Chat</button>
            <button class="btn btn-success" data-bs-target="#uploadFileModal" data-bs-toggle="modal">Upload File</button>
        </div>
    </div>

    <div class="modal fade" id="uploadFileModal" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="createWorkspaceModal">Upload File</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form enctype="multipart/form-data">
                    <input type="file" ref="file" @change="selectFile" class="form-control mb-3">

                    <label for="desc" class="form-label">Description</label>
                    <textarea id="desc" cols="30" rows="5" class="form-control mb-3"></textarea>
                    <button class="btn btn-warning" :disabled="file == ''">Upload</button>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
    </div>

    <div class="border p-3 mb-3">
        <h5 class="text-center">File uploads</h5>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'WorkspaceDetailView',

    data() {
        return {
            workspace: {},
            file: ''
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
                })
        },

        selectFile(event) {
            if (event.target.files.length > 0) {
                this.file = event.target.files
            } else {
                this.file = ''
            }
        }
    },

    mounted() {
        this.getWorkspace()
    },
}
</script>

<style>

</style>