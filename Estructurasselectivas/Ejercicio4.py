from random import *
#Pide que escriba el numero 
valorComprar=int(input("Digite el numero de la compra de la balota"))
#describe cuales son las balotas por medio del color
balota=(choice(["rojo","verde","diferente"]))
#se describe cual va hacer el descuento
descuento=0#se identifica para el resultado cero

if balota=="rojo":#el color de balota 
    descuento=15#Descuento de balota roja
elif balota=="verde":#el color de valota
    descuento=20#Descuento de balota verde
else:
    balota=="diferente"#Si es diferente no se identifica
    descuento==0#Se identifico para el resultado

#se hace el calculo del valor balota con el descuento
valorPagar=valorComprar-((valorComprar*descuento)/100)
#imprime lo que el usuario quiere ver el resultado
print("El balor de la compra es un total de",valorComprar,"el color de la balota es",balota,"el descuento es",descuento,"y valor a pagar es",valorPagar)

        

