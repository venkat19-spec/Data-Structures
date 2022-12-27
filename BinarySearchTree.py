class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    #INSERT RECURSIVELY INTO BINARY SEARCH TREE
    def InsertRecursive(self, root, data):

        if root is None:

            root = Node(data)

            return root

        else:
            
            if root.data == data:

                return root

            elif data > root.data:

                root.right = self.InsertRecursive(root.right,data)

            else:

                root.left = self.InsertRecursive(root.left,data)

        return root

    #INSERT ITERATIVELY INTO BINARY SEARCH TREE
    def InsertIterative(self, root, data):

        if root is None:

            root = Node(data)
            return root

        head = root
        prev = None

        while head is not None:

            prev = head

            if data == head.data:
                return
            if data > head.data:
                head = head.right
            else:
                head = head.left


        if data > prev.data:

            prev.right = Node(data)

        else:

            prev.left = Node(data)

        return root


    #SEARCHING FOR AN ELEMENT RECURSIVELY
    def SearchRecursive(self, root, data):

        if root is None:
            print("Node ",data," has not been found!!!")
            return False

        else:

            if data == root.data:

                print("Node ",data," has been found succesfully!!!")
                return 

            elif data > root.data:

                root.right = self.SearchRecursive(root.right,data)

            else:

                root.left = self.SearchRecursive(root.left,data)


    #SEARCHING FOR AN ELEMENT ITERATIVELY
    def SearchIterative(self, root, data):

        if root is None:

            print("Node ",data," has not been found!!!")
            return 

        else:

            while root is not None:

                if data == root.data:
                    print("Node ",data," has been found succesfully!!!")
                    return

                elif data > root.data:

                    root = root.right

                else:

                    root = root.left

    #FIND HEIGHT OF BINARY SEARCH TREE
    def FindHeight(self, root):

        if root is None:

            return 0

        leftheight = self.FindHeight(root.left)
        rightheight = self.FindHeight(root.right)

        return max(leftheight,rightheight)+1
        
    #CHECK IF TREE IS BALANCED OF NOT
    def IsBalanced(self, root):

        if root is None:

            return 0

        else:

            leftheight = self.IsBalanced(root.left)
            if leftheight == -1:
                return -1

            rightheight = self.IsBalanced(root.right)
            if rightheight == -1:
                return -1

            if abs(leftheight - rightheight) > 1:
                return -1

        return max(leftheight,rightheight)+1


    #TRAVERSAL
    def inordertraversal(self,root):
    
        if root is None:
            return

        self.inordertraversal(root.left)
        print(root.data,end="-> ")
        self.inordertraversal(root.right)


BST = BinarySearchTree()

ch='y'
root=None

while(ch=='y'):
    print()
    print("*******************************")
    print("1. Insert into BST recursively")
    print("2. Insert into BST iteratively")
    print("3. Search BST recursively")
    print("4. Search BST iteratively")
    print("5. Height of BST")
    print("6. Check if BST balanced or not")
    print("*******************************")
    print()
    print("Enter your choice: ")

    op = int(input())

    if op == 1:
        print("Enter value to be inserted: ")
        val = int(input())
        root = BST.InsertRecursive(root, val)
        print("Inorder Traversal: ",end=" ")
        BST.inordertraversal(root)
        print()

    if op == 2:
        print("Enter value to be inserted: ")
        val = int(input())
        root = BST.InsertIterative(root,val)
        BST.inordertraversal(root)
        print()

    if op == 3:
        print("Enter the element to be searched for: ")
        val = int(input())
        BST.SearchRecursive(root,val)
        print()

    if op == 4:
        print("Enter the element to be searched for: ")
        val = int(input())
        BST.SearchIterative(root,val)
        print()

    if op == 5:
        height = BST.FindHeight(root)
        print("Height of the tree : ",height)

    if op == 6:
        flag = BST.IsBalanced(root) != -1
        print(flag)

    print("Do you want to enter more y/n: ")
    ch = input()