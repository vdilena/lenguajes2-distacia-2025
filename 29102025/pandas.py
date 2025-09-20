import pandas as pd
import matplotlib.pyplot as plt

# Lectura de archivo csv y se transforma en un dataframe
estadisticasUnivDataFrame = pd.read_csv("university_enrollment_data.csv", index_col="Student_ID")

# Leo las primeras 5 filas de los datos
#print("*** Las 5 primeras filas del dataframe ***")
#print(estadisticasUnivDataFrame.head(50))

# Leo las ultimas 20 filas de los datos
#print("*** Las ultimas 20 filas del dataframe ***")
#print(estadisticasUnivDataFrame.tail(20))

# Obtengo informacion estadistica del datframe (cantidad, media, desvio estandar, minimo, maximo, percentiles)
#print("*** Analitica descriptiva del dataframe ***")
#print(estadisticasUnivDataFrame.describe())

# Limpieza de filas que vienen con datos vacios
dataframeLimpio = estadisticasUnivDataFrame.dropna()
#print("*** Trabajo con un dataframe sin las filas con datos faltantes ***")
#print(dataframeLimpio.head())

# Relleno los datos que vienen vacios, dependiendo de la columna
estadisticasUnivDataFrame = estadisticasUnivDataFrame.fillna({"Country":" ", "Field_of_Study": " ", "Age":0, "Gender":" ", "Year_of_Enrollment": 0})
#print("*** Indico con que rellenar cada celda vacia del dataframe ***")
#print(estadisticasUnivDataFrame.head())

""" Filtros por columnas """

# Obtengo los datos solo de la columna Year_of_Enrollment
#print("*** Obtengo solo los datos de Year_of_Enrollment con ID ***")
#print(estadisticasUnivDataFrame["Year_of_Enrollment"])

# Obtengo los datos de las columnas Year_of_Enrollment y Age
#print("*** Obtengo solo los datos de Year_of_Enrollment y Age con ID ***")
#print(estadisticasUnivDataFrame[["Year_of_Enrollment", "Age"]])

""" Filtros por indices que tienen en las filas del csv  """

# Obtengo la cuarta fila (la del indice 3)
#print("*** Obtengo los datos de la cuarta fila ***")
#print(estadisticasUnivDataFrame.iloc[3])

# Obtengo desde la segunda hasta la sexta fila
#print("*** Obtengo los datos desde la segunda hasta la sexta fila ***")
#print(estadisticasUnivDataFrame.iloc[1:5])

# Obtengo filas elegidas
#print("*** Obtengo los datos de las filas 0, 5, 48 ***")
#print(estadisticasUnivDataFrame.iloc[[0, 5, 48]])

""" Filtros por id que tienen en las filas del csv """

# Obtengo filas elegidas por id
#print("*** Obtengo los datos de las filas STUD00016, STUD00049, STUD06638 ***")
#print(estadisticasUnivDataFrame.loc[["STUD00016", "STUD00049", "STUD06638"]])

""" Filtros por filas y columnas """

# Obtengo filas elegidas por id y quiero ver las columnas Student_ID, Country y Year_of_Enrollment
#print("*** Obtengo los datos de las filas STUD06684, STUD06729, STUD07034 filtradas por las columnas Country, Field_of_Study y Year_of_Enrollment ***")
#print(estadisticasUnivDataFrame.loc[["STUD06684", "STUD06729", "STUD07034"], ["Country", "Field_of_Study", "Year_of_Enrollment", "Age"]])

""" Filtros por condiciones """

# Quiero todas las filas donde el Year_of_Enrollment sea despues de 2015
#print("*** Obtengo los datos de las filas donde el Year_of_Enrollment sea despues de 2015 ***")
#print(estadisticasUnivDataFrame[estadisticasUnivDataFrame["Year_of_Enrollment"] > 2015])

# Quiero todas las filas donde el Year_of_Enrollment sea despues de 2015 y Field_of_Study sea Engineering
#print("*** Obtengo los datos de las filas donde el Year_of_Enrollment sea despues de 2015 y Field_of_Study sea Engineering ***")
#print(estadisticasUnivDataFrame[(estadisticasUnivDataFrame["Year_of_Enrollment"] > 2015) & (estadisticasUnivDataFrame["Field_of_Study"] == "Engineering")])

# Quiero todas las filas donde el campo Gender contenga Male
#print("*** Obtengo los datos de las filas donde el campo Gender contenga Male ***")
#print(estadisticasUnivDataFrame[estadisticasUnivDataFrame["Gender"].str.contains("Male")])

""" Agregado de nuevas columnas """

# Agrego una nueva columna al dataframe para almacenar el rango segun la edad
def obtenerEdadPorRango (edad):
    rango = 1
    if edad >= 20 and edad < 30:
        rango = 1
    elif edad >= 30 and edad < 40:
        rango = 2
    elif edad >= 40 and edad < 50:
        rango = 3
    else:
        rango = 4

    return rango

estadisticasUnivDataFrame["rango"] = estadisticasUnivDataFrame["Age"].apply(obtenerEdadPorRango)
#print("*** Muestro los datos con la nueva columna rango ***")
#print(estadisticasUnivDataFrame.head(20))

# Agrego una nueva columna para especificar si es una carrera ligada a la Salud
def estaLigadaALaSalud(fila):

    if fila["Field_of_Study"] == "Medicine" or fila["Field_of_Study"] == "Psychology":
        return "Yes"
    else:
        return "No"

# El axis especifica que la funcion se aplica para cada fila del dataframe
estadisticasUnivDataFrame["es_salud"] = estadisticasUnivDataFrame.apply(estaLigadaALaSalud, axis=1)
#print("*** Muestro los datos con la nueva columna que espedifica si es una carrera ligada a la salud ***")
#print(estadisticasUnivDataFrame.head(20))

""" Funciones de agregacion """

#Obtengo un promedio de las columnas numericas, agrupados por la columna Field_of_Study
#print("*** Obtengo un promedio de las edades, el maximo de los años y la cantidad de los roles, agrupados por Carrera ***")
estAgrupadasCarrera = estadisticasUnivDataFrame.groupby(["Field_of_Study"]).agg({
    "Age": "mean", 
    "Year_of_Enrollment": 
    "max", "rango": "count"
})
#print(estAgrupadasCarrera.head(20))

""" Graficas con matplotlib """

# Obtengo una grafica con los promedios de edades
estAgrupadasCarrera["Age"].plot(kind="bar")
#plt.show()

""" Guardo el datafram filtrado en un csv """

#estAgrupadasCarrera.to_csv("estadisticasAgrupadasDF.csv")
