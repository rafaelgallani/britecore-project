<template>
  <div class="action-card">
    <b class="title">{{title}}</b>
    <span class="description">{{description}}</span>
  </div>
</template>

<script>
export default {
  name: 'ActionCard',
  props: {
    title: String,
    description: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .action-card {
    min-height: 100px;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;

    & .title {
      font-size: 1em;
    }
  }
</style>
