actividadesEquivalen=0.3#Da el valor definido
proyectoFinal=0.5#Da el valor definido
evaluacionesParciales=0.2#Da el valor definido

nombreDelEstudiante=(input("Escriba tu  nombre:"))#Pide que escriba el nombre del estudiante
print("Digite el promedio de las actividades realizadas en clase")#pide que escriba el promedio de las actividades realizadas en clase muestra en pantalla 
numero1=float(input("Digite el primer promedio:"))#pide que escribe el promedio1
numero2=float(input("Digite el segundo promedio:"))#pide que escriba el promedio2
numero3=float(input("Digite el tercer promedio:"))#pide que escriba el promedio3

notaActividades=((numero1+numero2+numero3)/3*0.3)#calcula los promedios de actividades 

print("Escriba la calificación del proyecto")#pide que escriba el promedio o calificaciòn de los proyectos 
number1=float(input("Escriba el promedio del proyecto:"))#escribe la calificación del proyecto
proyecto=((number1)/1*0.5)#Resultado de calculo

print("Escriba las calificaciones dadas en las evaluaciones")#pide que escriba las notas 
numb1=float(input("Escriba el promedio de la evaluaciòn"))#pide que escriba las 1nota
numb2=float(input("Escriba el segundo promedio de la evaluaciòn"))#pide que escriba la 2nota
Evaluaciones=((numb1+numb2)/2*0.2)#Resultado de calculo

Totalasacar=(notaActividades+proyecto+Evaluaciones)#se suman el calculo 



print("La nota final del algoritmia del estudiante", nombreDelEstudiante,"es",Totalasacar)#se imprime todo los resultado y lo que se pidio