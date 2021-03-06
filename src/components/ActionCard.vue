<template>
  <div class="action-card">
    <b class="title">{{ title }}</b>
    <span class="description">{{ description }}</span>
  </div>
</template>

<script>
export default {
  name: "ActionCard",
  props: {
    title: {
      type: String,
      default: ""
    },
    description: {
      type: String,
      default: ""
    },
  }
};
</script>


<style lang="scss" scoped>
  .action-card {
    cursor: pointer;
    min-height: 100px;
    display: flex;
    flex: 1;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 0 10px;
    margin: 5px 10px;
    border-radius: 5px;
    align-content: center;
    justify-content: center;

    box-shadow: 0px 0px 8px 1px rgba(217,217,217,1);

    & .title {
      font-size: 1.4em;
      font-weight: bold;
      margin-bottom: 5px;
      text-align: center;
      flex-basis: 100%;
    }

  }
</style>
