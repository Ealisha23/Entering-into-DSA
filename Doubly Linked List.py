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
    
        

    def display_LL(self):
        t = self.head
        while(t!=None):
            print(t.data,end=" <----> ")
            t = t.next
        print("None")

obj = doubly_LL()
obj.insert_at_end(10)
obj.insert_at_end(20) 
obj.insert_at_end(30)
obj.insert_at_beg(5)
obj.insert_at_beg(1)
obj.display_LL()

