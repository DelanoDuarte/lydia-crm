<template>
  <div>
    <div class="row pb-2">
      <div class="col">
        <h4>New Purchase</h4>
      </div>
      <div class="col">
        <button class="btn btn-success float-right" @click.prevent="create()">
          Create Purchase
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
        <simple-card title="New Purchase">
          <template #content>
            <purchase-form />
          </template>
        </simple-card>
      </div>
    </div>
  </div>
</template>

<script>
import PurchaseForm from "../../components/purchase/PurchaseForm.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard, PurchaseForm },
  methods: {
    create() {},
  },
};
</script>

<style>
</style>