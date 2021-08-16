import VueRouter from "vue-router";
import Home from "../views/Home.vue";

import { partner_routes } from "../views/partner/routes";
import { purchase_opportunity_routes } from "../views/purchase-opportunity/routes";
import { product_categories_routes } from "../views/product-category/routes";
import { payment_routes } from "../views/payment/routes";

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
  ...product_categories_routes,
  ...payment_routes,
];

const router = new VueRouter({
  routes, // short for `routes: routes`
});

export default router;
