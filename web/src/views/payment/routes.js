import PaymentList from "@/views/payment/PaymentList.vue";
import PaymentNew from "@/views/payment/PaymentNew.vue";

export const payment_routes = [
  {
    path: "/payment",
    name: "payment-list",
    component: PaymentList,
  },
  {
    path: "/payment/new",
    name: "payment-new",
    component: PaymentNew,
  },
];
