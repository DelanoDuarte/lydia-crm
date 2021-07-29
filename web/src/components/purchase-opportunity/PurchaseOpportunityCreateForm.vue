<template>
  <div class="row">
    <div class="col-md-8">
      <simple-card title="Basic Info">
        <template #content>
          <div class="row g-3 p-2">
            <div class="col-4">
              <label for="inputExcpetedEndDate" class="form-label"
                >Expected End Date</label
              >
              <input
                required
                type="date"
                class="form-control form-control-sm"
                id="inputExcpetedEndDate"
              />
            </div>
            <div class="col-4">
              <label for="inputPriority" class="form-label">Priority</label>
              <input
                required
                type="number"
                max="3"
                min="1"
                class="form-control form-control-sm"
                id="inputPriority"
              />
            </div>
          </div>
          <div class="row g-3 p-2">
            <div class="col-8">
              <label for="inputComments" class="form-label">Comments</label>
              <textarea
                class="form-control form-control-sm"
                id="inputComments"
              />
            </div>
          </div>
        </template>
      </simple-card>
    </div>
    <div class="col-md-4">
      <simple-card title="Partner">
        <template #content>
          <div class="text-center pt-3">
            <button
              class="btn btn-success btn-md"
              @click="showPartnerModal = !showPartnerModal"
            >
              Select / Search
            </button>
          </div>
        </template>
      </simple-card>
      <b-modal
        v-model="showPartnerModal"
        title="Select Partner"
        hide-footer
        size="lg"
      >
        <div>
          <purchase-opportunity-create-partner-search
            v-on:partner_search="onSearchPartner($event)"
          />
        </div>
      </b-modal>
    </div>
    <div class="col-md-8">
      <simple-card title="Products">
        <template #content>
          <div class="float-right pt-1 pb-1">
            <button class="btn btn-success btn-sm">
              <font-awesome-icon icon="plus" /> Add
            </button>
          </div>
          <purchase-opportunity-product-table :products="[]" />
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
import PurchaseOpportunityCreatePartnerSearch from "./PurchaseOpportunityCreatePartnerSearch.vue";
import PurchaseOpportunityProductTable from "./PurchaseOpportunityProductTable.vue";
export default {
  components: {
    SimpleCard,
    PurchaseOpportunityProductTable,
    PurchaseOpportunityCreatePartnerSearch,
  },
  data() {
    return {
      showPartnerModal: false,
    };
  },
  methods: {
    onSearchPartner(partner) {
      console.log(partner);
    },
  },
};
</script>

<style>
</style>