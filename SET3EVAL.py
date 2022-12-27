class Element:
    def __init__(self,value,waitingtime):
        self.value  = value
        self.waitingtime = waitingtime

    def display(self):
        return " Value = {0} Waiting Time = {1}".format(self.value,self.waitingtime)

    def displayList(self):
        return [self.value,self.waitingtime]

class Queue:

    #QUESTION 1
    def __init__(self):
        self.stack1 = []
        self.sum = 0
        
    def enqueue(self,data):
        self.stack1.append(data)

    def dequeue(self):

        if len(self.stack1) == 0:
            print("Stack Empty")

        if len(self.stack1) == 1:
            return self.stack1.pop()

        data = self.stack1.pop()
        retVal = self.dequeue()
        self.stack1.append(data)
        return retVal

    def printqueue(self):
        print("Queue: ",self.stack1)


    #QUESTION 3
    def modified_dequeue(self,element):
        sum = 0

        if len(self.stack1) == 0:
            print("Stack Empty")

        while self.stack1.pop() != element.value:

            data = self.stack1.pop()
            sum += data.waitingtime
            self.stack1.append(data)

        data = self.stack1.pop()
        sum += data.waitingtime
        self.stack1.append(data)

        avgtime = sum/len(self.stack1)

        return avgtime

queue = Queue()


x = int(input("Enter the number of ops for Q1: "))
line=[] 


while x>0:
    line = input().split()
    if(line[0]=="enqueue"):
        queue.enqueue(line[1])
        queue.printqueue()
    elif(line[0]=="dequeue"):
        print(queue.dequeue())
        queue.printqueue()
        
    x=x-1


queue1 = Queue()
flag = True

while(flag):
    print("1.Enqueue\n2.Calculate average waiting time\n3.Exit")
    k = int(input())

    if k == 1:

        print("Enter the value: ")
        value = int(input())
        print("Enter the avg waiting time:")
        waitingtime = int(input())
        e = Element(value,waitingtime)
        queue1.enqueue(e)
        queue1.printqueue()
        print(len(queue1.stack1))

    elif k == 2:

        print("Enter element for which avg waiting time has to be calculated: ")
        val = int(input())
        print("Enter the avg waiting time:")
        waitingtime  = int(input())
        e = Element(value,waitingtime)
        avgtime = queue1.modified_dequeue(e)
        queue1.modified_dequeue(e).displayList()
        print("Average time for element: ", avgtime)
        

    elif k == 3:

        flag = False

    else:
        
        print("Invalid Entry")
        
        