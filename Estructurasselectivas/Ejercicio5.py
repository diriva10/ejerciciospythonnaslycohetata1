genero=(input("Escriba el genero que perteneces, masculino o femenino:"))#Imprime y pide que escriba el genero 
edad=int(input("Escriba tu edad:"))#imprime y pide que escriba la edad 
pulsaciones=int(input("Escriba la cantidad de pulsaciones por cada 10s:"))#pide cantidad de pulsaciones

if genero=="femenino":#genero que es asi se especifica para calcular
   number=(220-edad)/10 #se calcula
elif genero=="masculino":
   number=(210-edad)/10#se calcula
else:
   print("Pr favor, introduce un sexo valido:(masculino/femenino)")

#imprimir el resultado
print("el numero de pulsaciones que debes tener por cada 10 segundos de ejercicios aeróbico es:",number)


