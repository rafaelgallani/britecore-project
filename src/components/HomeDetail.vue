<template>
  <home-card title="Overview">
    <action-card 
      class="action__primary"
      title="Risks"
      description="766"
    />
    <action-card 
      class="action__primary"
      title="Risk Types"
      description="1.082"
    />
    <action-card 
      class="action__primary"
      title="Fields"
      description="7.223"
    />

  </home-card>
  <home-card title="Actions">
    <action-card 
      class="action"
      title="Create a Risk Type"
      description="Adds a risk type record"
    />
    <action-card 
      class="action"
      title="Create a Risk"
      description="Adds a new Risk record"
    />
    <action-card 
      class="action"
      title="Manage a Risk"
      description="Visualize or edit details for an existent Risk"
    />
  </home-card>
</template>

<script>
import HomeCard from './HomeCard.vue'
import ActionCard from './ActionCard.vue'
export default {
  components: { ActionCard, HomeCard },
  name: 'HomeDetail',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  
  .action{
    position: relative;
    bottom: 0px;

    &__primary {
      background: $primary-color;
      color: $text-on-primary;

      position: relative;
      bottom: 0px;
    }

    &:hover, &__primary:hover{
      bottom: 2px;
    }
  }  
</style>
