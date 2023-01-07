<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <h3>Flash Card App</h3>
        <div class="d-flex">
          <a
            class="btn btn-primary"
            data-bs-toggle="modal"
            href="#exampleModalToggle"
            role="button"
            >Sign In</a
          >
          <a
            class="btn btn-primary"
            data-bs-toggle="modal"
            href="#exampleModalToggle2"
            role="button"
            >Sign Up</a
          >
          <app-signin></app-signin>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import Signin from "./Signin.vue";
export default {
  // eslint-disable-next-line
  name: "Header",
  components: {
    appSignin: Signin,
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
