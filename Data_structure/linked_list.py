class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data=data
        self.next=next
    def setData(self, data):
        self.data=data
    
    def getData(self):
        return self.data

    def setNext(self,next):
        self.next=next
    
    def getNext(self):
        return self.next

    def hasNode(self):
        return self.next!=None


class LinkedList(object):
    def __init__(self, node=None) -> None:
        self.head=node
        self.length=0
    
    def length(self):
        current=self.head
        count=0
        while current!=None:
            current=current.next
            count+=1
        return count
    
    def insertAtBeginning(self, data):
        newNode=Node()
        newNode.data=data
        if self.length==0:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1
    
    def insertAtEnd(self, data):
        newNode=Node()
        newNode.data=data
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=newNode
        newNode.next=None
        self.length+=1

    def insertAtPosition(self,pos,data):
        
        if pos>self.length or pos<0:
            return None
        
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode=Node()
                    newNode.data=data
                    count=1
                    current=self.head
                    while count<=pos-1:
                        count+=1
                        current=current.next
                    newNode.next=current.next
                    current.next=newNode
                    self.length+=1
    
    def deleteFromBeginning(self):
        if self.length==0:
            print('list is empty')
        
        else:
            self.head=self.head.next
            self.length-=1
    
    def deleteFromLast(self):
        if self.length==0:
            print('list is empty')
        
        else:
            current=self.head
            previous=self.head

            while current.next!=None:
                previous=current
                current=current.next
            
            previous.next=None
            self.length-=1
    
    def printAllElement(self):
        if self.length==0:
            print('linked list is empty')
        else:
            current=self.head
            while current!=None:
                print(current.data, end=' ')
                current=current.next
            print()



li=LinkedList()
li.insertAtBeginning(5)
li.insertAtBeginning(10)
li.insertAtEnd(16)

li.printAllElement()
print('Length')
print(li.length)
li.insertAtPosition(2,33)
li.printAllElement()
print('Length')
print(li.length)