nombre=(input("Escriba tu nombre"))#Pide que escriba el nombre
sueldo=int(input("Esrciba tu sueldo"))#Pide que escriba el numero de que resive sueldo
comision=int(input("Escriba el procentaje de comisión "))#Pide que escriba el porcentaje
ventas=int(input("escriba el numero de ventas"))#pide que escriba el numero de ventas
valorComision=ventas*comision;#calcula las ventas con comisión 

valorPagar=sueldo+valorComision#calcula el sueldo con valorcomisión

print("el vended@r", nombre, "tiene un sueldo de",sueldo,"y gano una comisión de", comision,"su sueldo a pagar es:", valorPagar)#imprime todos los resultados
