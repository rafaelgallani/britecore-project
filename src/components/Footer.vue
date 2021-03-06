<template>
  <footer class="footer-content">
    <b>{{ msg }}</b>
    <ul>
      <li>
        <a
          href="https://github.com/rafaelgalani"
          target="_blank"
          rel="noopener"
        >github</a>
      </li>
      <li>
        <a
          href="https://linkedin.com/in/rafaelgalani"
          target="_blank"
          rel="noopener"
        >linked</a>
      </li>
    </ul>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  props: {
    msg: {
      type: String,
      default: "made by Rafael Galani"
    }
  }
};
</script>


<style lang="scss" scoped>

.footer-content {
  padding: 10px;
  box-sizing: border-box;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  display: flex;
  background: $primary-color;
  color: $text-on-primary;
  justify-content: space-between;
  align-items: center;

  & *{
    color: $text-on-primary;
  }

  ul {
    list-style-type: none;
    padding: 0;

    li {
      display: inline-block;
      margin: 0 10px;
    }
  }
}
</style>
