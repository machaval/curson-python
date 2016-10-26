# 
#Chequea si un numero es primo o no 
#Devuelve True si es primo sino devuelve False    
def primeNumber(n):
    #Por definicion de primo
    if(n == 0 or n == 1 or n < 0):
        return False
    elif(n == 2):
        return True
    else:
        #Checkeo para que sea primo me alcansa con probar 
        #1 que no sea par
        #2 que no sea divisible por ninguno de sus anteriores numero impares ya que si es divisible por un numero par es divisible por 2 por definicion
        return not(isEven(n)) and checkPrime(n, n - 2)
        
#Metodo auxiliar que chequea si un numero es divisible por m o alguno de sus numeros anteriores
def checkPrime(n, m): 
    if(m <= 2):
        return True
    elif(n % m == 0):
        return False
    else:
        return checkPrime(n,m-2)
        
#Checkea si un numero es par o no
#Devuelve True si es par sino False        
def isEven(n):
    return (n % 2) == 0
    


numberToTest = int(input("Decime el numero?"))
print("Es primo: " + str( primeNumber(numberToTest) ) )
