class Element:
    def __init__(self,value,priority):
        self.value  = value
        self.priority = priority

    def display(self):
        return " Value = {0} Priority = {1}".format(self.value,self.priority)

    def displayList(self):
        return [self.value,self.priority]


class Queue:
    def __init__(self,size):
        self.size = size
        self.pQueue = [None]* self.size
        self.start = -1
        self.end  = -1

    def isEmpty(self):
        if (self.end < 0):
            return True
        else:
            return False

    def isFull(self):
        if(self.end == self.size):
            return True
        else:
            return False

    def dequeue(self):
        if not self.isEmpty():
            t = self.pQueue[self.start]
            for i in range (0,self.end-1):
                self.pQueue[i] = self.pQueue[i+1]
            self.end = self.end -1
            return t


    def sortPriority(self):
        for i in range(0,self.end):
            for j in (0,self.end-i-1):
                if (j+1 < self.end and self.pQueue[j].priority > self.pQueue[j+1].priority):
                    temp = self.pQueue[j]
                    self.pQueue[j] = self.pQueue[j+1]
                    self.pQueue[j+1] = temp
                    break


    def enqueue(self,n):
        if not self.isFull():
            if self.start == -1 and self.end == -1:
                self.start += 1
                self.end += 1
                self.pQueue[self.end] = n
                self.end += 1
            else:
                self.pQueue[self.end] = n
                self.end += 1
            print("start = {0} end = {1}".format(self.start,self.end))
            self.sortPriority()


    def updatePriority(self,element,p):
        flag = False
        for i in range (0,self.end):
            if(self.pQueue[i].value == element):
                self.pQueue[i].priority = p
                flag = True
                self.sortPriority()
                print("Priority has been updated!!")
                break
        if not flag:
            print("The element not found in queue")

            

    def displayQueue(self):
        t = [None]*self.size
        for i in range (0,self.end):
            t.insert(i,self.pQueue[i].displayList())
        return t




#MENU DRIVEN CODE
print("Enter the size of Queue")
n = int(input())
q = Queue(n)
flag = True

while(flag):
    print("1.Enqueue\n2.Dequeue\n3.Update Priority \n4.Display\n5.Exit")
    k = int(input())

    if k == 1:

        print("Enter the value: ")
        value = int(input())
        print("Enter the priority:")
        priority = int(input())
        e = Element(value,priority)
        q.enqueue(e)

    elif k == 2:

        print(q.dequeue().display())

    elif k == 3:

        print("Enter the element for which priority is to be changed")
        element = int(input())
        print("Enter the priority")
        p = int(input())
        q.updatePriority(element,p)

    elif k == 4:

        print(q.displayQueue())

    elif k == 5:

        flag = False

    else:
        
        print("Invalid Entry")

