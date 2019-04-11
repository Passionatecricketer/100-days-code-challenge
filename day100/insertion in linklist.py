class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None

    def count(self):
        count=0
        temp=self.head
        while temp is not None:
            temp=temp.next
            count+=1
        print "Length of the array is:",count

    def first(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode

    def between(self,pos,newdata):
        newnode=node(newdata)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    
    def end(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            return

        else:
            temp=self.head
            while (temp.next):
                temp=temp.next

            temp.next=newnode

    def sort(self,data):
        newnode=node(data)
        if self.head is None:
            newnode.next=self.head
            self.head=newnode

        elif self.head.data>data:
            newnode.next=self.head
            self.head=newnode

        temp=self.head
        while (temp is not None):
            while temp.next.data<data:
                temp=temp.next
            break
        newnode.next=temp.next
        temp.next=newnode

    def delete(self,key):
        temp=self.head
        if (temp is not None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return

        while (temp is not None):
            if (temp.data==key):
                break
            prev=temp
            temp=temp.next

        if (temp==None):
            print "Key not in linked list"

        prev.next=temp.next
        temp=None

    def delpos(self,pos):
        temp=self.head

        if pos==0:
            self.head=temp.next
            temp=None
            return

        for i in range(pos-1):
            temp=temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next=temp.next.next
        temp.next=None
        temp.next=next

    def printlist(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next

def main():
    a=0
    lis=linklist()
    print "1.Insert in beginning"
    print "2.Insert in middle"
    print "3.Insert at end"
    print "4.Delete a node(key)"
    print "5.Delete a node by position"
    print "6.Insert in sorted order"
    print "7.Print the list"
    while a<=7:
        a=input("Enter your choice:")
        if a==1:
            n=input("Enter the data:")
            lis.first(n)
        elif a==2:
            n=input("Enter the data:")
            pos=input("Enter the position to which data must be inserted:")
            lis.between(pos,n)
        elif a==3:
            n=input("Enter the data:")
            lis.end(n)
        elif a==4:
            n=input("Enter the key to be deleted:")
            lis.delete(n)
        elif a==5:
            n=input("Enter the position of node to be deleted:")
            lis.delpos(n)
        elif a==6:
            x=input("Enter the data:")
            lis.sort(x)
        elif a==7:
            lis.printlist()
            print
            lis.count()
        else:
            print "Terminating process"


if __name__=='__main__':
    main()
