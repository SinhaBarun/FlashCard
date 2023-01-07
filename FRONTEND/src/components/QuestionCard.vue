<template>
  <div class="container container-fluid">
    <div class="card border-success mb-3 card-columns" style="max-width: 18rem">
      <div class="card-header bg-transparent border-success">
        {{ question }}
      </div>
      <div class="card-body text-success">
        <div class="container container-card-body container-fluid">
          <div class="d-grid gap-2 d-md-block row justify-content-around">
            <div class="col-4">
              <button class="btn btn-primary" @click="checkAns(0)">
                {{ btns[0].options }}
              </button>
            </div>
            <div class="col-4">
              <button class="btn btn-primary" @click="checkAns(1)">
                {{ btns[1].options }}
              </button>
            </div>
          </div>
          <div class="row justify-content-around">
            <div class="col-4">
              <button class="btn btn-primary" @click="checkAns(2)">
                {{ btns[2].options }}
              </button>
            </div>
            <div class="col-4">
              <button class="btn btn-primary" @click="checkAns(3)">
                {{ btns[3].options }}
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="card-footer bg-transparent border-success">
        <button class="btn btn-primary" @click="showAnswer1">
          Show Answer
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "Question",
  data() {
    return {
      btns: [
        {
          options: "",
          ans: false,
        },
        {
          options: "",
          ans: false,
        },
        {
          options: "",
          ans: false,
        },
        {
          options: "",
          ans: false,
        },
      ],
      question: "",
    };
  },

  methods: {
    showAnswer1() {
      this.$emit("toggleQuestionAnswer");
    },

    getWord() {
      let token = this.$store.getters.access_token;
      const config = {
        headers: {
          Authorization: "Bearer " + token,
        },
      };
      const username = this.$store.getters.currentUsername;
      axios
        .get(`/getword/${username}`, config)
        .then((res) => {
          if (res.status == 200) {
            console.log(res);
            this.btns[0].options = res.data.options[0];
            this.btns[1].options = res.data.options[1];
            this.btns[2].options = res.data.options[2];
            this.btns[3].options = res.data.options[3];
            this.question = res.data.res_word;
            const n = Math.trunc(Math.random() * 4);
            this.btns[n].options = res.data.res_ans;
            this.btns[n].ans = true;
          }
        })
        .catch((err) => console.log(err));
    },

    checkAns(n) {
      const username = this.$store.getters.currentUsername;
      if (this.btns[n].ans) {
        console.log(this.btns[n].ans);
        axios
          .post(`/updatescore/${username}/${this.question}/1`)
          .then((res) => {
            console.log(res);
            this.$store.state.correctAns = res.data.correct;
            this.$store.state.incorrectAns = res.data.incorrect;
            this.getWord();
          });
      } else {
        axios
          .post(`/updatescore/${username}/${this.question}/0`)
          .then((res) => {
            console.log(res);
            this.$store.state.correctAns = res.data.correct;
            this.$store.state.incorrectAns = res.data.incorrect;
            this.getWord();
          });
      }
    },
  },

  created: function () {
    this.getWord();
  },
};
</script>
<style scoped>
.btn {
  margin: 0.5rem;
}
</style>
