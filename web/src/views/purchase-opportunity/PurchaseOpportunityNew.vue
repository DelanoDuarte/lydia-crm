<template>
  <div>
    <div class="row pb-3">
      <div class="col-md-6">
        <h4>New Purchase</h4>
      </div>

      <div class="col-md-6">
        <button @click="create()" class="btn btn-success btn-md float-end">
          Create Purchase
        </button>
      </div>
    </div>
    <purchase-opportunity-create-form />
  </div>
</template>

<script>
import PurchaseOpportunityCreateForm from "../../components/purchase-opportunity/PurchaseOpportunityCreateForm.vue";
export default {
  components: { PurchaseOpportunityCreateForm },
  data() {
    return {};
  },
  mounted() {},
  methods: {
    create() {},
  },
};
</script>

<style>
</style>