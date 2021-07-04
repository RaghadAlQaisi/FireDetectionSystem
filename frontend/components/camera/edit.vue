<template>
  <div class="grid grid-cols-7">
    <input v-model="camera.name" placeholder="Camera name" required class="col-span-2">
    <input v-model="camera.location" placeholder="Camera url" required class="col-span-4 mx-8 flex-grow px-4 py-2">
    <span class="flex flex-row flex-nowrap col-span-1 justify-end">
      <i class="ri-save-3-line" @click="$emit('saveEdit', camera)"></i>
      <i class="ri-close-line" @click="clearData"></i>
    </span>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        camera: {
          name: this.cameraData.name,
          location: this.cameraData.location
        }
      }
    },
    props: {
      cameraData: {
        type: Object,
        required: true
      },
      newCamera: {
        type: Boolean
      }
    },
    methods: {
      clearData() {
        this.newCamera ?
          this.camera = {
            name: '',
            location: ''
          } :
          this.camera = {
            name: this.cameraData.name,
            location: this.cameraData.location
          }
        this.$emit('discardEdit')
      }
    }
  }

</script>

<style scoped>
  input {
    @apply text-xl leading-7 border border-solid border-grey-default border-opacity-20 px-4 py-2;
  }

</style>
