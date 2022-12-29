FROM ruby:2.7.1-slim

# Copiamos el fichero details.rb al contenedor
COPY details.rb /opt/microservices/

# Establecemos las variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Exponemos el puerto 9080
EXPOSE 9080

# Ejecutamos el fichero details.rb al iniciar el contenedor
CMD ["ruby", "/opt/microservices/details.rb", "9080"]

# Comando para construir la imagen de details:
    # $ docker build -t g40/details .
