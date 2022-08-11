# ejemplos de la funcion print ()

print("hola mundo")
print("hola mundo" , ("otra vez"))
print("son las", 9, ("de la mañana"))
print("el resultado de 3 * 4 es=", 3 * 4)

# ejemplos de cadenas formateadas 
print("el nuemro 15 en el sistama decimal es %d, el numero 15 en el sistama octal es %o, el numero 15 en el sistema hexadecimal es %x" % (15, 15, 15))

pi = 3.141592
r = 5
print(f"el radio de un circulo es {r} y el area de ese circulo es {pi * r ** 2 : .2f}")

#impresion de caracteres especiales 
print("la letra beta es: \n\t \u03B2" )

#caracteres especiales
print("hola mundo", end = " "  )
print("otra vez", end = "\t")
print("y otra vez")

