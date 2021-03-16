<template>
  <div class="about">
    <div class="block">
      <h1>Made by <b>Rafael Galani.</b></h1>
      <p>An insurance system PoC designed as a project for <a href="https://www.britecore.com/" target="_blank" rel="noopener">BriteCore</a>.</p>
    </div>
    <div class="block">
      <p><b>Backend</b>: Python (uWSGI, Django, Django Rest Framework) + PostgreSQL + NGINX</p>
      <p><b>Frontend</b>: Vue.js + NGINX</p>
    </div>
    
    <div class="block">
      <p>This instance is hosted in AWS using ECS. All the development was containerized, so cloud deployment is seamless.</p>
      <p>Check the <a href="https://github.com/rafaelgalani/britecore-project" target="_blank" rel="noopener">repository</a> for more details.</p>
    </div>

    <div class="block">
      <p>Follow me: </p>
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
    </div>
  </div>
</template>

<style lang="scss">
.about {
  margin-left: 15px;
  line-height: 1.2;
}

.block + .block{
  padding-top: 15px;
}

b{
  font-weight: bolder;
}
</style>