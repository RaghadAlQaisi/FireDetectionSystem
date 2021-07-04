<template>
  <div>
    <CameraView v-if="!edit" :cameraData="camera" @startEdit="editToggle(true)" @deleteCamera="deleteCamera" />
    <CameraEdit v-show="edit" :cameraData="camera" @discardEdit="editToggle(false)" @saveEdit="saveCamera" />
  </div>
</template>

<script>
  export default {
    data() {
      return {
        edit: false,
        camera: {
          id: this.cameraData.id,
          name: this.cameraData.name,
          location: this.cameraData.location
        }
      }
    },
    props: {
      cameraData: {
        type: Object,
        required: true
      }
    },
    methods: {
      editToggle(value) {
        this.edit = value
      },
      async saveCamera(camera) {
        if (confirm('Confirm save?')) {
          let newCamera = {
            id: this.camera.id,
            name: camera.name,
            location: camera.location
          }
          await this.$store.dispatch('editCamera', newCamera).then()
          this.camera = this.$store.state.camerasList.filter(cam => cam.id == newCamera.id)[0]
          this.edit = false
        } else {
          console.log('Canceled')
        }
      },
      deleteCamera(id) {
        if (confirm('Are you sure you want to delete this camera?')) {
          this.$store.dispatch('deleteCamera', id)
        } else {
          console.log('Canceled')
        }
      }
    }
  }

</script>

<style>
  .ri-edit-2-line:hover,
  .ri-save-3-line:hover {
    @apply text-green-default;
  }

  .ri-delete-bin-line:hover,
  .ri-close-line:hover {
    @apply text-red-700;
  }

</style>
