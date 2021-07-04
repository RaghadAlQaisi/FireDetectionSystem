<template>
  <div>
    <CameraEdit :cameraData="camera" @saveEdit="saveCamera" newCamera />
  </div>
</template>

<script>
  export default {
    data() {
      return {
        camera: {
          name: '',
          location: ''
        }
      }
    },
    methods: {
      saveCamera(camera) {
        if (confirm('Add camera?')) {
          let newCamera = {
            name: camera.name,
            location: camera.location
          }
          this.$store.dispatch('editCamera', newCamera)
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
