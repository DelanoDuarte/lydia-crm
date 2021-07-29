<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card>
        <template #header>
          <h4>Actions</h4>
        </template>
        <template #content>
          <div class="row d-grid gap-2 p-2">
            <button class="btn btn-success btn-sm btn-block" type="button">
              Convert
            </button>
            <button
              class="btn btn-outline-danger btn-sm btn-block"
              type="button"
            >
              Delete
            </button>
            <button
              class="btn btn-outline-warning btn-sm btn-block"
              type="button"
              @click="$router.push({ name: 'purchase-opportunity-index' })"
            >
              Go Back
            </button>
          </div>
        </template>
      </simple-card>
    </div>
    <div class="col-md-10">
      <simple-card title="Opportunity">
        <template #content>
          <div>
            <div class="row">
              <div class="m-2 col-md-12 mx-0">
                <stepper
                  :steps="all_status"
                  :active_step="purchase_opportunity.status"
                />
              </div>
            </div>
          </div>
        </template>
      </simple-card>

      <div class="row">
        <div class="col-md-7">
          <purchase-opportunity-partner-card
            :partner="purchase_opportunity.partner"
          />
        </div>

        <div class="col-md-5">
          <simple-card title="Products">
            <template #content>
              <purchase-opportunity-product-table
                :products="purchase_opportunity.products"
              />
            </template>
          </simple-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PurchaseOpportunityPartnerCard from "../../components/purchase-opportunity/PurchaseOpportunityPartnerCard.vue";
import PurchaseOpportunityProductTable from "../../components/purchase-opportunity/PurchaseOpportunityProductTable.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import Stepper from "../../components/shared/Stepper.vue";
import { PurchaseOpportunityService } from "../../services/api";
export default {
  components: {
    SimpleCard,
    PurchaseOpportunityProductTable,
    PurchaseOpportunityPartnerCard,
    Stepper,
  },
  data() {
    return {
      purchase_opportunity: {
        type: Object,
      },
      all_status: [],
    };
  },
  mounted() {
    const purchase_opp_id = this.$route.params.id;
    this.load(purchase_opp_id);
  },
  methods: {
    load(id) {
      PurchaseOpportunityService.byId(id).then(
        (po) => (this.purchase_opportunity = po.data)
      );

      PurchaseOpportunityService.getAllStatus().then(
        (status) => (this.all_status = status.data)
      );
    },
  },
};
</script>

<style>
</style>