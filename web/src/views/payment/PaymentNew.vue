<template>
  <div>
    <div class="row pb-2">
      <div class="col">
        <h4>New Payment</h4>
      </div>
      <div class="col">
        <button class="btn btn-success float-right" @click.prevent="create()">
          Create Payment
        </button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-2">
        <simple-card title="Actions">
          <template #content> </template>
        </simple-card>
      </div>
      <div class="col-md-10">
        <simple-card title="New Payment">
          <template #content>
            <payment-form ref="paymentForm" />
          </template>
        </simple-card>
      </div>
    </div>
  </div>
</template>

<script>
import PaymentForm from "../../components/payment/PaymentForm.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PaymentService } from "../../services/api";
export default {
  components: { SimpleCard, PaymentForm },
  methods: {
    create() {
      const paymentData = this.$refs.paymentForm.payment;

      paymentData.partner = paymentData.partner.id;
      paymentData.purchase = paymentData.purchase.id;
      paymentData.mode = paymentData.mode.id;

      PaymentService.create(paymentData)
        .then(() => {
          this.$router.push({ name: "payment-list" });
        })
        .then(() => {
          this.$bvToast.toast("New Payment Created", {
            title: `Payment`,
            variant: "success",
            solid: true,
          });
        })
        .catch((error) => {
          console.log(error);
          this.$bvToast.toast(
            "Something Bad Happened on Payment Creation. Try again later.",
            {
              title: `Payment`,
              variant: "danger",
              solid: true,
            }
          );
        });
    },

    /**
     * Validate if a payment exist for an purchase with same amount given.
     */
    checkIfAlreadyExistsAnPaymentForGivenPurchaseAndSameAmount() {},
  },
};
</script>

<style>
</style>