# Carga y visualización
#     Almacenar en una matriz las ventas de las sucursales que existen dentro del csv, donde cada fila tiene los datos de cada sucursal y tienen la siguiente información:
#         Código
#         Dirección
#         Cantidad de empleados
#         Lista de ventas por mes (hay una columna por cada mes)
#     Mostrar las ventas mensuales y toda la información de cada sucursal.


import csv
from functools import reduce

matrizSucursales = []  # lista de listas (cada sublista = 12 meses de una sucursal)

def cargarMatrizSucursales():

    matriz = []

    with open("ventas_sucursales.csv") as archivo:
        matriz = list(csv.reader(archivo, delimiter=','))

    #print(matrizSucursales)

    # Formateo las ventas en float
    cabecera = list(matriz[0])
    for numeroFila in range(1, len(matriz)):

        numeroColumna = 0
        for item in matriz[numeroFila]:

            # Casteo el valor de la venta mensual a float
            if (numeroColumna > 2):
                matriz[numeroFila][numeroColumna] = float(item)

            # Muestro las ventas con la dirección de la sucursal correspondiente y su cantidad de empleados.
            #print(f"{cabecera[numeroColumna]}: {item}")
            numeroColumna += 1

        #print("************************************")

    return matriz

matrizSucursales  = cargarMatrizSucursales()

# Implementar funciones para calcular por una sucursal elegida por código:
#     Promedio de ventas.
#     Máxima y mínima venta.

def sucursalPorCodigo(codigoSucursal):

    sucursalEncontrada = None
    for sucursal in matrizSucursales[1:]:
        if(sucursal[0] == codigoSucursal):
            sucursalEncontrada = sucursal
            break

    return sucursalEncontrada

def mostrarPromedioVentasDeSucursal(sucursal):

    sumatoriaVentas = sum(venta for venta in sucursal[3:]) # Sumo a partir de la columna 3
    return sumatoriaVentas/12

def mostrarMaximaVenta(sucursal):
    maximoVentas = max(venta for venta in sucursal[3:])
    return maximoVentas

def mostrarMinimoVenta(sucursal):
    minimoVentas = min(venta for venta in sucursal[3:])
    return minimoVentas

codigoSucursalPedida = input("Ingresar el codigo de la sucursal:")
sucursarElegida = sucursalPorCodigo(codigoSucursalPedida)
#print(f"Promedio de ventas $: {mostrarPromedioVentasDeSucursal(sucursarElegida)}")
#print(f"Maxima venta $: {mostrarMaximaVenta(sucursalPorCodigo(codigoSucursalPedida))}")
#print(f"Minima venta $: {mostrarMinimoVenta(sucursalPorCodigo(codigoSucursalPedida))}")

# Clasificación
#     Clasificar las ventas anuales de cada sucursal como:
#         “Excelente” (≥ 190.000.000 pesos).
#         “Aceptable” (≥ 140.000.000 y < 190.000.000).
#         “Baja” (< 140.000.000).
#     Guardar los resultados en una estructura que permita almacenar la lista de sucursales por categoría.

def obtenerSucursalesDeVentasExcelentes():

    #sucursalesExcVentas = list(sucursal for sucursal in  matrizSucursales[1:] if(sum(sucursal[3:]) > 190000000)) # Devuelvo por list comprehension

    sucursalesExcVentas = []
    for sucursal in matrizSucursales[1:]:
        if(sum(sucursal[3:]) >= 190000000):
            sucursalesExcVentas.append(sucursal)
    return sucursalesExcVentas

def obtenerSucursalesDeVentasAceptables():

    sucursalesExcVentas = list(sucursal for sucursal in  matrizSucursales[1:] if( sum(sucursal[3:]) >= 140000000 and sum(sucursal[3:]) < 190000000)) # Devuelvo por list comprehension
    return sucursalesExcVentas

def obtenerSucursalesDeVentasBajas():

    sucursalesExcVentas = list(sucursal for sucursal in  matrizSucursales[1:] if(sum(sucursal[3:]) < 140000000)) # Devuelvo por list comprehension
    return sucursalesExcVentas

ventasExcelentes = obtenerSucursalesDeVentasExcelentes()
#print(f"Sucursales con ventas excelentes: {ventasExcelentes}")
ventasAceptables = obtenerSucursalesDeVentasAceptables()
#print(f"Sucursales con ventas aceptables: {ventasAceptables}")
ventasBajas = obtenerSucursalesDeVentasBajas()
#print(f"Sucursales con ventas bajas: {ventasBajas}")

sucursalesPorCategoria = dict({"excelentes": ventasExcelentes, "aceptables": ventasAceptables, "bajas": ventasBajas})
#print(f"Ventas por categoria: {sucursalesPorCategoria}")

# Convertir todas las ventas de pesos a dólares usando un tipo de cambio fijo.
# Obtener las sucursales con ventas anuales superiores a un umbral definido por el usuario. (Y como podrias cambiar la funcion para que se reciba en dolares el importe???)
# Calcular el total acumulado de ventas por sucursal, pidiendo la sucursal a la cual se quiere obtener el dato del acumulado de ventas.

def matrizSucursalesConValoresEnDolares():

    conversor = lambda importeEnPesos : importeEnPesos/1380
    matrizTransformada = []
    for sucursal in matrizSucursales[1:]:

        sucursalTransformadaADolares = list(map(conversor, sucursal[3:]))
        matrizTransformada.append(sucursalTransformadaADolares)

    return matrizTransformada

def sucursalesConVentasAnualesSuperioresA(importeEnPesos):

    #def ventaAnualMayorAImporte(sucursal):
    #    print(sucursal[3:])
    #    sumatoriaVentasSucursal = sum(sucursal[3:])
    #    return sumatoriaVentasSucursal > importeEnPesos


    ventaAnualMayorAImporte = lambda sucursal : sum(sucursal[3:]) > importeEnPesos
    return list(filter(ventaAnualMayorAImporte, matrizSucursales[1:]))

def totalAcumuladoVentasPorSucursal(sucursal):
    return reduce(lambda x,y : x + y, sucursal[3:], 0)

#print(f"Ventas en dolares de las sucursales: {matrizSucursalesConValoresEnDolares()}")
importeEnPesosAChequearVentasSuperiores = float(input("Ingrese monto a analizar: "))
print(f"Estas son las sucursales con ventas anuales superiores a {importeEnPesosAChequearVentasSuperiores}: {sucursalesConVentasAnualesSuperioresA(importeEnPesosAChequearVentasSuperiores)}")
print(f"Este es el total acumulado por ventas para la sucursal {codigoSucursalPedida}: {totalAcumuladoVentasPorSucursal(sucursarElegida)}")
