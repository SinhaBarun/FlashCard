<template>
  <table class="table table-responsive">
    <thead>
      <tr>
        <th scope="col">Correct</th>
        <th scope="col">InCorrect</th>
        <th scope="col">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{ correct }}</td>
        <td>{{ incorrect }}</td>
        <td>{{ correct + incorrect }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "Score",

  created: function () {
    const username = this.$store.getters.currentUsername;
    axios
      .get(`/getscore/${username}`)
      .then((res) => {
        if (res.status == 200) {
          console.log(res);
          this.$store.state.correctAns = res.data.correct;
          this.$store.state.incorrectAns = res.data.incorrect;
        }
      })
      .catch((err) => console.log(err));
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
