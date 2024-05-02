#pide que escriba los numeros
primeraCalificacion=int(input("Escriba tu primera calificación:"))
segundaCalificacion=int(input("Escriba tu segunda calificación"))
terceraCalificacion=int(input("Escriba tu tercera calificación"))
#suma los numeros y divide en 3
Calificacion=(primeraCalificacion+segundaCalificacion+terceraCalificacion)/3
#califica el resultado si aprueba o sino
if Calificacion>=70:
    print("Aprobado")
else:
    print("Desaprobado")

