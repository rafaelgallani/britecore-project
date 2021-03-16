# Britecore Project - Frontend
Developed using [Vue.js (`v2`)](https://vuejs.org/). Initially Vue.js `v3` was chosen, but eventually the change was needed, since lots of plugins are only compatible for versions `<= 2.0`. [NGINX](https://www.nginx.com/) is used in the production state/Dockerfile. 
In case you want to develop locally without rebuilding the image, you will need to change requests made to the `/api/(...)` path: these are routed through NGINX, you must append `http://localhost:CHOSEN_API_PORT` to them. This could be refactored easily, but there was not much time left on the project. Feel free to open an issue! :)

## Tools:
- `npm`: `7.5.1`
- `node`: `v15.8.0`
- `@vue/cli`: `4.5.11`

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
