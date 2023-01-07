<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <li v-for="(word, index) in reviewedWords" :key="index">
      <div
        v-if="queSide"
        class="card text-white bg-secondary mb-3"
        style="max-width: 18rem"
        @click="queSide = !queSide"
      >
        <div class="card-header" style="text-align: center">
          {{ index + 1 }}
        </div>
        <div class="card-body">
          <h2 class="card-title" style="text-align: center">{{ word[0] }}</h2>
        </div>
      </div>
      <div
        v-else
        class="card text-white bg-secondary mb-3"
        style="max-width: 18rem"
        @click="queSide = !queSide"
      >
        <div class="card-header" style="text-align: center">
          {{ index + 1 }}
        </div>
        <div class="card-body">
          <h2 class="card-title" style="text-align: center">{{ word[1] }}</h2>
        </div>
      </div>
    </li>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "dashboard",
  data() {
    return {
      queSide: true,
    };
  },
  methods: {
    getReviewedWords() {
      let token = this.$store.getters.access_token;
      const config = {
        headers: {
          Authorization: "Bearer " + token,
        },
      };
      const username = this.$store.getters.currentUsername;
      axios
        .get(`/getReviewedWords/${username}`, config)
        .then((res) => {
          if (res.status == 200) {
            this.$store.state.reviewedWords = res.data.reviewedWords;
            console.log(this.reviewedWords);
          }
        })
        .catch((err) => console.log(err));
    },
  },
  created: function () {
    this.getReviewedWords();
  },
  computed: {
    reviewedWords() {
      return this.$store.getters.reviewedWords;
    },
  },
};
</script>

<style scoped>
li {
  list-style-type: none;
}

.flip-enter-active {
  animation: flip-in 0.5s ease-out forwards;
}
.flip-leave-active {
  animation: flip-out 0.5s ease-out forwards;
}

@keyframes flip-out {
  from {
    transform: rotateY(0deg);
  }
  to {
    transform: rotateY(90deg);
  }
}
@keyframes flip-in {
  from {
    transform: rotateY(90deg);
  }
  to {
    transform: rotateY(0deg);
  }
}
</style>
