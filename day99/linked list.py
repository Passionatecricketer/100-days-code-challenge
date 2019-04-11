class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print temp.data
            temp=temp.next

if  __name__ == '__main__':
    lis=linkedlist()
    lis.head=node(45)
    second=node(56)
    third=node(67)

    lis.head.next=second
    second.next=third
    third.next=None
    
    lis.printlist()
