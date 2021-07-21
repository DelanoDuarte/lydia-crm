<template>
  <div class="p-3 mb-3 bg-body rounded shadow">
    <slot name="header" class="card-header"></slot>
    <h5 class="border-bottom p-2 mb-0">{{ title }}</h5>
    <slot name="content" class="card-content"></slot>
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
  margin-bottom: 20px;
}
</style>