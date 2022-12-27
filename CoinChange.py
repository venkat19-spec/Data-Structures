import sys

coins = []

amt = int(input("Amount: "))
n = int(input("Number of coins: "))
for i in range(0,n):
    print("Denomination ",i+1,": ")
    val = int(input())
    coins.append(val)
a = amt+1
b = n+1
dparray = [[-1 for i in range(a)] for j in range(b)]

def coinchangeDP(coins, value):

    if coins is None and value > 0:
        return -1

    if value == 0:

        return 0

    for i in range(0,b):

        for j in range(0, a):

            if j == 0:

                dparray[i][j] = 0

            elif i == 0:

                dparray[i][j] = sys.maxsize

            elif coins[i-1] > j:

                dparray[i][j] = dparray[i-1][j]

            else:

                dparray[i][j] = min(1+dparray[i][j - coins[i-1]], dparray[i-1][j])


    minimum = -1 if dparray[b-1][a-1] > 1e4 else dparray[b-1][a-1]
    return minimum


result = coinchangeDP(coins,amt)
print("Min coins: ",result)
            

