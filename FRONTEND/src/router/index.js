import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home";
import Dashboard from "@/views/Dashboard";
import store from "@/store/index.js";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard,
    beforeEnter(from, to, next) {
      if (store.state.isAuthenticated) {
        next();
      } else {
        prompt("Please Login first");
        next("/");
      }
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
