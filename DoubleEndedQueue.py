
class deque:
    def __init__(self,x):
        self.size = x
        self.res = [None]*self.size
        self.f = -1  
        self.r = -1  
        
    def isfull(self):
        if ((self.f==0 and self.r==self.size-1) or self.f==self.r+1):
            return True
        else:
            return False
    
    def isEmpty(self):
        if(self.f==-1 and self.r==-1):
            return True
        else:
            return False
        
        
    def enqueueFront(self,data):
        if (self.isfull()):
            print("queue is full")
        elif(self.f==-1 and self.r==-1):
            self.f=0
            self.r=0
            self.res[self.f] = data
            print(self.res)
        elif(self.f==0):
            self.f = self.size-1
            self.res[self.f]=data
            print(self.res)
        else:
            self.f= self.f-1
            self.res[self.f]=data
            print(self.res)
    
    
         
    def enqueueRear(self,data):
        if (self.isfull()):
            print("queue is full")
        elif(self.f==-1 and self.r==-1):
            self.f=0
            self.r=0
            self.res[self.r] = data
            print(self.res)
        elif(self.r==self.size-1):
            self.r=0
            self.res[self.r]=data
            print(self.res)
        else:
            self.r=self.r+1
            self.res[self.r]=data
            print(self.res)
            

    def display(self):
        i=self.f
        while(i!=self.r):
            print(self.res[i])
            i= (i+1)%self.size
        print(self.res[self.r])
        

    def getFront(self):
        if(self.f==-1):
            print("queue is empty")
        else:
            print("front element is :",self.res[self.f])        


    def getRear(self):
        if(self.r==-1):
            print("queue is empty")
        else:
            print("rear element is :",self.res[self.r])
    

    def delFront(self):
        if (self.isEmpty()):
            print("queue is empty")
        elif(self.f==self.r):
            print(self.res[self.f])
            self.f=-1
            self.r=-1
        elif(self.f==self.size-1):
            print(self.res[self.f])
            self.f=0
        else:
            print(self.res[self.f])
            self.f= self.f+1
            

    def delRear(self):
        if (self.isEmpty()):
            print("queue is empty")
        elif(self.f==self.r):
            print(self.res[self.r])
            self.f=-1
            self.r=-1
        elif(self.r==0):
            print(self.res[self.r])
            self.r= self.size-1;
        else:
            print(self.res[self.r])
            self.r= self.r-1
               
size = int(input())
s=deque(size)
x = int(input())
line= [] 

while(x>0):
    
    line = (input()).split()
     
    if(line[0]=="enfront"):
        s.enqueueFront(line[1])

    elif(line[0]=="enrear"):
        s.enqueueRear(line[1])

    elif(line[0]=="defront"):
        print(s.delFront())

    elif(line[0]=="derear"):
        print(s.delRear())

    elif(line[0]=="gf"):
        s.getFront()

    elif(line[0]=="gr"):
        s.getRear()
    
        
    x=x-1
