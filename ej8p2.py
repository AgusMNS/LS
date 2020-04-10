primos=list()
print("Ingresa una palabra para determinar si la cantidad total de veces que aparece cada letra es un número primo ")
palabra=str(input())
letras=set(palabra) #obtengo un conjunto de las letras que aparecen no repetidas
print(letras)
for x in letras:
    cant=palabra.count(x) #calculo cuantas veces aparece esa letra en la palabra
    print("La letra "+ x +" aparece: "+ str(cant) +" veces")
    if(cant!=1):  #1 es el unico nro que se divide por si mismo y 1 que no es primo, entonces lo descarto
        primo=True
        for y in range(2,10): #si es divisible por algun otro nro que si mismo y el 1 entonces no es primo
            if ((cant % y == 0) and (y != cant)):
                 primo=False
        if(primo==True):
            primos.append(x)
print("Las letras: ")
print(primos) 
print("aparecen un numero primo de veces")


