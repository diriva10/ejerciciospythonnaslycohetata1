estimularAlumnos=float(input("Escriba la cantidad de alumnos:"))#imprime y pide que escriba la cantidad de alumnos 

if estimularAlumnos>=9: #Identifica si es mayor o igual la cantidad de alumnos
    descuento=estimularAlumnos*0.3#se calcula por medio de multiplicación la cantidad de alumnos y descuento 
    print(descuento)#se imprime el resultado
else:
   estimularAlumnos<9#Identifica si es menor la cantidad de alumnos 
   pagar=estimularAlumnos*0.1#Se calcula por medio de multiplicación la cantidad de alumnos y descuento 
   print(pagar)#se imprime el resultado   
