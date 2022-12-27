# create a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:

   
    def __init__(self):
        self.head=None
        
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(self, data):
     
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head 
            self.head = newnode
    
    def pop(self):
     
        if self.isempty():
            return None
 
        else:
            deletenode = self.head 
            self.head = self.head.next
            deletenode.next = None
            return deletenode.data
        
    def top(self):
     
        if self.isempty():
            return None
 
        else:
            return self.head.data
        
    
    def display(self):
     
        x = self.head 
        if self.isempty():
            print("Stack Underflow")
 
        else:
 
            while(x != None):
 
                print(x.data, "->", end=" ")
                x = x.next
            print()
            return
        

MyStack = Stack()
x = int(input("Enter the number of ops: "))
line= [] 


while(x>0):
    line = (input()).split()
    if(line[0]=="push"):
        MyStack.push(line[1])
        MyStack.display()
    elif(line[0]=="pop"):
        print(MyStack.pop())
    elif(line[0]=="top"):
       print(MyStack.top())
      
        
    x=x-1