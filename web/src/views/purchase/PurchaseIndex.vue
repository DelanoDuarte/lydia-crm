<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card>
        <template v-slot:header>
          <h4>Filters</h4>
        </template>
      </simple-card>
    </div>

    <div class="col-md-10">
      <simple-card title="Purchase"> </simple-card>
    </div>
  </div>
</template>

<script>
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
};
</script>

<style>
</style>