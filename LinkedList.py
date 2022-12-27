from re import I

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
        self.last = None
        self.count = 0

    def isEmpty(self):

        if self.head == None:
            return True
        else:
            return False


    def addelement(self,data):

        if self.head == None:
            self.head = Node(data)
            self.last = Node(data)
            self.count += 1
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            self.count += 1

    def lastelement(self):

        if self.last is not None:

            return self.last.data


    def deletelement(self):

        prenode = self.head
        curnode = self.head.next
        postnode = curnode.next

        i=0

        while i < self.count:
            prenode.next = postnode
            if postnode == None:
                prenode.next = None
                self.last = prenode
                break
            elif postnode.next == None:
                break
            else:
                prenode=postnode
                curnode=prenode.next
                postnode=curnode.next
            i+=2
        self.count = self.count // 2 + self.count % 2


            

    def size(self):
        return self.count

    def display(self):
     
        x = self.head 
        if self.isEmpty():
            return
 
        else:
            while(x != None):
                print(x.data,end="->")
                x = x.next
            print("null")
            return

MyLinkedList = LinkedList()
x = int(input("Enter the number of ops: "))
line= [] 


while(x > 0):
    line = (input()).split()

    if(line[0]=="EF"):
        MyLinkedList.addelement(line[1])
        MyLinkedList.display()

    elif(line[0]=="size"):
        print(MyLinkedList.size())

    elif(line[0]=="RE"):
        MyLinkedList.deletelement()
        MyLinkedList.display()

    elif(line[0]=="LE"):
        print(MyLinkedList.lastelement())
        
    x=x-1