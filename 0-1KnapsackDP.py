def knapsackDP(maxweight,number,value,weight):

    if number == 0 or maxweight == 0:
        return 0

    if dparray[number][maxweight] != -1:
        return dparray[number][maxweight]

    elif weight[number-1] <= maxweight:

        dparray[number][maxweight] = max(value[number-1] + knapsackDP(maxweight - weight[number-1],number - 1,value,weight),
                                     knapsackDP(maxweight,number - 1,value,weight))
        return dparray[number][maxweight]

    else:

        dparray[number][maxweight] = knapsackDP(maxweight, number - 1, value, weight)
        return dparray[number][maxweight]

maxwt = int(input("Enter the maxmimum weight: "))
number = int(input("Enter number of items:"))
value = []
weight = []


for i in range(number):

    print("Value for item ",i+1)
    val = int(input())
    print("Weight for item ",i+1)
    wt = int(input())
    value.append(val)
    weight.append(wt)

print(value,weight)
dparray = [[-1 for i in range(maxwt + 1)] for j in range(number + 1)]
result = knapsackDP(maxwt,number,value,weight)
print("Max value of knapsack: ",result)