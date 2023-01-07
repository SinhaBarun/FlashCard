<template>
  <div class="container container-fluid">
    <app-header></app-header>
    <main>
      <div class="container container-fluid">
        <div class="row row-cols-2">
          <div class="col">
            <transition name="flip" mode="out-in">
              <component
                :is="mode"
                @toggleQuestionAnswer="
                  mode == 'app-answer'
                    ? (mode = 'app-question')
                    : (mode = 'app-answer')
                "
              ></component>
            </transition>
          </div>
          <div class="col">
            <app-score></app-score>
          </div>
        </div>
      </div>
      <div class="container container-flid">
        <h3>Reviewed Cards</h3>
        <div class="row row-cols-1">
          <app-reviewed-decks></app-reviewed-decks>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import dashBoardHeader from "@/components/DashboardHeader.vue";
import Question from "../components/Question.vue";
import Score from "../components/Score.vue";
import Answer from "../components/Answer.vue";
import reviewedDecks from "../components/reviewedDecks.vue";
export default {
  // eslint-disable-next-line
  name: "dashboard",
  components: {
    appQuestion: Question,
    appScore: Score,
    appAnswer: Answer,
    appHeader: dashBoardHeader,
    appReviewedDecks: reviewedDecks,
  },
  data() {
    return {
      mode: "app-question",
    };
  },
};
</script>

<style scoped>
.container {
  padding-top: 0.5rem;
  margin-bottom: 1.5rem;
}

.flip-enter-active {
  animation: flip-in 0.5s ease-out forwards;
}
.flip-leave-active {
  animation: flip-out 0.5s ease-out forwards;
}
h3 {
  text-align: center;
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
