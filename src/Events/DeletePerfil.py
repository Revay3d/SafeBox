import os
from colorama import Fore, init
from Events.Acctions import mensaje
def borra_carpetas(carpeta):
    mensaje(Fore.RED + "Se borro con exito.")
    os.system(f"rmdir /S /Q .{carpeta}")
    os.system(f"rmdir /S /Q .config")
