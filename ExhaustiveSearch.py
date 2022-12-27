import time

def function(x):

    if x == 0:
        return 0
    else:
        return pow(x , 2) - (5 * x) + 6

result = []
t = []
computations = []

def ExhaustiveSearch(lowerbound,upperbound,n_intermediate):

    x1 = lowerbound

    delx = (upperbound - lowerbound) / n_intermediate

    x2 = x1 + delx

    x3 = x2 + delx

    n_computations = 0

    while x3 <= upperbound:
        
        f1 = function(x1)

        f2 = function(x2)

        f3 = function(x3)

        n_computations += 3

        if f1 >= f2 and f2 <= f3:

            result.append([x1,x3])
            computations.append(n_computations)
            return result

        else:

            x1 = x2

            x2 = x3

            x3 = x2 + delx


print("********************")
print("Exhaustive Search  ")
print("*******************")


lwb = int(input("Lower Bound: "))
upb = int(input("Upper Bound: "))

start = time.time()

for i in range(1,10):

    start = time.time()
    ans = ExhaustiveSearch(lwb,upb,pow(10,i))
    end = time.time()
    t.append((end-start) * 10**3)
    
    if ans == 0:

        print("No minima exists in the given range!")
        break
    else:
        print("Minima Range: ",ans)


print("Minima Ranges: ",ans)
print("Convergence Time:" ,t)
print("Function computations: ",computations)



