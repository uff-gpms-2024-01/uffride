
# develop stage
FROM node:21-alpine3.18 as develop-stage
WORKDIR /app
COPY package*.json ./
RUN npm i -g @quasar/cli

# build stage
FROM develop-stage as build-stage
RUN npm i
RUN quasar build

# # production stage
# FROM nginx:1.17.5-alpine as production-stage
# COPY --from=build-stage /app/dist/spa /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
