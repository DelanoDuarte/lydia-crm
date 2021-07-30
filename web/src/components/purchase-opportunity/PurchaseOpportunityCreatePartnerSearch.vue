<template>
  <div>
    <div class="row">
      <form @submit="submitPartner($event)">
        <div class="form-row gap-3">
          <div class="col-md-6 p-2">
            <input
              type="text"
              class="form-control"
              placeholder="First name"
              v-model="partner.firstName"
            />
          </div>
          <div class="col-md-6 p-2">
            <input
              type="text"
              class="form-control"
              placeholder="Last name"
              v-model="partner.lastName"
            />
          </div>
          <div class="col-md-6 p-2">
            <input
              type="date"
              class="form-control"
              placeholder="Birthdate"
              v-model="partner.birthDate"
            />
          </div>
        </div>
        <div class="p-2 float-right">
          <button type="submit" class="btn btn-primary">Search</button>
          <!-- <button type="reset" class="btn btn-warning">Clear</button> -->
        </div>
      </form>
    </div>

    <div class="row">
      <partner-table
        :partners="partners"
        v-on:selected_partner="$emit('select_partner', $event)"
      />
    </div>
  </div>
</template>

<script>
import { PartnerService } from "../../services/api";
import PartnerTable from "../partner/PartnerTable.vue";
export default {
  components: { PartnerTable },
  data() {
    return {
      partner: {
        firstName: "",
        lastName: "",
        birthDate: "",
      },
      partners: [],
    };
  },
  methods: {
    submitPartner(event) {
      event.preventDefault();
      const { firstName, lastName, birthDate } = this.partner;
      const filters = `${firstName} ${lastName} ${birthDate}`;
      PartnerService.find(filters).then((response) => {
        this.partners = response.data;
      });
    },
  },
};
</script>

<style>
</style>