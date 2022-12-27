class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):

        self.queue = []

    def ConstructTree(self,root,data):

        if root is None:

            root = Node(data)
            return root
        
        self.queue.append(root)

        while len(self.queue):

            temp = self.queue[0]
            self.queue.pop(0)
            print(temp.data)

            if not temp.left:
                temp.left = Node(data)
                break

            else:
                self.queue.append(temp.left)

            if not temp.right:
                temp.right = Node(data)
                break

            else:
                self.queue.append(temp.right)

        return root

    def IterativeSearch(self,root,data):

        stack = []
        stack.append(root)

        while stack:

            current = stack.pop()
            
            if data == current.data:
                print("Element ",data, "has been found successfully!")
                return

            if current.right is not None:
                stack.append(current.right)

            if current.left is not None:
                stack.append(current.left)



    def inordertraversal(self,root):
    
        if root is None:
            return

        self.inordertraversal(root.left)
        print(root.data,end="-> ")
        self.inordertraversal(root.right)


BT = BinaryTree()

ch='y'
root=None

while(ch=='y'):
    print()
    print("*******************************")
    print("1. Insert into BT recursively")
    print("2. Search Element in BT")
    print("*******************************")
    print()
    print("Enter your choice: ")

    op = int(input())

    if op == 1:
        print("Enter value to be inserted: ")
        val = int(input())
        root = BT.ConstructTree(root, val)
        print("Inorder Traversal: ",end=" ")
        BT.inordertraversal(root)
        print()

    if op == 2:
        print("Enter value to be searched: ")
        val = int(input())
        BT.IterativeSearch(root,val)
        print()

    print()
    print("Do you want to enter more y/n: ")
    ch = input()