class WebHistory:

    def __init__(self,size):

        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def isFull(self):

        return self.top == self.size - 1

    def isEmpty(self):
        
        return self.top < 0

    def addURL(self, url):

        if self.isFull():
            print("Stack Full")
            return
        self.top += 1
        self.stack[self.top] = url

    def loadRececntURL(self):

        return self.stack[self.top]

    def deleteNRecent(self, n):
        if n > self.size:
            print("N value greater than size")

        elif n <= 0:
            print("N value too small!!")

        else:
            while n > 0:
                if not self.isEmpty():
                    self.stack[self.top] = None
                    self.top -= 1
                n -= 1

    def sizeofHistory(self):
        return self.top+1
    
    def printStack(self):

        for i in range(len(self.stack)):
            print(self.stack[i])

            
s = WebHistory(5)

print()
s.addURL("https://w3schools.com")
s.addURL("https://geeks4geeks.com")
s.addURL("https://stackoverflow.com")
s.addURL("https://overleaf.com")

print("Recent URL: ",s.loadRececntURL())
s.printStack()
print()

s.addURL("https://takeUforward.com")
s.addURL("https://godaddy.com")
s.printStack()

print("Recent URL: ",s.loadRececntURL())
print()
s.deleteNRecent(6)
print()
s.printStack()
print()
print("Stack Size:",s.sizeofHistory())

s.addURL("https://godaddy.com")
print()
s.printStack()
print("Stack Size: ",s.sizeofHistory())

