# Usar uma imagem base do Node.js
FROM node:18

# Criar e definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos package.json e package-lock.json para instalar dependências
COPY package*.json ./

# Instalar dependências do Node.js
RUN npm install

# Instalar o Vite e React Router DOM
RUN npm install vite react-router-dom

# Copiar o restante do código para o contêiner
COPY . .

# Expor a porta 3000
EXPOSE 3000

# Iniciar o servidor de desenvolvimento
CMD ["npm", "run", "dev"]
