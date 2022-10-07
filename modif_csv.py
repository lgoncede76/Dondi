import pandas as pd

ds = pd.read_csv("Registro_Diario.csv")


ul_ci = int(ds.shape[0])

for i in range(0, ul_ci):
    print("Linea: "+str(i))

print(ds)

datos_linea = ds.iloc[1350]    

print(datos_linea)

indice = datos_linea['Unnamed: 0']

print('Fecha: ' + str(indice))
