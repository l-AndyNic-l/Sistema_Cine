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

    opcion = input( "* Ingrese una opción: " )

    if opcion == "1":
        
        limpiar_pantalla( "====== Mostrar asientos ======" )

        mostrar_asientos()

    elif opcion == "2":
        
        limpiar_pantalla( "====== Comprar Entrada ======" )

        comprar_entrada()

    elif opcion == "3":
        
        limpiar_pantalla( "====== Ver Lista de Ventas ======\n" )

        mostrar_ventas()

    elif opcion == "4":
        
        print( "Gracias, adios." )
        break

    else:
        print( "ERROR! Ingrese una opción válida." )

    print( "\n\n*Para continuar presione una tecla*" )
    msvcrt.getch()
