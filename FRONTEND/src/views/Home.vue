<template>
  <div>
    <app-header></app-header>
    <h1 class="display-1">Flash Card App</h1>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
export default {
  // eslint-disable-next-line
  name: "Home",
  components: {
    appHeader: Header,
  },
};
</script>
<style>
h1 {
  text-align: center;
  margin: 40px auto;
  font-size: 4rem;

  font-family: "Courgette", cursive;
}
</style>
