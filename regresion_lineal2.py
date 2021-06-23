import pandas as pd # manejo de datos
import seaborn as sns #creacion de graficas y visualizacion de datos
import matplotlib.pyplot as plt #depandencia para crear graficos

df = pd.read_csv("/Datacademi/studentsperformance_15085fee-8bc7-4d33-a182-655428728fe1.csv")

df.head()
df.shape #tamaño
df.columns # nos devulve las columnas
df.dtypes #nos devuelve el tipo de cada columna
df.mean() #nos devulve el promedio
df.median() #nos devuelve la mediana