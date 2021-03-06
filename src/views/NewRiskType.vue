<template>
  <div class="new-risk-type">
    <h2 class="title">
      New Risk Type
    </h2>
    <form class="actions">
    </form>
  </div>
</template>

<script>
export default {
  name: "NewRiskType",
  components: {  },
  data: function() {
    return {
        form: {
          name: ""
        }
      };
    },
  methods: { }
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
