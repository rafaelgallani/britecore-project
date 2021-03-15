import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import NewRisk from "../views/NewRisk.vue";
import NewRiskType from "../views/NewRiskType.vue";
import ManageRisks from "../views/ManageRisks.vue";
import ManageRiskType from "../views/ManageRiskType.vue";
import About from  "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/create/risk",
    name: "New Risk",
    component: NewRisk
  },
  {
    path: "/create/risktype",
    name: "New Risk Type",
    component: NewRiskType
  },
  {
    path: "/manage/risktype",
    name: "Manage Risk Type",
    component: ManageRiskType
  },
  {
    path: "/manage/risktype/:riskTypeId",
    name: "Manage Risks",
    component: ManageRisks
  },
  {
    path: "/about",
    name: "About",
    component: About
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
