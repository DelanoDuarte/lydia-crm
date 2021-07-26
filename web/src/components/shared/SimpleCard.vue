<template>
  <div class="p-3 mb-3 bg-body rounded shadow">
    <h5 class="border-bottom p-2 mb-0">{{ title }}</h5>

    <slot name="header"></slot>
    <div class="card-content">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
  },
};
</script>

<style scoped>
.card-content {
  padding: 5px;
}
</style>