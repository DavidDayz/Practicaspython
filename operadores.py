# operadores nos dicen que hacer 
# operadores aritmeticos 
from re import X


print(3 + 4)#suma
print(5 - 2)#resta
print(5 * 5)#multiplicacion
print(6 / 2)#divicion
print(11 % 4)# modulo = nos dice el sobrante de una division 
print(11 // 4)#divicon de piso = nos indica la mayor de veces que entra un numero en una divison
print(2 ** 3)#potensacion = se ulizan dos astericos para elebar al cubo 

#operadores en cadenas de texto 

print("hola" + "mundo")#cocatenacion
print("hola" * 3)# repeticion 
print("hola" + "mundo" * 3)

#operadores de comparacion = dejan verificar si es igual a otro 
print("hola" == "Hola")#igual que 
print("hola" != "Hola")#distinto que
print(3 > 11)#mayor que o menor que 
print(11 >= 10)#mayor o igaul que 
print(10 <= 10)#menor o igual que 


#operadores de existencia
print("ola" in "hola")#de existencia
print("ola" not in "hola")# de inexitencia

#operadores booleanos 
print(True or False) # verifica que se cumplan solo una de las condiciones
print(True and False)# verifica que solo se cumpla las dos condiciones

#operadores de asignacion 
x = 1#operador de asignacion estadandar
x += 2# operador de asignacion suma
x *= 3# operador de asignacion multiplicasion
x %= 4#operador de asignacion modulo 
print(x)

# en progamacion es igaul que en matematicas hay jerarquia 
x = 5 + 2 * 3 / 3 ** 5
print(x)



