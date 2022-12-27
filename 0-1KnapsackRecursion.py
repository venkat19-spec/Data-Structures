def knapsack(maxweight,number,value,weight):

    if number == 0 or maxweight == 0:
        return 0

    elif weight[number-1] <= maxweight:

        return max(value[number-1] + knapsack(maxweight - weight[number-1],number - 1,value,weight),knapsack(maxweight,number - 1,value,weight))

    else:

        return knapsack(maxweight, number - 1, value, weight)


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
result = knapsack(maxwt,number,value,weight)

print("Max value of knapsack: ",result)