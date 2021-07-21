<template>
  <simple-card title="Partner">
    <template #content>
      <div v-if="partner">
        <div class="row">
          <div class="m-2 col-md-5">
            <label for="p-name" class="form-label">Name</label>
            <input
              type="text"
              class="form-control"
              id="p-name"
              disabled
              v-bind:value="partner.full_name"
            />
          </div>

          <div class="m-2 col-md-5">
            <label for="p-email" class="form-label">Email</label>
            <input
              type="text"
              class="form-control"
              id="p-email"
              disabled
              v-bind:value="partner.email"
            />
          </div>
        </div>

        <div class="row">
          <div class="m-2 col-md-5">
            <label for="p-birthdate" class="form-label">BirthDate</label>
            <input
              type="text"
              class="form-control"
              id="p-birthdate"
              disabled
              v-bind:value="partner.birthDate"
            />
          </div>
        </div>
      </div>
    </template>
  </simple-card>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  props: {
    partner: Object,
  },
};
</script>

<style>
</style>