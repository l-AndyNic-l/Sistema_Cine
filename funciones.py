# Funciones.py

import os

asientos = [
    {
        "fila": "A",
        "asientos": [
            {
                "numero": 1,
                "disponibilidad": 0
            },    
            {
                "numero": 2,
                "disponibilidad": 0
            },    
            {
                "numero": 3,
                "disponibilidad": 0
            },    
            {
                "numero": 4,
                "disponibilidad": 0
            },    
            {
                "numero": 5,
                "disponibilidad": 0
            },    
        ]
    },
    {
        "fila": "B",
        "asientos": [
            {
                "numero": 1,
                "disponibilidad": 0
            },    
            {
                "numero": 2,
                "disponibilidad": 0
            },    
            {
                "numero": 3,
                "disponibilidad": 0
            },    
            {
                "numero": 4,
                "disponibilidad": 0
            },    
            {
                "numero": 5,
                "disponibilidad": 0
            },  
        ],
    },  
    {
        "fila": "C",
        "asientos": [
            {
                "numero": 1,
                "disponibilidad": 0
            },    
            {
                "numero": 2,
                "disponibilidad": 0
            },    
            {
                "numero": 3,
                "disponibilidad": 0
            },    
            {
                "numero": 4,
                "disponibilidad": 0
            },    
            {
                "numero": 5,
                "disponibilidad": 0
            },  
        ]
    },
    {
        "fila": "D",
        "asientos": [
            {
                "numero": 1,
                "disponibilidad": 0
            },    
            {
                "numero": 2,
                "disponibilidad": 0
            },    
            {
                "numero": 3,
                "disponibilidad": 0
            },    
            {
                "numero": 4,
                "disponibilidad": 0
            },    
            {
                "numero": 5,
                "disponibilidad": 0
            },  
        ],
    },
    {
        "fila": "E",
        "asientos": [
            {
                "numero": 1,
                "disponibilidad": 0
            },    
            {
                "numero": 2,
                "disponibilidad": 0
            },    
            {
                "numero": 3,
                "disponibilidad": 0
            },    
            {
                "numero": 4,
                "disponibilidad": 0
            },    
            {
                "numero": 5,
                "disponibilidad": 0
            },  
        ]
    },
]

ventas = []


def mostrar_asientos():
    
    print( "\n-------------------------------" )
    print( "         Pantalla Cine" )
    print( "-------------------------------" )

    for fila in asientos:

        print( f"\nFila { fila[ 'fila' ] }:", end="" )

        for asiento in fila[ "asientos" ]:

            if asiento[ "disponibilidad" ] == 0:

                print ( f" [{ asiento[ 'numero' ] }] ", end="" )

            else:
                print ( f" [X] ", end="" )

def comprar_entrada():

    fila = buscar_fila( "\n*Ingrese la fila ( A a la E ): " )

    columna = buscar_columna( fila, "Ingrese la columna de asiento ( 1 al 5 ): " )

    nombre = input( "Ingrese su nombre: " )

    venta = {
        "nombre": nombre,
        "fila": fila[ "fila" ],
        "asiento": columna,
        "precio": 10.00
    }

    ventas.append( venta )
    print( "Entrada comprada exitosamente." )

def buscar_fila( mensaje ):

    fila = input( mensaje ).strip().title()

    for f in asientos:

        if f[ "fila" ] == fila:

            return f
        
    print( "ERROR! La fila ingresada no existe." )

def buscar_columna( fila, mensaje ):

    columna = int( input( mensaje ) )

    for c in fila[ "asientos" ]:

        if c[ "numero" ] == columna:

            if c[ "disponibilidad" ] == 0:

                print( "Asiento disponible!" )

                c[ "disponibilidad" ] = 1

                return c
            
            else:
                print( "Asiento NO disponible!" )
                return

    print( "ERROR! La columna ingresada no existe." )

def mostrar_ventas():

    if not ventas:

        print( "No se han realizado ventas." )

    else:

        for v in ventas:

            print( f"Nombre: { v[ 'nombre' ] } | Entrada: Fila { v[ 'fila' ] }-{ v[ 'asiento' ][ 'numero' ] } | Precio: { v[ 'precio' ] }" )

def limpiar_pantalla( titulo ):

    os.system( "cls" )
    print( titulo )