<template>
  <form @submit="submitPartner($event)">
    <div class="form-row gap-3">
      <div class="col-md-6 p-1">
        <input
          type="text"
          class="form-control"
          placeholder="First name"
          v-model="partner.firstName"
        />
      </div>
      <div class="col-md-6 p-1">
        <input
          type="text"
          class="form-control"
          placeholder="Last name"
          v-model="partner.lastName"
        />
      </div>
      <div class="col-md-6 p-1">
        <input
          type="date"
          class="form-control"
          placeholder="Birthdate"
          v-model="partner.birthDate"
        />
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Search</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      partner: {
        firstName: undefined,
        lastName: undefined,
        birthDate: undefined,
      },
    };
  },
  methods: {
    submitPartner(event) {
      event.preventDefault();
      this.$emit("partner_search", this.partner);
    },
  },
};
</script>

<style>
</style>