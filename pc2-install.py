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
os.system('sudo apt-get -y install python3')
os.system('sudo apt-get -y install python3-pip')

# Instalamos git y clonamos el repositorio de la practica
os.system('sudo apt install git')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2')

# Modificamos el archivo requirements.txt con las versiones actualizadas
os.system('echo "" > ./practica_creativa2/bookinfo/src/productpage/requirements.txt')
fin = open ("./practica_creativa2/bookinfo/src/productpage/requirements.txt","w+")
fin.write("certifi\n")
fin.write("chardet\n")
fin.write("Click\n")
fin.write("contextlib2\n")
fin.write("dominate\n")
fin.write("Flasks\n")
fin.write("Flask-Bootstrap\n")
fin.write("Flask-JSON\n")
fin.write("future\n")
fin.write("futures\n")
fin.write("gevent\n")
fin.write("greenlet\n")
fin.write("idna\n")
fin.write("itsdangerous\n")
fin.write("jaeger-client\n")
fin.write("Jinja2\n")
fin.write("json2html\n")
fin.write("MarkupSafe\n")
fin.write("nose\n")
fin.write("opentracing\n")
fin.write("opentracing-instrumentation\n")
fin.write("requests\n")
fin.write("simplejson\n")
fin.write("six\n")
fin.write("threadloop\n")
fin.write("thrift\n")
fin.write("tornado\n")
fin.write("urllib3\n")
fin.write("visitor\n")
fin.write("Werkzeug\n")
fin.write("wrapt\n")
fin.close()
# Instalar las dependencias especificadas en requirements.txt
subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
# Instalamos las librerias que dan problemas
os.system('pip install urllib3')
os.system('pip install visitor')
os.system('pip install wrapt')
os.system('pip install flask_bootstrap')
os.system('pip install Flask Werkzeug -U')
os.system('pip install jaeger-client')
os.system('pip install opentracing-instrumentation')
os.system('pip install json2html')
os.system('pip install Flash')

# Modificar el código de la aplicación para que en el título aparezca el nombre del grupo. que hay que cambiar?
"""
group_number = os.environ["GRUPO 40"]
with open("./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "r") as f:
    code = f.read()
code = code.replace("<GROUP_NUMBER>", group_number)
with open("./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "w") as f:
    f.write(code)
"""

# Ejecutar la aplicación especificando el puerto deseado
port = 8080  # Especificar el puerto deseado aquí
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(port)])
