FROM node:12.18.1-slim

# Creamos el directorio /opt/microservices/ratings y copiamos los ficheros necesarios al contenedor
RUN mkdir -p /opt/microservices/ratings
COPY src/package.json /opt/microservices/ratings/
COPY src/ratings.js /opt/microservices/ratings/

# Variable de entorno
ENV SERVICE_VERSION=v1

# Instalamos las dependencias necesarias
RUN cd /opt/microservices/ratings && npm install

# Exponemos el puerto 9080
EXPOSE 9080

# Ejecutamos el fichero app.js al iniciar el contenedor
CMD ["node", "/opt/microservices/ratings/ratings.js". "9080"]

# Comando para construir la imagen de ratings:
# $ docker build -t g40/ratings .
