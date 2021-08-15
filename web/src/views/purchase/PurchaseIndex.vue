<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card title="Filters">
        <template #header>
          <purchase-filters />
        </template>
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

            <template v-slot:[`cell(opportunity.priority)`]="data">
              <span :class="`${priorityColor(data.value)}`">
                Level {{ data.value }}</span
              >
            </template>
          </b-table>
        </template>

        <template #footer>
          <b-pagination
            class="float-right"
            v-model="pagination.currentPage"
            :total-rows="pagination.totalRows"
            :per-page="pagination.perPage"
            aria-controls="my-table"
            v-on:change="onPageChange($event)"
          ></b-pagination>
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import PurchaseFilters from "../../components/purchase/PurchaseFilters.vue";
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PurchaseService } from "../../services/api";
import { purchasePriorityLevel } from "../../utils/PurchaseStatusUtils";

export default {
  components: { SimpleCard, CardStatus, PurchaseFilters },
  data() {
    return {
      fieldsTable: [
        { key: "status" },
        { key: "partner.full_name", label: "Partner" },
        { key: "purchaseDate", label: "Date" },
        { key: "opportunity.priority", label: "Priority" },
      ],
      pagination: {
        currentPage: 1,
        totalRows: 0,
        perPage: 25,
      },
      purchases: [],
    };
  },
  mounted() {
    this.load(1);
  },
  methods: {
    load(page) {
      PurchaseService.allByPage(page)
        .then((response) => {
          this.purchases = response.data.results;
          this.pagination.totalRows = response.data.count;
          this.pagination.currentPage = page;
        })
        .catch((error) => console.log(error));
    },
    priorityColor(priority) {
      return "badge text-white bg-" + purchasePriorityLevel(priority);
    },

    onPageChange(page) {
      this.load(page);
    },
  },
};
</script>

<style>
</style>