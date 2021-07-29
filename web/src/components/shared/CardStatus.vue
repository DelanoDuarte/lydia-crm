<template>
  <div class="card-stats card">
    <div class="card-body">
      <div class="row">
        <div class="col-5 col-md-4">
          <div class="icon-big text-center icon-warning">
            <font-awesome-icon icon="user-circle" />
          </div>
        </div>
        <div class="col-7 col-md-8">
          <div class="numbers">
            <p class="card-category">{{ title }}</p>
            <p class="card-title">{{ subTitle }}</p>
            <p></p>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="card-footer">
      <hr />
      <div class="stats">
        <i class="fas fa-sync-alt"></i>
        <slot name="footer"></slot>
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    subTitle: String,
  },
};
</script>

<style scoped>
.card {
  border-radius: 6px;
  box-shadow: 0 2px 2px rgb(204 197 185 / 50%);
  background-color: #fff;
  color: #252422;
  margin-bottom: 20px;
  position: relative;
  z-index: 1;
  border: none;
}
.card .numbers {
  font-size: 2em;
  text-align: right;
}

.card .icon-big {
  font-size: 3em;
  min-height: 64px;
}

.card .stats i {
  margin-right: 2px;
  min-width: 15px;
}

.card .stats {
  color: #a9a9a9;
  font-weight: 300;
}
.card-stats .card-body .numbers .card-category {
  color: #9a9a9a;
  font-size: 16px;
  line-height: 1.4em;
}
.row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

.card-stats .card-body {
  padding: 15px 15px 0;
}

.card-body {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 1.25rem;
}
</style>