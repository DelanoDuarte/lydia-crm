import PurchaseOpportunityIndex from "./PurchaseOpportunityIndex.vue";
import PurchaseOpportunityDetails from "./PurchaseOpportunityDetails.vue";

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
];
