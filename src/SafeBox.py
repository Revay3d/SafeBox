# Importaciones

import base64
import os
import time
import stdiomask
from colorama import Fore, init
from Events.CreatePerfil import escribir_configuracion, crear_carpeta
from Events.Acctions import clear_screen, ocultar_carpeta, cuenta_regresiva, mostrar_carpeta, mensaje
from Events.DeletePerfil import borra_carpetas
# Verifica si la carpeta config existe y si no la crea
if not os.path.exists(".config"):
    os.mkdir(".config")
os.system(f"attrib +h +r +s .config")

# Funciones




def leer_configuracion():
    try:
        with open(".config/config.txt", "r") as f:
            lineas = f.readlines()
            contraseña = base64.b64decode(lineas[0].strip()).decode()
            carpeta = lineas[1].strip()
            intentos = int(lineas[2].strip())
            bloqueo = lineas[3].strip() == 'True'

    except FileNotFoundError:
        contraseña, carpeta, intentos, bloqueo = "", "", 0, False
    return contraseña, carpeta, intentos, bloqueo








# Almacena las variables de la función leer_configuracion en variables globales
contraseña, carpeta, intentos, bloqueo = leer_configuracion()


# Comprueba si las variables están vacías y si es así las crea

if not contraseña:
    while True:
        contraseña = input("Crea una contraseña: ")
        entrada_usuario = input("Confirmar contraseña: ")
        if entrada_usuario == contraseña:
            break
        else:
            print("No concuerdan las contraseñas creadas... Intenta de nuevo.")
            time.sleep(2)
            clear_screen()

if not carpeta:
    carpeta = input("Crea el nombre de la carpeta: ")

if not intentos:
    intentos = int(input("¿Cuántas oportunidades?: "))

# Copia las variables globales y las pone en la función
escribir_configuracion(contraseña, carpeta, intentos, bloqueo)

# Crea la carpeta con el nombre estipulado
crear_carpeta(carpeta)

clear_screen()

while intentos > 0:
    # Llave o bloqueo comprueba si la carpeta está abierta

    if bloqueo:
        entrada_usuario = input("La carpeta se cerrará, ¿estás seguro? s/n: ")
        if entrada_usuario == "s":
            cuenta_regresiva(2, Fore.YELLOW +
                             "       La carpeta se cerrará ")
            escribir_configuracion(contraseña, carpeta,
                                   intentos, False)
            ocultar_carpeta(carpeta)
            break
        else:
            mensaje(Fore.WHITE + "Ok, no hay problema...")
            time.sleep(3)
            break
     # Si está cerrada le pregunta la contraseña
    else:
        # Contraseña encriptada
        entrada_usuario = stdiomask.getpass(
            prompt="Ingresa la contraseña: ", mask=f"#")

        # Valida si a puesto Del para borrar carpeta + config
        if entrada_usuario == "Del":
            print(
                Fore.RED + f'ADVERTENCIA: Estás a punto de eliminar la carpeta .{carpeta} y todos sus contenidos.')
            print('Esto incluye la contraseña de la carpeta, todas sus configuraciones y cualquier archivo guardado en ella.')
            entrada_usuario = input(
                '¿Estás seguro de que deseas continuar? (s/n): ')
            if entrada_usuario == "s":
                borra_carpetas(carpeta)
                time.sleep(5)
                break
            else:
                clear_screen()
                mensaje(Fore.GREEN + "Se canselo la accion.")
                time.sleep(5)
                break
           # Valida si a puesto CCO para cambiar contraseña.
        elif entrada_usuario == "CCO":
            clear_screen()
            mensaje(Fore.WHITE + "Cambiar contraseña")
            entrada_usuario = input("\nContraseña anterior: ")    
            if entrada_usuario == contraseña:
                nueva_contraseña  = input("\nNueva contraseña: ")
                contraseña = nueva_contraseña
                escribir_configuracion(contraseña, carpeta, intentos, bloqueo)
                cuenta_regresiva(1, Fore.WHITE + "Actualizada con exito, reinicio")
                break 
          
            else:
                cuenta_regresiva(3, Fore.MAGENTA + "Contraseña incorecta, se cerrando")  
                break 

         # de lo contrario ve si la contraseña es correcta    
        elif entrada_usuario == contraseña:
            clear_screen()
            mensaje(Fore.GREEN + " Contraseña correcta")
            mostrar_carpeta(carpeta)
            escribir_configuracion(contraseña, carpeta,
                                   intentos, True)
            time.sleep(1)
            break

        # Si no lo es, le quita los intentos establecidos
        else:
            clear_screen()
            mensaje(Fore.RED + " Contraseña incorrecta")
            intentos -= 1

# Cierra la carpeta.
else:
    clear_screen()
    print("Cargando...")
    cuenta_regresiva(2, Fore.MAGENTA + "La carpeta se cerrará por precaución")
    ocultar_carpeta(carpeta)
