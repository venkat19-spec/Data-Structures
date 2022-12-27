class Node:

    def __init__(self,data):

        self.data = data
        self.value= None
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):

        return self.data


class Conversion:
 
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
 
    def isEmpty(self):
        return True if self.top == -1 else False
 
    def peek(self):
        return self.array[-1]
 
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def isOperand(self, ch):
        return ch.isalpha()
 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    def infixToPostfix(self, exp):
 
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
 
            elif i == '(':
                self.push(i)
 
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        return self.output
 
class Tree:

    def __init__(self):

        self.root = None
        self.stack = []

    def ConstructTree(self, expr):

        for i in expr:

            if i.isalpha():

                newnode = Node(i)
                self.stack.append(newnode)

            elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':

                a = self.stack.pop()
                b = self.stack.pop()
                
                opnode = Node(i)
                opnode.left = b
                opnode.right = a
                b.parent = opnode
                a.parent = opnode
                self.stack.append(opnode)
                

        node = self.stack.pop()
        
        return node

        
    def postordertraversal(self,root):
    
        if root is None:
            return
        self.postordertraversal(root.left)
        self.postordertraversal(root.right)
        print(root.data,end=" ")

    def preordertraversal(self,root):

        if root is None:
            return

        print(root.data,end=" ")
        self.preordertraversal(root.left)
        self.preordertraversal(root.right)

    def readvaluesfromuser(self,root):

        if root.left is None and root.right is None:
            print("Enter the value for",root.data," :")
            root.value = int(input())

        else:
            self.readvaluesfromuser(root.left)
            self.readvaluesfromuser(root.right)      
            

    def EvaluateTree(self,root):

        if root is None:
            return

        else:

            lvalue = self.EvaluateTree(root.left)
            rvalue = self.EvaluateTree(root.right)

            if root.data == '+':
                root.value = lvalue+rvalue
            elif root.data == '-':
                root.value = lvalue-rvalue
            elif root.data == '*':
                root.value = lvalue*rvalue
            elif root.data == '/':
                root.value = lvalue/rvalue

        return root.value

    def MergeExpressionTrees(self,root1,root2,op):

        newnode = Node(op)
        newnode.left = root1
        newnode.right = root2
        

        if newnode.data == '+':
            newnode.value = root1.value + root2.value

        elif newnode.data == '-':
            newnode.value = root1.value - root2.value

        elif newnode.data == '*':
            newnode.value = root1.value * root2.value

        elif newnode.data == '/':
            newnode.value = root1.value / root2.value

        return newnode.value


tree = Tree()

ch = 'y'

while ch == 'y':

    print()
    print("*******************************")
    print("1. Convert Infix to Postfix")
    print("2. Construct Tree from Postfix")
    print("3. Read values of Tree")
    print("4. Evaluate Expression")
    print("5. Merge Expression Trees")
    print("*******************************")
    print()

    print("Enter your choice: ")
    op = int(input())

    if op == 1:

        exp = input("Infix Expression: ")
        obj = Conversion(len(exp))
        ans = obj.infixToPostfix(exp)
        print("Postfix Expression: ",ans)
    
    if op == 2:
        node = tree.ConstructTree(ans)
        print("Post order traversal: ")
        tree.postordertraversal(node)
        print()
        print("Pre order traversal: ")
        tree.preordertraversal(node)
        print()

    if op == 3:

        tree.readvaluesfromuser(node)
        print("Values have been read succesfully")

    if op == 4:

        print("Value of Expression Tree: ")
        value = tree.EvaluateTree(node)
        print(value)

    if op == 5:

        # ENTER EXPRESSION 1 
        exp1 = input("Enter Infix Expression 1: ")
        # CREATE AN OBJECT 
        ob1 = Conversion(len(exp1))
        # CONVERT INFIX TO POSTFIX EXPRESSION
        ans = ob1.infixToPostfix(exp1)
        # CONSTRUCT LEFT TREE FROM POSTFIX EXPRESSION
        root1 = tree.ConstructTree(ans)

        # READ VALUES FROM USER FOR NODES
        tree.readvaluesfromuser(root1)
        print("Values have been read succesfully")
        # EVALUATE LEFT TREE AND STORE ANSWER 
        leftreeans = tree.EvaluateTree(root1)

        #######################################

        # ENTER EXPRESSION 2
        exp2 = input("Enter Infix Expression 2: ")
        # CREATE AN OBJECT 
        ob2 = Conversion(len(exp2))
        # CONVERT INFIX TO POSTFIX EXPRESSION
        ans = ob2.infixToPostfix(exp2)
        # CONSTRUCT RIGHT TREE FROM POSTFIX EXPRESSION
        root2 = tree.ConstructTree(ans)

        # READ VALUES FROM USER FOR NODES
        tree.readvaluesfromuser(root2)
        print("Values have been read succesfully")
        # EVALUATE RIGHT TREE AND STORE ANSWER 
        rightreeans = tree.EvaluateTree(root2)

        ########################################


        #ENTER THE OPERATION BY WHICH YOU WANT TO MERGE
        print("Enter the operation by which you want to merge: ")
        val = input()
        value = tree.MergeExpressionTrees(root1,root2,val)

        print("Value of merged expression tree: ", value)


    print("Do you want to continue y/n")
    ch = input()