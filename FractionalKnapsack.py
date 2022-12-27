class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity,array):

    array.sort(key=lambda x: (x.value/x.weight), reverse=True)

    result = 0

    for item in array:

        if item.weight <= capacity:

            capacity -= item.weight
            result += item.value

        else:

            result += item.value * capacity/item.weight
            break

    return result

arr = []
print("*******************")
print("Fractional Knapsack")
print("*******************")
print()

cap = int(input("Enter the capacity: "))
item_no = int(input("Enter the number of items: "))

for i in range(item_no):
    print("Enter the value for item ",i+1)
    val = int(input())
    print("Enter the weight for item ",i+1)
    wt = int(input())
    item = Item(val,wt)
    arr.append(item)

result = fractional_knapsack(cap,arr)

print("Max value: ",result)