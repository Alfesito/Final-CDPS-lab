#!/usr/bin/python3
# Grupo 40:
#   - Ana Clara Pérez Acosta
#   - Andrés Alfaro Fernández 
#   - Fernando Castell Miñón

# Librerias para ejecucion de comandos
import sys
import subprocess
from subprocess import STDOUT
import os
# Libreria para logs
import logging
# Libreria para la modificación de archivos XML
from lxml import etree

#Lista de nombre para los servidores
servers_name=["c1","lb","s1","s2","s3"]
vms=list()

debugmode = False
num_servers = 3

def create():
    logger.debug('Creando...')
    logger.debug('Se verifica el parametro de numero de servidores')
    
    if num_servers is not None:
        cont = 0
        for i in servers_name:
            if str(cont) <= num_servers:
                vms.append(i)
                cont=cont+1
            else:
                vms.append(i)
                break

    logger.debug('Se aplican las configuraciones en el host')
    # Creamos los nombres de los bridges que soportan cada una de las LAN
    os.system('sudo brctl addbr LAN1')
    os.system('sudo brctl addbr LAN2')
    os.system('sudo ifconfig LAN1 up')
    os.system('sudo ifconfig LAN2 up')
    # Configuracion de la red LAN1 en el host
    os.system("sudo ifconfig LAN1 10.20.1.3/24")
    os.system("sudo ip route add 10.20.0.0/16 via 10.20.1.1")

    os.system("chmod +rwx cdps-vm-base-pc1.qcow2")

    for i in vms: 
        # Crea y copia la imagen del la VM y el XML para cada  máquina -> https://lxml.de/tutorial.html
        os.system("qemu-img create -f qcow2 -b cdps-vm-base-pc1.qcow2 "+i+".qcow2")
        os.system("cp plantilla-vm-pc1.xml "+i+".xml")
        logger.debug('Modificamos el fichero xml de '+i)
        tree = etree.parse(i+".xml")
        root = tree.getroot()
        root.find("domain")
        name = root.find("name")
        name.text = i
        source = root.find("./devices/disk/source")
        ruta = os.path.abspath(i+".qcow2")
        source.set("file", ruta)
        
        if i == "c1":
            # Editamos XML del c1
            interface = root.find("./devices/interface/source")
            interface.set("bridge", "LAN1")
        elif i== "lb":
            # Editamos el XML del lb
            interface = root.find("./devices/interface/source")
            interface.set("bridge", "LAN1")
            interface_tag = etree.Element("interface", type="bridge")
            devices_tag = root.find("devices")
            interface_tag.text = ""
            devices_tag.append(interface_tag)
            source_tag = etree.Element("source", bridge="LAN2")
            model_tag = etree.Element("model", type="virtio")
            interface_tag.append(source_tag)
            interface_tag.append(model_tag)
        else:
            # Editamos el XML de los servidores
            interface = root.find("./devices/interface/source") 
            interface.set("bridge", "LAN2")  
        tree.write(i+".xml")

        # Definimos las MVs con los XML
        logger.debug('Se define las MV '+i+' con el xml')
        os.system("sudo virsh define "+i+".xml")
        logger.debug('Configurando del fichero hostname de '+i)
        os.system("touch hostname")
        os.system("chmod +rwx hostname")
        fin = open ("hostname","w+")
        fin.write(str(i)+"\n")
        fin.close()
        os.system("sudo virt-copy-in -a "+i+".qcow2 hostname /etc")
        os.system('rm hostname')

        # Deshabilitamos el servicio Apache2 y editamos ip_forward a 1 para hacer que lb trabaje como router
        os.system("touch rc.local")
        os.system("chmod +x rc.local")
        fin1 = open ("rc.local","w+")
        fin1.write("#!/bin/bash\n")
        fin1.write("sudo service apache2 stop\n")
        # Instala y ejecuta el repositorio de bookpage
        if i=="s1" or i=="s2" or i=="s3":
            fin1.write("sudo apt install git\n")
            fin1.write("sudo apt install python3\n")
            fin1.write("git clone https://github.com/Alfesito/PC2.git\n")
            fin1.write("python3 ./PC2/pc2-install.py\n")
        fin1.close()
        os.system("sudo virt-copy-in -a "+i+".qcow2 rc.local /etc")

        subprocess.call(["sudo virt-edit -a lb.qcow2 /etc/sysctl.conf -e 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/'"], shell=True)
            
        # Escribimos el nombre de la máquina en hosts
        logger.debug('Configura el archivo hosts de '+i)
        os.system("cp /etc/hosts hosts")
        fin = open ("hosts","w")
        fout = open ("/etc/hosts", "r")
        for line in fout:
            if "127.0.0.1" in line:
                fin.write("127.0.1.1\t"+i+"\n")
            else:
                fin.write(line)
        fin.close()
        fout.close()
        os.system("sudo virt-copy-in -a "+i+".qcow2 hosts /etc")

        # Modificamos las interfaces según la VM
        # http://fpg.66ghz.com/DebianRed/etcnetworkinterfaces.html
        os.system("touch interfaces")
        os.system("chmod 777 interfaces")
        logger.debug('Configurando el archivo interfaces de '+i)
        fout = open("interfaces","w+")
        if i == "lb":
            fout.write("auto lo \n")
            fout.write("iface lo inet loopback\n")
            fout.write("\nauto eth0 eth1\n")
            fout.write("iface eth0 inet static\n")
            fout.write("\taddress 10.20.1.1\n")
            fout.write("\tnetmask 255.255.255.0\n")
            fout.write("\tgateway 10.20.1.1 \n")
            fout.write("\tdns-nameservers 10.20.1.1\n")
            fout.write("iface eth1 inet static\n")
            fout.write("\taddress 10.20.2.1 \n")
            fout.write("\tnetmask 255.255.255.0\n")
            fout.write("\tgateway 10.20.2.1\n")
            fout.write("\tdns-nameservers 10.20.2.1\n")
        elif i == "c1":
            fout.write("auto lo\n")
            fout.write("iface lo inet loopback\n")
            fout.write("\nauto eth0\n")
            fout.write("iface eth0 inet static\n")
            fout.write("\taddress 10.20.1.2 \n")
            fout.write("\tnetmask 255.255.255.0 \n")
            fout.write("\tgateway 10.20.1.1 \n")
            fout.write("\tdns-nameservers 10.20.1.1\n")
        elif i == "s1":
            fout.write("auto lo \n")
            fout.write("iface lo inet loopback \n")
            fout.write("\nauto eth0 \n")
            fout.write("iface eth0 inet static \n")
            fout.write("\taddress 10.20.2.101 \n")
            fout.write("\tnetmask 255.255.255.0 \n")
            fout.write("\tgateway 10.20.2.1 \n")
            fout.write("\tdns-nameservers 10.20.2.1\n")
        elif i == "s2":
            fout.write("auto lo\n")
            fout.write("iface lo inet loopback\n")
            fout.write("\nauto eth0 \n")
            fout.write("iface eth0 inet static\n")
            fout.write("\taddress 10.20.2.102\n")
            fout.write("\tnetmask 255.255.255.0 \n")
            fout.write("\tgateway 10.20.2.1 \n")
            fout.write("\tdns-nameservers 10.20.2.1\n")
        elif i == "s3":
            fout.write("auto lo\n")
            fout.write("iface lo inet loopback\n")
            fout.write("\nauto eth0\n")
            fout.write("iface eth0 inet static\n")
            fout.write("\taddress 10.0.2.103\n")
            fout.write("\tnetmask 255.255.255.0\n")
            fout.write("\tgateway 10.20.2.1\n")
            fout.write("\tdns-nameservers 10.20.2.1\n")
        fout.close()
        os.system("sudo virt-copy-in -a "+i+".qcow2 interfaces /etc/network")
        os.system('rm interfaces')

    logger.debug('Eliminando archivos no necesarios')
    os.system('rm hosts')
    os.system('rm rc.local')

def start():
    logger.debug('Empezando...')
    for i in vms:
        logger.debug('Iniciando la maquina '+i)
        os.system('sudo virsh start '+i)
        os.system("xterm -e 'sudo virsh console "+i+"'&")

def stop():
    logger.debug('Parando...')
    # Apaga las máquinas
    for i in vms:
        logger.debug('Parando maquina '+i)
        os.system('sudo virsh shutdown '+i)

def destroy():
    logger.debug('Eliminando...')
    # Apaga forzadamente las máquinas
    for i in vms:
        logger.debug('Eliminando maquina '+i)
        os.system('sudo virsh destroy '+i)
        os.system('rm '+i+'.xml')
        os.system('rm '+i+'.qcow2')
    os.system('sudo ifconfig LAN1 down')
    os.system('sudo ifconfig LAN2 down')
    os.system('sudo brctl delbr LAN1')
    os.system('sudo brctl delbr LAN2')

# @main
if len(sys.argv) == 1:
    param1 = str(3)

    if num_servers is not None:
        cont = 0
        for i in servers_name:
            if cont <= num_servers:
                vms.append(i)
                cont=cont+1
            else:
                vms.append(i)
                break
    
# Si debugmode es true, se ejecuta el debuger
    if debugmode:
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger('gestiona-pc1')
    else:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger('gestiona-pc1')

    if sys.argv[1] == 'create':
        create()
    elif sys.argv[1] == 'start':
        start()
    elif sys.argv[1] == 'stop':
        stop()
    elif sys.argv[1] == 'destroy':
        destroy()
else:
    print("\nAlgo no ha salido bien")
    print("Algún parámetro es incorrecto o está fuera de los límites\n")
