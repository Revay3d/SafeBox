import os
import time
from colorama import Fore, init

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ocultar_carpeta(carpeta):
    os.system(f"attrib +h +s +r .{carpeta}")


def mostrar_carpeta(carpeta):
    os.system(f"icacls .{carpeta} /reset")
    os.system(f"attrib -h -s -r .{carpeta}")


def cuenta_regresiva(segundos, mensaje):
    while segundos > -1:

        clear_screen()
        print(Fore.BLUE + f"""
              ==============================================""")
        print(f"                {mensaje} en {segundos}s")
        print(
            Fore.BLUE + f"""              ==============================================""")
        Fore.BLACK
        time.sleep(1)
        segundos -= 1


def mensaje(mensaje):
        
        print(Fore.BLUE + f"""
              ==============================================""")
        print(f"                            {mensaje}")
        print(
            Fore.BLUE + f"""              ==============================================""")
        Fore.BLACK
      

