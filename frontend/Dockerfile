
FROM node:20.5-alpine
WORKDIR /app
COPY package.json* ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npx tailwindcss -i ./styles.css -o ./public/tailwind.css --minify || true
CMD ["npm", "run", "dev"]
