import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    currentUsername: "",
    access_token: "",
    correctAns: 0,
    incorrectAns: 0,
    ans: "",
    reviewedWords: [],
  },
  getters: {
    correctAns: (state) => {
      return state.correctAns;
    },
    incorrectAns: (state) => {
      return state.incorrectAns;
    },
    reviewedWords: (state) => {
      return state.reviewedWords;
    },
    isAuthenticated: (state) => {
      return state.isAuthenticated;
    },
  },
  mutations: {},
  actions: {},
  modules: {},
});
