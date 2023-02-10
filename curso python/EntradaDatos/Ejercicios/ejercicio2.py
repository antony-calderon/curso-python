'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

p1 = float(input("Ingrese la nota de practica uno: "))
p2 = float(input("Ingrese la nota de practica dos: "))
p3 = float(input("Ingrese la nota de practica tres: "))

ep = float(input("Ingrese la nota del examen parcial: "))
ef = float(input("Ingrese la nota del examen final: "))

pp = (p1 + p2 + p3)/3
print(pp)

prom = (pp + (2*ep) + (3*ef))/6

print("La nota promedio del estudiante durante el curso es de: " + str(prom))
