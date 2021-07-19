<template>
  <div class="row">
    <purchase-opportunity-filters :purchase_opportunity_status="all_status" />

    <div class="col-md-10">
      <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Today" subTitle="1581"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Last Month" subTitle="2358"> </card-status>
        </div>
      </div>

      <simple-card title="Opportunity">
        <template #content>
          <purchase-opportunity-table
            :purchase_opportunities="purchase_opps"
            v-on:on-row-click="rowSelected($event)"
          />
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import PurchaseOpportunityFilters from "../../components/purchase-opportunity/PurchaseOpportunityFilters.vue";
import PurchaseOpportunityTable from "../../components/purchase-opportunity/PurchaseOpportunityTable.vue";
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PurchaseOpportunityService } from "../../services/api";
export default {
  components: {
    SimpleCard,
    PurchaseOpportunityTable,
    CardStatus,
    PurchaseOpportunityFilters,
  },
  data() {
    return {
      purchase_opps: [],
      all_status: [],
    };
  },
  mounted() {
    this.load();
  },

  methods: {
    load() {
      PurchaseOpportunityService.getAll().then(
        (po) => (this.purchase_opps = po.data)
      );
      PurchaseOpportunityService.getAllStatus().then(
        (pos) => (this.all_status = pos.data)
      );
    },

    rowSelected(po_id) {
      console.log("Selected Row ", po_id);
      this.$router.push({
        name: "purchase-opportunity-details",
        params: { id: po_id },
      });
    },
  },
};
</script>

<style>
</style>