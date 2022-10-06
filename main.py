import pandas as pd

import os


os.system("clear")
ds = pd.read_csv("Registro_Diario.csv", index_col=0)

#print(ds)

#Menu
opt=3
while opt != 4:
    print("1.- Agregar Registro")
    print("2.- Rellenar")
    print("3.- Proveedores")
    print("4.- Salir")

    opt  = int(input(">>>"))



    match opt:
        case 1:
            os.system("clear")
            print("\nAgregar Regiatro")
        case 2:
            os.system("clear")
            print("\nRellenar")
        case 3:
            os.system("clear")
            print("Proveedores Actuales")
            print("."*20)

            prov_act = ds.groupby('Proveedor', as_index=False).sum('Monto')

            prov_act = prov_act.loc[prov_act['Monto'] != 0, ['Proveedor']] 
            print(prov_act)
            input()
        case 4:
            os.system("clear")
            print("\nSaliendo ...")