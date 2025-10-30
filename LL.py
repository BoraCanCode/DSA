class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
# n1 = Node(10)
# print(n1,n1.data,n1.next)
# n2 = Node(20)
# print(n2,n2.data,n2.next)
# n1.next=n2
# print(n1.next)

# adding node to head

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_head(self,data):       
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_tail(self,data):
        if self.head==None:
            self.insert_at_head(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            new =Node(data)
            temp.next=new

    def insert_in_between(self,data,pos):
        temp=self.head
        i=0
        while temp.next!=None and i<pos:
            temp=temp.next
            i+=1
        new =Node(data)
        remaining=temp.next
        temp.next=new
        new.next=remaining

    def delete_at_head(self):
        new_head = self.head.next
        self.head.next=None
        self.head=new_head
    
    def delete_at_tail(self):
        if self.head==None:
            return 
        if self.head.next==None:
            return 
        prev=self.head
        while prev.next.next!=None:
            prev=prev.next
        prev.next=None
    
    def reverse(self):
        prev = None
        current = self.head
        while current!=None:
            remaining = current.next
            current.next = prev
            prev = current
            current = remaining
        self.head = prev

    def printList(self):
        if self.head is None:
            print('Empty List')
            return 
        current=self.head
        while current is not None:
            print(current.data,end='->')
            current=current.next
        print('None')
ll = LinkedList()
ll.insert_at_tail(40)
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_in_between(500,2)
ll.insert_at_tail(30)
ll.delete_at_head()
ll.delete_at_tail()
ll.reverse()
ll.printList()


