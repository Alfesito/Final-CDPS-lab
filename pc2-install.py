#!/usr/bin/python3
# Grupo 40:
#   - Ana Clara Pérez Acosta
#   - Andrés Alfaro Fernández 
#   - Fernando Castell Miñón

import os
import subprocess

# Puerto del servicio
port = 8080

# Actualizamos el sistema
os.system('sudo apt-get -y update')
os.system('sudo apt-get -y upgrade')

# Habilitamos el FW y el puerto donde queremos desplegar nuestro servicio
os.system('sudo ufw enable')
os.system('sudo ufw allow '+str(port)+'/tcp')
# Instalamos Python y pip
os.system('sudo apt-get -y install python3.9') #las versiones 3.8 y 3.9 son estables
os.system('sudo apt-get -y install python3-pip')

# Instalamos git y clonamos el repositorio de la practica
os.system('sudo apt-get -y install git')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2')

# Instalar las dependencias especificadas en requirements.txt
subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
# Instalamos las librerias que dan problemas de versiones
os.system('pip install urllib3')#
os.system('pip install flask_bootstrap')#
os.system('pip install jaeger-client')#
os.system('pip install opentracing-instrumentation')#

# Modificar el código de la aplicación para que en el título aparezca el nombre del grupo.
os.environ['GROUP_NUMBER'] = "Grupo 40"
group_number = os.environ['GROUP_NUMBER']
# Para index.html
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "r") as f:
    code = f.read()
code = code.replace("Simple Bookstore App", group_number)
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "w") as f:
    f.write(code)
# Para productpage.html
with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r") as f:
    code = f.read()
code = code.replace("Simple Bookstore App", group_number)
with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w") as f:
    f.write(code)

# Ejecutar la aplicación especificando el puerto deseado
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(port)])
