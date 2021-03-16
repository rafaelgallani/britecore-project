<template>
  <div class="card-list">
    <home-card title="Overview">
      <action-card 
        class="action__primary"
        title="Total of Risks"
        :description="count.risks"
      />
      <action-card 
        class="action__primary"
        title="Total of Risk Types"
        :description="count.riskTypes"
      />
      <action-card 
        class="action__primary"
        title="Total of Fields"
        :description="count.fields"
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
      <div @click="navigate('manage/risktype')">
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
import axios from "axios";

export default {
  name: "HomeDetail",
  components: { ActionCard, HomeCard },
  data: function () {
    return {
      count: {
        risks: "-",
        riskTypes: "-",
        fields: "-",
      },
      loading: true,
      loader: null,
      riskType: {},
      risks: [],
    };
  },
  
  async mounted(){
    this.toggleLoading(true);
    await Promise.all([
      await axios.get("/api/v1/risk/?fields=id").then(
        result => this.count.risks = result.data.length
      ),
      await axios.get("/api/v1/risk-type/?fields=id").then(
        result => this.count.riskTypes = result.data.length
      ),
      await axios.get("/api/v1/field/?fields=id").then(
        result => this.count.fields = result.data.length
      ),
    ]);
    this.toggleLoading(false);
  },
  methods: {
    navigate(url) {
      let [ path, param ] = url.split("/");
      const route = param? { path: `/${path}/${param}` } : path;
      router.push(route);
    },

    toggleLoading(toggle){
      this.loading = toggle;
      if (toggle) this.loader = this.$loading.show();
      if (!toggle) if (this.loader) this.loader.hide();
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
