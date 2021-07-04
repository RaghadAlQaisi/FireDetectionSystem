<template>
  <div class="grid grid-cols-7">
    <h3 class="py-2 col-span-2">{{cameraData.name}}</h3>
    <h3 class="mx-8 flex-grow px-4 py-2 col-span-4">Url: {{cameraData.location}}</h3>
    <span class="flex flex-row flex-nowrap col-span-1 justify-end">
      <i class="ri-edit-2-line" @click="$emit('startEdit')"></i>
      <i class="ri-delete-bin-line" @click="$emit('deleteCamera', cameraData.id)"></i>
    </span>
  </div>
</template>

<script>
  export default {
    props: {
      cameraData: {
        type: Object,
        required: true
      }
    }
  }

</script>
