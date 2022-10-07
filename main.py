import pandas as pd

import os
import time

from datetime import datetime


fecha_actual = datetime.now().date()


opt= 0
while opt != 4:

    os.system("clear")

    ds = pd.read_csv("Registro_Diario.csv", index_col=0)

    prov = ds.groupby('Proveedor', as_index=False).sum('Monto')

    prov_act = prov.loc[prov['Monto'] != 0, ['Proveedor']]

    print("1.- Agregar Registro")
    print("2.- Rellenar")
    print("3.- Proveedores")
    print("4.- Salir")

    opt  = int(input(">>> "))



    match opt:
        case 1:
            os.system("clear")
            print("\nAgregar Regiatro")
            input("Precione Enter ...")

        case 2:

            os.system("clear")

            print("\nRellenar")

            total_lineas_column  = ds.shape

            total_lineas= total_lineas_column[0]

            ultimo_registro = ds.iloc[total_lineas - 1]
            
            #Tomando la fecha como stream
            ultima_fecha = ultimo_registro['Fecha']


            print(type(ultima_fecha), ultima_fecha)


            input("Precione Enter ...")

        case 3:

            os.system("clear")
            print("Proveedores Actuales")
            print("."*20)

            print(prov_act)

            print("."*20)
            
            input("Precione Enter ...")

        case 4:

            os.system("clear")
            print("Saliendo ...")
            time.sleep( 2 )
            os.system("clear")
