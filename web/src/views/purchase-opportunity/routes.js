import PurchaseOpportunityIndex from "./PurchaseOpportunityIndex.vue";
import PurchaseOpportunityDetails from "./PurchaseOpportunityDetails.vue";
import PurchaseOpportunityNew from "./PurchaseOpportunityNew.vue";

export const purchase_opportunity_routes = [
  {
    path: "/purchase-opportunity",
    name: "purchase-opportunity-index",
    component: PurchaseOpportunityIndex,
  },

  {
    path: "/purchase-opportunity/:id",
    name: "purchase-opportunity-details",
    component: PurchaseOpportunityDetails,
  },

  {
    path: "/purchase-opportunity/create",
    name: "purchase-opportunity-create",
    component: PurchaseOpportunityNew,
  },
];
