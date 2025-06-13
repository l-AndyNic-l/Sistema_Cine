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

def mostrar_asientos():

    for fila in asientos:

        print( f"\nFila { fila[ 'fila' ] }:", end="" )

        for asiento in fila[ "asientos" ]:

            if asiento[ "disponibilidad" ] == 0:

                print ( f" [{ asiento[ 'numero' ] }] ", end="" )

            else:
                print ( f" [X] ", end="" )

def limpiar_pantalla( titulo ):

    os.system( "cls" )
    print( titulo )