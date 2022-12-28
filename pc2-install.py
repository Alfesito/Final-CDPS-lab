#!/usr/bin/python3
# Grupo 40:
#   - Ana Clara Pérez Acosta
#   - Andrés Alfaro Fernández 
#   - Fernando Castell Miñón

import os
import subprocess

# Actualizamos el sistema
os.system('sudo apt-get update')
os.system('sudo apt-get -y upgrade')

# Instalamos Python y pip
os.system('sudo apt-get -y install python3.8')
os.system('sudo apt-get -y install python3-pip')

# Instalamos git y clonamos el repositorio de la practica
os.system('sudo apt -y install git')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2')


# Instalamos las librerias que dan problemas
#os.system('pip install urllib3')
#os.system('pip install visitor')
#os.system('pip install wrapt')
#os.system('pip install flask_bootstrap')
#os.system('pip install Flask Werkzeug -U')
#os.system('pip install jaeger-client')
#os.system('pip install opentracing-instrumentation')
#os.system('pip install json2html')
#os.system('pip install Flash')

# Instalar las dependencias especificadas en requirements.txt
subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])

# Modificar el código de la aplicación para que en el título aparezca el nombre del grupo. que hay que cambiar?
os.environ['GROUP_NUMBER'] = "Grupo 40"
group_number = os.environ['GROUP_NUMBER']
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "r") as f:
    code = f.read()
code = code.replace("Simple Bookstore App", group_number)
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "w") as f:
    f.write(code)


# Ejecutar la aplicación especificando el puerto deseado
port = 8080  # Especificar el puerto deseado aquí
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(port)])
