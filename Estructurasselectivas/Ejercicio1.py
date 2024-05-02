#pide que escriba los numeros
primeraCalificacion=int(input("Escriba tu primera calificación:"))#imprime pero pide un numero entero
segundaCalificacion=int(input("Escriba tu segunda calificación"))#imprime pero pide un numero entero
terceraCalificacion=int(input("Escriba tu tercera calificación"))#imprime pero pide un numero entero
#suma los numeros y divide en 3
Calificacion=(primeraCalificacion+segundaCalificacion+terceraCalificacion)/3
#califica el resultado si aprueba o sino
if Calificacion>=70:#Identifica el numero s es mayo o igual
    print("Aprobado")#imprime si es aprobado
else:#si no
    print("Desaprobado")#imprime si es desaprobado

