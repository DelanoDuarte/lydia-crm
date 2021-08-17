<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card title="Filters">
        <template #content>
          <payment-filter />
        </template>
      </simple-card>
    </div>
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
        <template #content>
          <b-table striped hover :items="payments" :fields="fieldsTable">
            <template v-slot:[`cell(paymentNumber)`]="data">
              <span class="badge bg-success text-white"> {{ data.value }}</span>
            </template>
            <template v-slot:[`cell(amount)`]="data">
              <b> € {{ data.value }} </b>
            </template>
            <template v-slot:[`cell(mode.name)`]="data">
              <span class="badge rounded-pill bg-primary text-white">
                {{ data.value }}</span
              >
            </template>
          </b-table>
        </template>

        <template #footer>
          <div class="row">
            <div class="col-md-12">
              <div class="float-left">
                <div class="row g-3 p-2">
                  <label for="itemsPerPage">Items per Page</label>
                  <select
                    id="itemsPerPage"
                    class="form-control"
                    v-model="pagination.limit"
                    @change="load(pagination.limit, pagination.currentPage - 1)"
                  >
                    <option @value="1">1</option>
                    <option @value="5">5</option>
                    <option @value="15">15</option>
                    <option @value="25">25</option>
                  </select>
                </div>
              </div>
              <div class="float-right">
                <b-pagination
                  class="float-right"
                  v-model="pagination.currentPage"
                  :total-rows="pagination.totalRows"
                  :per-page="pagination.limit"
                  aria-controls="my-table"
                  v-on:change="load(pagination.limit, $event - 1)"
                ></b-pagination>
              </div>
            </div>
          </div>
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import PaymentFilter from "../../components/payment/PaymentFilter.vue";
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { PaymentService } from "../../services/api";
export default {
  components: { SimpleCard, CardStatus, PaymentFilter },
  data() {
    return {
      payments: [],
      fieldsTable: [
        { key: "paymentNumber", label: "Number" },
        { key: "paymentDate", label: "Date" },
        { key: "partner.full_name", label: "Partner" },
        { key: "amount", label: "Amount" },
        { key: "mode.name", label: "Payment Mode" },
      ],
      pagination: {
        currentPage: 1,
        totalRows: 0,
        limit: 25,
      },
    };
  },

  mounted() {
    this.load(this.pagination.limit, this.pagination.currentPage - 1);
  },

  methods: {
    load(limit, offset) {
      PaymentService.all(limit, offset)
        .then((response) => {
          this.payments = response.data.results;
          this.pagination.totalRows = response.data.count;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>