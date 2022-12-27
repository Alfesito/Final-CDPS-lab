import os
import subprocess

# Actualizamos el sistema
os.system('sudo apt-get update')
os.system('sudo apt-get -y upgrade')

# Instalamos Python y pip
os.system('sudo apt-get -y install python3.9')
os.system('sudo apt-get -y install python3.9-pip')

# Instalamos git y clonamos el repositorio de la practica
os.system('sudo apt install git')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2')

# Instalar las dependencias especificadas en requirements.txt
subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])

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
subprocess.check_call(["python", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(port)])
