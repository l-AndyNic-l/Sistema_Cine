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

    while True:

        fila = buscar_fila( "\n*Ingrese la fila ( A a la E ): " )

        columna = buscar_columna( fila, "\n*Ingrese la columna de asiento ( 1 al 5 ): " )

        if columna != False:
        
            nombre = validar_nombre( "\n*Ingrese su nombre para realizar la compra: " )

            venta = {
                "nombre": nombre,
                "fila": fila[ "fila" ],
                "asiento": columna,
                "precio": 10.00
            }

            ventas.append( venta )
            print( f"\n*** La entrada Fila { fila['fila'] }-{ columna['numero'] }, fue comprada exitosamente por { nombre } ***" )
            print( "--------------------" )
            print( "Total pagado: $10.0" )
            print( "--------------------" ) 
            break

def buscar_fila( mensaje ):

    while True:

        fila = validar_fila( mensaje )

        for f in asientos:

            if f[ "fila" ] == fila:

                return f
        
        print( "ERROR! La fila ingresada no existe." )

def buscar_columna( fila, mensaje ):

    while True:
        columna = validar_columna( mensaje )

        for c in fila[ "asientos" ]:

            if c[ "numero" ] == columna:

                columna_econtrada = True

                if c[ "disponibilidad" ] == 0:

                    print( "\n|| El asiento se encuentra disponible! ||" )

                    c[ "disponibilidad" ] = 1

                    return c
            
                else:
                    print( "\n|| El asiento NO se encuentra disponible! ||" )
                    return False      

        if columna_econtrada == False:

            print( "ERROR! La columna ingresada no existe." ) 

        else:
            break       

def mostrar_ventas():

    contador = 1

    if not ventas:

        print( "No se han realizado ventas." )

    else:

        for v in ventas:

            print( f"{ contador }) Nombre: { v[ 'nombre' ] } | Entrada: Fila { v[ 'fila' ] }-{ v[ 'asiento' ][ 'numero' ] } | Total: { v[ 'precio' ] }" )
            contador += 1


def limpiar_pantalla( titulo ):

    os.system( "cls" )
    print( titulo )


# Validaciones.

def validar_fila( mensaje ):

    while True:

        fila = input( mensaje ).strip().title()

        if len( fila ) == 1:

            return fila
        
        else:
            print( "ERROR! Debe ingresar una letra dentro del rango de A a la E." )

def validar_columna( mensaje ):

    while True:
        try:
            columna = int( input( mensaje ) )

            if columna >= 1 and columna <= 5:
                
                return columna
            
            else:
                print( "ERROR! Debe ingresar un número de columna dentro del rango 1 a 5." )

        except:
            print( "ERROR! Debe ingresar un número de columna válido." )

def validar_nombre( mensaje ):

    while True:

        nombre = input( mensaje ).strip().title()

        if len( nombre ) >= 3:

            return nombre
        
        else:
            print( "ERROR! Debe ingresar un nombre con más de 3 carácteres." )
