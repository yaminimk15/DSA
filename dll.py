class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prv=None
class dll:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            newnode.prev=self.temp
            self.temp=newnode
    def insert_at_front(self,data):
        newnode=node(data)
        self.head.prv=newnode
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
    def insert_at_middle(self,data,pos):
        newnode=node(data)
        self.temp=self.head
        i=1
        while(i<pos-1):
            self.temp=self.temp.next
            i=i+1
        newnode.prev=self.temp
        newnode.next=self.temp.next
        self.temp.next= newnode
        newnode.next.prv=newnode
    def del_at_front(self):
        self.head=self.head.next
        self.head.prev=None
    def del_at_end(self):
        self.temp=self.head
        while self.temp.next.next is not None:
            self.temp=self.temp.next
        self.temp.next=None
    def del_at_middle(self,pos):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        self.temp.next=self.temp.next.next
        self.temp.next.prv=self.temp
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,"-----",end="")
            self.temp=self.temp.next
        print()
obj=dll()
while(True):
    print("1.create 2.display 3. insert at front 4. insert at end 5. insert at middle 6. del at front 7. del at end 8. del at middle")
    a=int(input("enter a choice: "))
    if (a==1):
        n=int(input("enter number of  node to create"))
        for i in range(n):
            data =int(input("enter a data: "))
            obj.create(data)
    elif (a==2):
        obj.display()
    elif(a==3):
        data=int(input("enter a data: "))
        obj.insert_at_front(data)
    elif (a==4):
        data=int(input("enter a data"))
        obj.insert_at_end(data)
    elif (a==5):
        data=int(input("Enter a data"))
        pos=int(input("enter a position"))
        obj.insert_at_middle(data, pos)
    elif (a==6):
        obj.del_at_front()
    elif(a==7):
        obj.del_at_end()
    elif(a==8):
        pos=int(input("enter a position"))
        obj.del_at_middle(pos)
