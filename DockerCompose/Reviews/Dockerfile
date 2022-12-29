FROM openjdk:8-jdk-slim

# Creamos el directorio /opt/microservices/reviews y copiamos los ficheros necesarios al contenedor
RUN mkdir -p /opt/microservices/reviews
COPY reviews-wlpcfg/build/libs/reviews.war /opt/microservices/reviews

# Ejecutamos el fichero reviews.war al iniciar el contenedor
CMD ["java", "-jar", "/opt/microservices/reviews/reviews.war"]

# Compilar y empaquetar los ficheros necesarios ejecutando, dentro de la ruta src/reviews/reviews-wlpcfg, el siguiente comando:
# - En PowerShell:
# $docker run --rm -u root -v "$(Get-Location)"/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
# - En Linux:
# $docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build

# Comando para construir la imagen de review:
    # Version 1
    # $ docker build -t g40/reviews:v1 --build-arg SERVICE_VERSION=v1 .
    # Version 2
    # $ docker build -t g40/reviews:v2 --build-arg SERVICE_VERSION=v2 .
    # Version 3
    # $ docker build -t g40/reviews:v3 --build-arg SERVICE_VERSION=v3 .

