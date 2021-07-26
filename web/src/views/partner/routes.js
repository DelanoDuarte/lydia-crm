import PartnerList from "@/views/partner/PartnerList.vue";
import PartnerNew from "@/views/partner/PartnerNew.vue";

export const partner_routes = [
  {
    path: "/partner",
    name: "partner-list",
    component: PartnerList,
  },
  {
    path: "/partner/create",
    name: "partner-create",
    component: PartnerNew,
  },
];
