import argparse
import socket
from cryptography.fernet import Fernet

msj= input("Que mensaje quiere enviar: ")
description = """Modo de uso:
    client.py -msj "Mensaje a enviar"""
parser = argparse.ArgumentParser(
    description='Port scanning',
    epilog=description,
    formatter_class=argparse.RawDescriptionHelpFormatter)
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)
file = open('clave.key', 'wb')
file.write(clave)
file.close() 
mensaje = msj
Msj_Bytes = mensaje.encode()
msj_cifrado = cipher_suite.encrypt(Msj_Bytes)
print("Mensaje enviado:\n", mensaje)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(msj_cifrado)
msj = s.recv(BUFFER_SIZE).decode()
s.close()

print("Respuesta enviada:", msj)
