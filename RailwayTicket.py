

class reserved:
    def __init__(self):
        self.size = 3
        self.res = [None]*self.size
        self.start = -1
        self.end = -1

    def is_full(self):
        if self.end == self.size-1:
            return True
        else:
            return False

    def reserve_ticket(self,id, name, address):
        data = [id,name,address]
        if self.is_full():
            return False
        elif self.start == -1:
            self.start = self.end = 0
        else:
            self.end+=1
        self.res[self.end] = data
        return True

    def cancel_ticket(self, id):
        i=0
        if self.start == -1:
            return False
        while(i<=self.end):
            if self.res[i][0] == id:
                break
            i+=1
        if i>self.end:
            return False
        self.res.pop(i)
        self.res.append(None)
        self.end-=1
        if self.end ==-1:
            self.start =-1
        return True

    def print_reserved(self):
        print("Reserved queue: ", self.res)

class waiting:
    def __init__(self):
        self.size = 3
        self.res = [None]*self.size
        self.start = -1
        self.end = -1

    def is_full(self):
        if self.end == self.size-1:
            return True
        else:
            return False

    def add_to_waiting(self,id, name, address):
        data = [id,name,address]
        if self.is_full():
            return False
        elif self.start == -1:
            self.start = self.end = 0
        else:
            self.end+=1
        self.res[self.end] = data
        print("Added to waiting list.")
        return True


    def dequeue(self):
        if self.start == -1:
            print("Waiting list is empty.")
            return None
        else:
            temp = self.res[self.start]
            self.res[self.start] = None
            self.start += 1
            return temp


    def cancel_ticket(self, id):
        i=0
        if self.start == -1:
            return False
        while(i<=self.end):
            if self.res[i][0] == id:
                break
            i+=1
        if i>self.end:
            return False
        self.res.pop(i)
        self.res.append(None)
        self.end-=1
        if self.end ==-1:
            self.start =-1
        return True

    def print_wait(self):
        print("Waiting queue: ", self.res)

tickets = reserved()
waitlist = waiting()
check = 'y'

while(check == 'y'):
    print("1. Book ticket.")
    print("2. Cancel ticket.")
    print("3. Exit App")
    x = input("Enter choice : ")
    if x=='1':
        id = input("Enter id : ")
        name = input("Enter Name : ")
        address = input("Enter address : ")
        if not(tickets.reserve_ticket(id, name, address)):
            waitlist.add_to_waiting(id,name,address)
        else: 
            print("Ticket reserved")
    elif x=='2':
        id = input("Enter id number to cancel : ")
        if tickets.cancel_ticket(id):
            temp = waitlist.dequeue()
            if temp:
                tickets.reserve_ticket(temp[0],temp[1],temp[2])
            print("Ticket cancelled")
        else:
            if not(waitlist.cancel_ticket(id)):
                print("Nothing to cancel.")
            else:
                print("Ticket cancelled from wait list. You will get your refund shortly.")
    else:
        print("Thank you for using our services.")
        break
    check = input("Do you wish to book/ cancel another ticket? (y/n) :")
    if(check != 'y'):
        print("Thank you. Please visit again.")
    tickets.print_reserved()
    waitlist.print_wait()
    print()