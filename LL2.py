class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    def insert_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tail(self,data):
        if self.head==None:
            self.insert_head(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        new = Node(data)
        temp.next = new
    
    def reverse(self):
        prev = None
        current = self.head
        while current!=None:
            remaining = current.next
            current.next=prev
            prev = current
            current=remaining
        self.head = prev



    def k_node_from_last(self,k):
        a = self.head
        b=self.head
        count =0
        while count<k:
            a = a.next
            count+=1
        while a!=None:
            a = a.next
            b = b.next
        return b

    def add_one_to_list(self):
        self.reverse()
        temp = self.head
        carry = 1
        
        while temp!=None:
            nodeSum = temp.data+carry
            temp.data = nodeSum %10
            
            carry = nodeSum//10
            prev = temp
            temp = temp.next
        if carry!=0:
            prev.next=Node(carry)
        self.reverse()
    
    def remove_duplicate_in_sorted_list(self,head):
        if head is None:
            return head
        temp = head
        while temp.next!=None:
            if temp == temp.next:
                temp.next=temp.next.next
            else:
                temp = temp.next
        return head
        

    def show(self):
        current = self.head
        while current is not None:
            print(current.data,end='->')
            current=current.next
        print('None')

ll =LL()
ll.tail(10)
ll.tail(20)
ll.tail(30)
ll.insert_head(40)
ll.insert_head(50)
print(ll.k_node_from_last(2).data)
ll.show()
ll.add_one_to_list()
ll.show()
        





        