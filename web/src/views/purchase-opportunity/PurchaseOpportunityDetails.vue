<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card>
        <template #header>
          <h4>Actions</h4>
        </template>
        <template #content>
          <div class="row d-grid gap-2 p-2">
            <button class="btn btn-success btn-sm" type="button">
              Convert
            </button>
            <button class="btn btn-outline-danger btn-sm" type="button">
              Delete
            </button>
            <button
              class="btn btn-outline-warning btn-sm"
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
        <template #content> </template>
      </simple-card>

      <div class="row">
        <div class="col-md-7">
          <simple-card title="Partner">
            <template #content>
              <div v-if="purchase_opportunity.partner">
                <div class="row">
                  <div class="m-2 col-md-5">
                    <label for="p-name" class="form-label">Name</label>
                    <input
                      type="text"
                      class="form-control"
                      id="p-name"
                      disabled
                      v-bind:value="purchase_opportunity.partner.full_name"
                    />
                  </div>

                  <div class="m-2 col-md-5">
                    <label for="p-email" class="form-label">Email</label>
                    <input
                      type="text"
                      class="form-control"
                      id="p-email"
                      disabled
                      v-bind:value="purchase_opportunity.partner.email"
                    />
                  </div>
                </div>

                <div class="row">
                  <div class="m-2 col-md-5">
                    <label for="p-birthdate" class="form-label"
                      >BirthDate</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      id="p-birthdate"
                      disabled
                      v-bind:value="purchase_opportunity.partner.birthDate"
                    />
                  </div>
                </div>
              </div>
            </template>
          </simple-card>
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
import PurchaseOpportunityProductTable from "../../components/purchase-opportunity/PurchaseOpportunityProductTable.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PurchaseOpportunityService } from "../../services/api";
export default {
  components: { SimpleCard, PurchaseOpportunityProductTable },
  data() {
    return {
      purchase_opportunity: {
        type: Object,
      },
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
    },
  },
};
</script>

<style>
</style>