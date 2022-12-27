import time

def function(x):

    if x == 0:
        return 0
    else:
        return pow(x , 2) + (54 / x)

def fibonacci(n):
     
    if n <= 1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

result = []
t = []
computations = []

def FibonacciSearch(lowerbound,upperbound,n):
    
    k = 2

    L = upperbound - lowerbound

    while k <= n:
        
        start = time.time()

        n_computations = 0

        fib1 = fibonacci(n-k+1)
        fib2 = fibonacci(n+1)

        n_computations += 2

        computations.append(n_computations)

        lk = (fib1 / fib2) * L

        x1 = lowerbound + lk

        x2 = upperbound - lk

        f1 = function(x1)
        f2 = function(x2)

        if f1 > f2:

            lowerbound = x1

        else:

            upperbound = x2
            
        end = time.time()

        t.append((end-start) * 10**3)

        k += 1

    result.append([lowerbound,upperbound])

    return result

print("********************")
print("Fibonacci Search  ")
print("*******************")

lwb = int(input("Lower Bound: "))
upb = int(input("Upper Bound: "))

iter = int(input("Iterations: "))

ans = FibonacciSearch(lwb,upb,iter)

if ans == 0:

    print("No minima exists in the given range!")

else:
    print("Minima Range: ",ans)

print("Minima Ranges: ",ans)
print("Convergence Time:" ,t)
print("Function computations: ",computations)


