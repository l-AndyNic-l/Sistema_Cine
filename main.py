# Main.py

from funciones import *
import msvcrt

menu = """=========== Menu ==========
1) Mostrar asientos.
2) Comprar entrada.
3) Ver lista de ventas.
4) Salir del sistema.
===========================
"""

while True:

    limpiar_pantalla( menu )

    opcion = input( "Ingrese una opció: " )

    if opcion == "1":
        pass

    elif opcion == "2":
        pass

    elif opcion == "3":
        pass

    elif opcion == "4":
        
        print( "Gracias, adios." )
        break

    else:
        print( "ERROR! Ingrese una opción válida." )

    print( "\n\n*Para continuar presione una tecla*" )
    msvcrt.getch()
