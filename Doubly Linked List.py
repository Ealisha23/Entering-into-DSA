# double LL
class Node:
    def __init__(self,value=None):
        self.prev = None
        self.data = value 
        self.next = None

class doubly_LL:
    def __init__(self,head = None):
        self.head = head
    
    def insert_at_end(self,value):
         temp = Node(value)

         if(self.head== None):   
             self.head = temp
             return
         
         else:
             t = self.head
             while(t.next!=None):
                 t = t.next

         t.next = temp  
         temp.prev = t

    def insert_at_beg(self,value):
        temp=Node(value)

        if(self.head==None):
         self.head =temp
        else:
          temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_mid(self,value,x):
        t = self.head
        while (t.next is not None):
            if (t.data == x):
                break
            else:
                t=t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def delete_LL(self,value):
        if (self.head == None):
            print("linked List is empty")   # when LL is empty
            return
        
        t = self.head

       # code for deleting very first node

        if (t.data == value):
            self.head = self.head.next
            self.head.prev = None 
            return

       #code for deleting any node in between

        while (t.next is not None):
            if (t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next 

        # for deleting last node
        
        if (t.data == value):
            t.prev.next = None

    def display_LL(self):
        t = self.head
        while(t!=None):
            print(t.data,end=" <----> ")
            t = t.next
        print("None")

obj = doubly_LL()
obj.insert_at_end(10)
obj.insert_at_end(20) 
obj.insert_at_end(40)
obj.insert_at_beg(5)
obj.insert_at_beg(1)
obj.insert_at_mid(30,20)
obj.delete_LL(1)
obj.delete_LL(40)
obj.display_LL()

