<template>
  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-10">
      <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Incoming" subTitle="1581"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Amount" subTitle="2358"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Something"> </card-status>
        </div>
      </div>

      <simple-card title="Payments">
        <template v-slot:content> </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard, CardStatus },
};
</script>

<style>
</style>