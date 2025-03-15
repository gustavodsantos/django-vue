# Usar a imagem base do Node.js 20 com Alpine Linux
FROM node:20-alpine

# Definir o diretório de trabalho
WORKDIR /frontend

# Copiar os arquivos de definição de dependências
COPY package.json package-lock.json ./

# Instalar as dependências
RUN npm install

# Copiar o restante dos arquivos do projeto
COPY . /frontend

# Executar o build do projeto
RUN npm run build

# Expor a porta 80 (porta padrão para produção)
EXPOSE 3000

# Comando para servir os arquivos de produção
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]