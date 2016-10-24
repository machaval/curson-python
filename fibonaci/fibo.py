#Fibonaci
#fib(n) = fib(n -1) + fib(n-2)
def fib(n):
    if(n <= 0):
        return "Numero invalido " + str(n);
    elif(n <= 2):
        return 1;
    else:
        return fib(n-1) + fib(n-2);

#Pregunta al usuario 
fibOf = input("Fibonaci de que numero quiere calcular?")

print(fib(int(fibOf)))
