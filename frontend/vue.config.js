module.exports = {
  css: {
    loaderOptions: {
      sass: {
        additionalData: `
            @import "@/assets/style/reset.scss";
            @import "@/assets/style/variables.scss";
          `
      }
    }
  }
};