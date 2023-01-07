<template>
  <div>
    <div
      class="modal fade"
      id="exampleModalToggle"
      aria-hidden="true"
      aria-labelledby="exampleModalToggleLabel"
      tabindex="-1"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalToggleLabel">Sign In</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input
                type="email"
                class="form-control"
                placeholder="name@example.com"
                id="floatingInput"
                v-model="user.username"
              />
              <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating">
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                v-model="user.password"
                id="floatingPassword"
              />
              <label for="floatingPassword">Password</label>
            </div>
          </div>
          <div class="modal-footer">
            <button
              class="btn btn-primary"
              data-bs-target="#exampleModalToggle2"
              data-bs-toggle="modal"
            >
              Create Account
            </button>
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-primary"
              @click="onSignIn"
            >
              Sign In
            </button>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="exampleModalToggle2"
      aria-hidden="true"
      aria-labelledby="exampleModalToggleLabel2"
      tabindex="-1"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalToggleLabel2">Sign Up</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="form-floating mb-3">
              <input
                type="email"
                class="form-control"
                placeholder="name@example.com"
                id="floatingInput"
                v-model="user.username"
              />
              <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating">
              <input
                type="password"
                class="form-control"
                id="floatingPassword"
                placeholder="Password"
                v-model="user.password"
              />
              <label for="floatingPassword">Password</label>
            </div>
          </div>
          <div class="modal-footer">
            <button
              class="btn btn-primary"
              data-bs-target="#exampleModalToggle"
              data-bs-toggle="modal"
            >
              Already Have Account ? Sign In
            </button>
            <button type="button" class="btn btn-primary" @click="onSignUp">
              Sign Up
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";
import { mapGetters } from "vuex";
export default {
  // eslint-disable-next-line
  name: "Signin",

  data() {
    return {
      ...mapGetters(["isAuthenticated"]),
      user: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    ...mapActions(["makeAuthenticated"]),

    onSignIn() {
      axios
        .post("/login", {
          username: this.user.username,
          password: this.user.password,
        })
        .then((res) => {
          if (res.status == 200) {
            this.$store.getters.currentUsername = res.data.username;
            this.$store.getters.access_token = res.data.access_token;
            this.$store.state.isAuthenticated = true;
            console.log(this.$store.state.isAuthenticated);
            this.$router.push("/dashboard");
          }
        })
        .catch((err) => console.log(err));
    },

    onSignUp() {
      axios
        .post("/user", {
          username: this.user.username,
          password: this.user.password,
        })
        .then((res) => {
          console.log(res);
          if (res.status == 201) {
            prompt("Please LogIn ==> Dashboard");
            this.$router.push("/");
          }
          console.log(res.status);
          console.log(res.data);
        })
        .catch((err) => {
          if (err.status == 409) {
            prompt("Please enter a different Username");
          }
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.modal-content {
  background-color: #8ec5fc;
  background-image: linear-gradient(62deg, #8ec5fc 0%, #e0c3fc 100%);
}
.g-2 {
  margin: 0px 0px 10px 0px;
}
</style>
