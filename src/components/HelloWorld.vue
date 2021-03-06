<template>
  <h2 class="title">Welcome!</h2>
  <main class="actions">
    <action-card 
      title="Create a new risk type"
      description="Adds a risk type record to the database."
    />
    <action-card 
      title="Create a risk"
      description="Adds a new risk record to the database."
    />
    <action-card 
      title="Manage a risk"
      description="Visualize or edit details for an existent risk."
    />
  </main>
</template>

<script>
import ActionCard from './ActionCard.vue'
export default {
  components: { ActionCard },
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .title {
    font-size: 40px;
    margin-bottom: 10px;
  }
</style>
