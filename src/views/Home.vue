<template>
  <div class="home">
    <home-detail/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeDetail from '../components/HomeDetail.vue'

export default {
  name: 'Home',
  components: {
    HomeDetail
  }
}
</script>

<style lang="scss">
.home {
  width: 100%;
}
</style>

