<template>
  <div class="card-list">
    <home-card title="Overview">
      <action-card 
        class="action__primary"
        title="Total Risks"
        description="766"
      />
      <action-card 
        class="action__primary"
        title="Total Risk Types"
        description="1.082"
      />
      <action-card 
        class="action__primary"
        title="Total Fields"
        description="7.223"
      />
    </home-card>
    <home-card title="Actions">
      <div @click="navigate('create/risktype')">
        <action-card 
          class="action"
          title="Create a Risk Type"
          description="Adds a risk type record"
        />
      </div>
      <div @click="navigate('create/risk')">
        <action-card 
          class="action"
          title="Create a Risk"
          description="Adds a new Risk record"
        />
      </div>
      <div @click="navigate('manage/risks')">
        <action-card 
          class="action"
          title="Manage a Risk"
          description="Visualize or edit details for an existent Risk"
        />
      </div>
    </home-card>
  </div>
</template>

<script>
import HomeCard from "./HomeCard.vue";
import ActionCard from "./ActionCard.vue";
import router from "../router";

export default {
  name: "HomeDetail",
  components: { ActionCard, HomeCard },
  methods: {
    navigate(url) {
      let [ path, param ] = url.split("/");
      const route = param? { path: `/${path}/${param}` } : path;
      router.push(route);
    },
  }
};
</script>

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
