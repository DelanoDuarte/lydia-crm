<template>
  <form>
    <div class="row">
      <div class="col-md-8">
        <simple-card title="Basic Info"> </simple-card>
      </div>
      <div class="col-md-4">
        <simple-card title="Partner">
          <template #content>
            <div class="text-center pt-3">
              <button class="btn btn-success btn-md">Search</button>
            </div>
          </template>
        </simple-card>
      </div>
      <div class="col-md-8">
        <simple-card title="Products">
          <template #content>
            <div class="float-end pt-1">
              <button class="btn btn-success btn-sm">Add</button>
            </div>
            <purchase-opportunity-product-table />
          </template>
        </simple-card>
      </div>
    </div>

    <div class="row"></div>
  </form>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
import PurchaseOpportunityProductTable from "./PurchaseOpportunityProductTable.vue";
export default {
  components: { SimpleCard, PurchaseOpportunityProductTable },
};
</script>

<style>
</style>