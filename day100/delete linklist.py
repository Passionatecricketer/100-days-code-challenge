#class to create structure of the node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#class to perform the operation in linked list
class linklist:

    def __init__(self):
        self.head=None

    #Function to insert data in beginning of the list
    def begin(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode

    #function for delettion of the node
    #with first paramater as head and second as node to be deleted
    def deletenode(self,head,key):
        #condition to check if head node is the node to be deleted
        if self.head.data==key:
            #condition to check if list contains only one node
            if self.head.next is None:
                print "Given list contains only one node and the list cannot be empty so terminating the process."
            #Initializing net node as head node after deletion of head node
            self.head=self.head.next
            
        else:
            temp=self.head
            while (temp is not None):
                if (temp.data==key):
                    break
                prev=temp
                temp=temp.next

            #Condition in key is not present in the list
            if (temp==None):
                print "Key not in linked list"

            prev.next=temp.next

            temp=None

    #Function to print the list
    def printlist(self):
        temp=self.head
        while(temp):
            print temp.data,
            temp=temp.next

#Driver program
if  __name__ == '__main__':
    lis=linklist()
    lis.begin(4)
    lis.begin(9)
    lis.begin(5)
    
    print "Original list"

    lis.printlist()

    print

    print "List after deletion"

    #If node to be deleted is 4
    lis.deletenode(5,4)

    lis.printlist()
    print

    #If node to be deleted is head node
    lis.deletenode(5,5)

    lis.printlist()
    print
    
    #If only one node is left
    lis.deletenode(9,9)

    lis.printlist()
    print
