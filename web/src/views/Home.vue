<template>
  <div class="home">
    <div>
      <simple-card title="Home">
        <p>Welcome to Lydia</p>
      </simple-card>
    </div>
    <div>
      <RecentUpdates />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import RecentUpdates from "@/components/home/RecentUpdates.vue";
import SimpleCard from "@/components/shared/SimpleCard.vue";

export default {
  name: "Home",
  components: {
    RecentUpdates,
    SimpleCard,
  },
};
</script>
