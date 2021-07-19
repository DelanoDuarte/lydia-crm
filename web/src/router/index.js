import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import { partner_routes } from "../views/partner/routes";
import { purchase_opportunity_routes } from "../views/purchase-opportunity/routes";

import PurchaseIndex from "@/views/purchase/PurchaseIndex.vue";
import ProductCatalog from "@/views/product-catalog/ProductCatalog.vue";

const product_routes = [
  {
    path: "/product-catalog",
    name: "product-catalog",
    component: ProductCatalog,
  },
];

const purchase_routes = [
  {
    path: "/purchase",
    name: "purchase-index",
    component: PurchaseIndex,
  },
];

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  ...partner_routes,
  ...purchase_routes,
  ...purchase_opportunity_routes,
  ...product_routes,
  ...purchase_opportunity_routes,
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;