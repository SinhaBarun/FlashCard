<template>
  <div>
    <div class="card text-white bg-secondary mb-3" style="max-width: 18rem">
      <div class="card-header">Card {{ correct + incorrect }}</div>
      <div class="card-body">
        <h5 class="card-title">{{ ans }}</h5>
      </div>
    </div>
    <button class="btn btn-primary" @click="showQuestion">Show Question</button>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: "Answer",
  data() {
    return {
      ans: this.$store.state.ans,
    };
  },
  methods: {
    showQuestion() {
      this.$emit("toggleQuestionAnswer");
    },
  },
  computed: {
    correct() {
      return this.$store.getters.correctAns;
    },
    incorrect() {
      return this.$store.getters.incorrectAns;
    },
  },
};
</script>

<style scoped></style>
