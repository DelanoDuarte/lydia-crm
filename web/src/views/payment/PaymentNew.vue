<template>
  <div>
    <div class="row pb-2">
      <div class="col">
        <h4>New Payment</h4>
      </div>
      <div class="col">
        <button class="btn btn-success float-right">Create Payment</button>
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
            <payment-form />
          </template>
        </simple-card>
      </div>
    </div>
  </div>
</template>

<script>
import PaymentForm from "../../components/payment/PaymentForm.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard, PaymentForm },
};
</script>

<style>
</style>