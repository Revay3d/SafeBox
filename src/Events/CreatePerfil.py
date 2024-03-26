import base64
import os

from colorama import Fore, init

def escribir_configuracion(contraseña, carpeta, intentos, bloqueo,):
    with open(".config/config.txt", "w") as f:
        contraseña_codificada = base64.b64encode(contraseña.encode()).decode()
        f.write(
            f"{contraseña_codificada}\n{carpeta}\n{intentos}\n{bloqueo}\n")
        


def crear_carpeta(carpeta): 
    if not os.path.exists(f".{carpeta}"):
        os.mkdir(f".{carpeta}")

  
     


        