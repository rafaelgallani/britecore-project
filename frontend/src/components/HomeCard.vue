<template>
  <div class="home-card">
    <h2 class="title">
      {{ title }}
    </h2>
    <main class="actions">
      <slot />
    </main>
  </div>
</template>

<script>
export default {
  name: "HomeCard",
  props: {
    title: {
      type: String,
      default: ""
    }
  }
};
</script>


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
