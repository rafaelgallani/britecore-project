<template>
  <div class="home-card">
    <h2 class="title">{{title}}</h2>
    <main class="actions">
      <slot></slot>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HomeCard',
  props: {
    title: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  .title {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .actions {
    width: 100%;
    display: flex;
    flex-wrap: nowrap;
    padding: 10px;
  }

  .home-card + .home-card{
    margin-top: 50px;
  }
</style>
