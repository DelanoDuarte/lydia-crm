<template>
  <div>
    <div class="row pb-3">
      <div class="col-md-6">
        <h4>New Purchase</h4>
      </div>

      <div class="col-md-6">
        <button
          @click.prevent="create()"
          class="btn btn-success btn-md float-right"
        >
          Create Purchase
        </button>
      </div>
    </div>
    <purchase-opportunity-create-form ref="purchaseOpportunityForm" />
  </div>
</template>

<script>
import PurchaseOpportunityCreateForm from "../../components/purchase-opportunity/PurchaseOpportunityCreateForm.vue";
import { PurchaseOpportunityService } from "../../services/api";
export default {
  components: { PurchaseOpportunityCreateForm },
  data() {
    return {};
  },
  mounted() {},
  methods: {
    create() {
      const purchase_opportunity =
        this.$refs.purchaseOpportunityForm.purchase_opportunity;
      purchase_opportunity.products = this.$store.state.product.products.map(
        (p) => p.id
      );
      purchase_opportunity.partner = purchase_opportunity.partner.id;

      PurchaseOpportunityService.create(purchase_opportunity)
        .then(() => {
          this.$bvToast.toast("Purchase Opportunity successfuly created.", {
            title: `Purchase Opportunity`,
            variant: "success",
            solid: true,
          });
        })
        .then(() => {
          this.$router.push({ name: "purchase-opportunity-index" });
          this.$store.commit("product/clear");
        })
        .catch(() => {
          this.$bvToast.toast(
            "Something Bad Happnened on Purchase Opportunity creation.",
            {
              title: `Purchase Opportunity`,
              variant: "danger",
              solid: true,
            }
          );
        });
    },
  },
};
</script>

<style>
</style>