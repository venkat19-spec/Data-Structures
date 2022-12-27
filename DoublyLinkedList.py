class Node:

    def __init__(self,data):

        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        
        self.head = None


    def insertfront(self,data):

        if self.head is None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def deletefront(self):

        if self.head is None:
            print("Can't delete from front!")

        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None

    def insertafter(self,prev_data,data):

        node = self.head
        flag = 0
        while node:
            if node.data == prev_data:
                flag=1
                newnode = Node(data)
                newnode.next = node.next
                newnode.prev = node
                node.next = newnode
                break
            node = node.next

        if flag == 0:
            print("Prev doesnt exist")

        if newnode.next is not None:
            newnode.next.prev = newnode

    def insertend(self,data):

        if self.head is None:
            self.head = Node(data)

        else:
            node = self.head

            while node.next is not None:
                node = node.next

            newnode = Node(data)
            node.next = newnode
            newnode.prev = node

    def deletend(self):

        if self.head is None:
            print("Cant delete from end!")

        else:
            node = self.head
            while node.next is not None:
                node = node.next
            
            node.prev.next = None
            node.prev = None


    def printList(self, node):
 
        while node:
            print(node.data ,end="->")
            last = node
            node = node.next
 

DLL = DoublyLinkedList()

x = int(input("Enter the number of ops: "))
line= [] 


while(x > 0):
    line = (input()).split()

    if(line[0]=="IF"):
        DLL.insertfront(int(line[1]))
        DLL.printList(DLL.head)

    elif(line[0]=="IA"):
        DLL.insertafter(int(line[1]), int(line[2]))
        DLL.printList(DLL.head)

    elif(line[0]=="IE"):
        DLL.insertend(int(line[1]))
        DLL.printList(DLL.head)

    elif(line[0]=="DF"):
        DLL.deletefront()
        DLL.printList(DLL.head)

    elif(line[0]=="DE"):
        DLL.deletend()
        DLL.printList(DLL.head)
    
    
    print()
    x=x-1

        

