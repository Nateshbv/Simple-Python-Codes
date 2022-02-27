# Create a Class Node to create the node
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
# Create the list 
class List:
    def __init__(self):
        self.head= None
# function for inserting to the list in sorted order        
    def Insert_sort(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        
        else:
            current=self.head
            while( current.next is not None and current.next.data < new_node.data):
                current=current.next
                
            new_node.next=current.next
            current.next=new_node
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def List_print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
def main():
    ilist= List()
    nodes=int(input("enter the number of nodes"))
    for i in range(0,nodes):
        new_node = Node(int(input("enter the nodes")))
        ilist.Insert_sort(new_node)
# Print the sorted linked list 
    print ("Create Linked List")
    ilist.List_print()  

if __name__ == "__main__":
    main()
        
        
