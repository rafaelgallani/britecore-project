<template>
  <header class="header-content">
    <img
      class="logo"
      alt="Vue logo"
      src="@/assets/logo.svg"
      @click="goToHome"
    />
    <div id="nav">
      <router-link to="/">
        Home
      </router-link> |
      <router-link to="/about">
        About
      </router-link>
    </div>
  </header>
</template>

<script>
  export default {
    name: "Header",
    methods: {
      goToHome(){
        this.$router.push("/");
      }
    }
  };
</script>


<style lang="scss" scoped>
  .header-content {
    position: sticky;
    top: 0;
    background: $navbar-background;
    border-bottom: 1px solid $navbar-border-color;
    display: flex;
    width: 100%;
    justify-content: space-between;
    z-index: 100;

    .logo {
      max-width: 300px;
      min-width: 200px;
      width: 15%;
      cursor: pointer;
    }

    #nav {
      padding: 30px;

      a {
        text-decoration: none;
        font-weight: bold;
        color: #2c3e50;

        &.router-link-exact-active {
          color: $primary-color;
        }
      }
    }
  }
</style>