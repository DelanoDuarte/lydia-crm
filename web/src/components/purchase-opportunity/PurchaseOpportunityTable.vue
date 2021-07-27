<template>
  <table class="table table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Status</th>
        <th scope="col">Partner</th>
        <th scope="col">Priority</th>
        <th scope="col">Expected End Date</th>
        <th scope="col">Created At</th>
        <th scope="colr"></th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="po in purchase_opportunities"
        v-bind:key="po.id"
        @dblclick="$emit('on-row-click', po.id)"
        class="clickable-row"
      >
        <td>
          <span class="badge bg-success">{{ po.status }}</span>
        </td>
        <td>
          <b>
            {{ po.partner.full_name }}
          </b>
        </td>
        <td>{{ po.priority }}</td>
        <td>{{ po.expectedEndingDate }}</td>
        <td>{{ po.createdAt }}</td>
        <td>
          <font-awesome-icon icon="ellipsis-v" />
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    purchase_opportunities: {
      type: Array,
      default: [],
    },
  },
};
</script>

<style scoped>
.clickable-row {
  cursor: pointer;
}
</style>