import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import NewRisk from "../views/NewRisk.vue";
import NewRiskType from "../views/NewRiskType.vue";
import ManageRisk from "../views/ManageRisk.vue";
import ManageRiskType from "../views/ManageRiskType.vue";

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
    path: "/manage/risk",
    name: "Manage Risk",
    component: ManageRisk
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
