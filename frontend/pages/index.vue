<template>
  <div class="container">
    <div>
      <h1 class="title">
        Fire Detection using deep CNN
      </h1>
      <div class="links">
        <NuxtLink to="/monitor" class="button--green py-4 px-8">Monitor</NuxtLink>
        <NuxtLink to="/cameras" class="button--green py-4 px-8">Cameras</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    layout: 'main'
  }

</script>

<style scoped>
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .title {
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
    margin: 2rem 0;
    line-height: 1;
  }

  .subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }

  .links {
    padding-top: 15px;
  }

</style>
