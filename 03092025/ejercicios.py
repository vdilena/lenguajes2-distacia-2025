import random

""" La universidad necesita analizar los resultados de los dos parciales para 30 estudiantes. Las notas (números enteros de 0 a 10) están almacenados en dos listas.
El sistema debe realizar lo siguiente:
Carga inicial de datos
Crear dos listas con las 30 calificaciones generadas aleatoriamente.
Mostrar las notas en pantalla. """

listaPrimerParcial = []
listaSegundoParcial = []

for _ in range(30):
    listaPrimerParcial.append(random.randint(1,10))
    listaSegundoParcial.append(random.randint(1,10))

print(f"Notas primer parcial: {listaPrimerParcial}")
print(f"Notas segundo parcial: {listaSegundoParcial}")

""" Análisis básico con condicionales
    Calcular y mostrar cuántos estudiantes aprobaron (nota ≥ 7) y cuántos desaprobaron (<4) en ambos parciales.
    Identificar si al menos la mitad de la clase aprobó o no en cada parcial. """

# Calcular y mostrar cuántos estudiantes aprobaron (nota ≥ 7) y cuántos desaprobaron (<4) en ambos parciales.
cantidadAlumnosAprobadosMayorIgualSietePP = 0
cantidadAlumnosDesaprobadosPP = 0
cantidadAlumnosAprobadosMayorIgualSieteSP = 0
cantidadAlumnosDesaprobadosSP = 0

# Forma 1
#sumaNotas = sum(nota >= 7 for nota in listaPrimerParcial)
#print(sumaNotas)

# Forma 2
for incrementador in range(len(listaPrimerParcial)):

    notaPrimerParcial = listaPrimerParcial[incrementador]
    notaSegundoParcial = listaSegundoParcial[incrementador]

    if(notaPrimerParcial >= 7):
        cantidadAlumnosAprobadosMayorIgualSietePP += 1
    
    if(notaSegundoParcial >= 7):
        cantidadAlumnosAprobadosMayorIgualSieteSP += 1

    if(notaPrimerParcial < 4):
        cantidadAlumnosDesaprobadosPP += 1
    
    if(notaSegundoParcial < 4):
        cantidadAlumnosDesaprobadosSP += 1

print(f"# aprobados con 7 o mas en primer parcial: {cantidadAlumnosAprobadosMayorIgualSietePP}, # desaprobados primer parcial: {cantidadAlumnosDesaprobadosPP}, # aprobados con 7 o mas en segundo parcial: {cantidadAlumnosDesaprobadosPP}, # desaprobados segundo parcial: {cantidadAlumnosDesaprobadosSP}")

# Identificar si al menos la mitad de la clase aprobó o no en cada parcial.
cantApPrimerParcial = 0
cantApSegundoParcial = 0
for incrementador in range(len(listaPrimerParcial)):

    notaPrimerParcial = listaPrimerParcial[incrementador]
    notaSegundoParcial = listaSegundoParcial[incrementador]

    if(notaPrimerParcial >= 4):
        cantApPrimerParcial +=1
    
    if(notaSegundoParcial >=4):
        cantApSegundoParcial +=1

aproboAlMenosMitadCursoPP = cantApPrimerParcial >= (len(listaPrimerParcial)/2)
aproboAlMenosMitadCursoSP = cantApSegundoParcial >= (len(listaSegundoParcial)/2)
print(f"Aprobo la mitad del curso primer parcial: {aproboAlMenosMitadCursoPP}, Aprobo la mitad del curso segundo parcial: {aproboAlMenosMitadCursoSP}")

""" Estadísticas con colecciones
        Registrar la cantidad de estudiantes por cada nota (ejemplo: {10: 2, 9: 4, 8: 6…}). para el primer parcial"""

cantAlumnosPorNota = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

for nota in listaPrimerParcial:
    cantAlumnosPorNota[nota] += 1

print(f"Cantidad de calificaciones de alumnos por nota {cantAlumnosPorNota}")





