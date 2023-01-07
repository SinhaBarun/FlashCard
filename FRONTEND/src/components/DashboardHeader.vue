<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <h3>Flash Card App</h3>
        <div class="d-flex">
          <span class="navbar-text">
            <strong>Welcome {{ currentUsername }}</strong>
          </span>
          <a
            class="btn btn-primary"
            data-bs-toggle="modal"
            href="#exampleModalToggle2"
            role="button"
            @click="logOut"
            >Log Out</a
          >
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "dashBoardHeader",
  data() {
    return {
      currentUsername: this.$store.getters.currentUsername,
    };
  },
  methods: {
    logOut() {
      const token = this.$store.getters.access_token;
      const config = {
        headers: {
          Authorization: "Bearer " + token,
        },
      };
      axios
        .post("/logout", {}, config)
        .then((res) => {
          console.log(res);
          this.$router.push("/");
        })
        .catch((err) => {
          console.log(token);
          console.log(err);
        });
    },
  },
};
</script>

<style>
nav {
  background-color: #8ec5fc;
  background-image: linear-gradient(62deg, #8ec5fc 0%, #e0c3fc 100%);
}
.btn {
  margin-left: 10px;
}
h3 {
  font-family: "Source Sans Pro", sans-serif;
  color: beige;
}
</style>
