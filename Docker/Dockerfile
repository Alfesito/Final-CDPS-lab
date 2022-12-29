#!/usr/bin/python3
# Grupo 40:
#   - Ana Clara Pérez Acosta
#   - Andrés Alfaro Fernández 
#   - Fernando Castell Miñón

FROM python:3.8
RUN apt-get update && apt-get install -y python3-pip git
COPY . /app
WORKDIR /app
# Clonamos el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2
# Cambiamos versiones que dan problemas en el requirements.txt
RUN sed -i "s/urllib3==1.26.5/urllib3/g" ./practica_creativa2/bookinfo/src/productpage/requirements.txt
# Instalamos las librerias necesarias
RUN pip3 install flask_bootstrap
RUN pip3 install jaeger-client
RUN pip3 install opentracing-instrumentation
RUN pip3 install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt
# Puerto que expone el servicio
EXPOSE 9080
# Variable de entorno GROUP_NUMBER
ENV GROUP_NUMBER=40
RUN sed -i "s/Simple Bookstore App/$GROUP_NUMBER/g" ./practica_creativa2/bookinfo/src/productpage/templates/productpage.html
# Comando para ejecutar el servicio
CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]

# 1. Creamos la imagen:
    # $docker build -t g40/product-page .
# 2. Arrancamos el contenedor con el puerto 9080
    # $docker run -p 9080:9080 --name g40-product-page -d g40/product-page
# 3. Abrimos el navegador: http://localhost:9080/productpage

# Es importante tener en cuenta que, al utilizar un solo contenedor para todos los servicios, 
# es posible que sea más difícil actualizar o cambiar la versión de un servicio específico sin 
# tener que volver a construir e instalar la imagen completa. Además, puede ser más difícil aislar
# y solucionar problemas en un servicio específico si todos están incluidos en un mismo contenedor.
# En general, se recomienda utilizar microservicios para facilitar el despliegue y el mantenimiento 
# de aplicaciones complejas.