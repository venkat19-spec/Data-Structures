class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Queue:
 
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
 
    def EnQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
 
    def DeQueue(self):
 
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None

        return temp.data

    def display(self):
     
        x = self.front
        if self.isEmpty():
            print("Queue Underflow")
 
        else:
 
            while(x != None):
 
                print(x.data, "->", end=" ")
                x = x.next
            print()
            return
    
    def FrontElement(self):

        if self.isEmpty():
            return None
 
        else:
            return self.front.data

    def RearElement(self):

        if self.isEmpty():
            return None
 
        else:
            return self.rear.data

MyQueue = Queue()
x = int(input("Enter the number of ops: "))
line= [] 


while(x>0):
    
    line = (input()).split()

    if(line[0]=="enqueue"):
        MyQueue.EnQueue(line[1])
        MyQueue.display()
    elif(line[0]=="dequeue"):
        print(MyQueue.DeQueue())
    elif(line[0]=="front"):
       print(MyQueue.FrontElement())
    elif(line[0]=="rear"):
       print(MyQueue.RearElement())
      
        
    x=x-1
