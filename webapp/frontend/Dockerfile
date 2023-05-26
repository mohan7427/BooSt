FROM node:18.15.0-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build --prod

FROM nginx:1.21-alpine

COPY --from=build /app/dist/falbst /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]