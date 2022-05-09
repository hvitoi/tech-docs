# Specify a base image
FROM node:alpine

# /usr/app stores the node apps
WORKDIR /usr/app

# With this setup, only changes to package.json will reinstall depenendencies
COPY ./package.json ./
RUN npm install
COPY ./ ./

# Default command
CMD ["npm", "start"]