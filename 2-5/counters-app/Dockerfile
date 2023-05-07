FROM node:18.16.0-alpine3.17
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
ENV NAME=hodi
CMD ["npm","start"]