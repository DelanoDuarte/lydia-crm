<template>
  <table class="table table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Gender</th>
        <th scope="col">Email</th>
        <th scope="col">BirthDate</th>
        <th scope="col">Partner Type</th>
        <th scope="col"></th>
      </tr>
    </thead>
    <tbody>
      <tr
        class="table-row"
        v-for="partner in partners"
        v-bind:key="partner.id"
        @dblclick="$emit('selected_partner', partner)"
      >
        <td>{{ partner.full_name }}</td>
        <td>
          <span class="badge rounded-pill bg-info text-white">
            {{ partner.gender }}
          </span>
        </td>
        <td>{{ partner.email }}</td>
        <td v-if="partner.birthDate">{{ partner.birthDate }}</td>
        <td v-else>*Not Provided</td>
        <td>
          <span class="badge rounded-pill bg-success text-white">
            {{ partner.partnerType.name }}
          </span>
        </td>
        <td>
          <font-awesome-icon icon="ellipsis-v" size="sm" />
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    partners: [],
  },
};
</script>

<style scoped>
.table-row {
  cursor: pointer;
}
</style>