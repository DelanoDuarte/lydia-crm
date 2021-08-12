<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card title="Filters">
        <template #header> </template>
      </simple-card>
    </div>

    <div class="col-md-10">
      <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Today" subTitle="1581"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Last Month" subTitle="2358"> </card-status>
        </div>
      </div>
      <simple-card title="Purchase">
        <template #content>
          <b-table striped hover :items="purchases" :fields="fieldsTable">
            <template #cell(status)="data">
              <span class="badge bg-success text-white">{{ data.value }}</span>
            </template>
            <template v-slot:[`cell(partner.full_name)`]="data">
              <b>{{ data.value }} </b>
            </template>
          </b-table>
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PurchaseService } from "../../services/api";
export default {
  components: { SimpleCard, CardStatus },
  data() {
    return {
      fieldsTable: [
        { key: "status" },
        { key: "partner.full_name", label: "Partner" },
        { key: "purchaseDate", label: "Date" },
        { key: "opportunity.priority", label: "Priority" },
      ],
      purchases: [],
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      PurchaseService.all()
        .then((response) => (this.purchases = response.data))
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>