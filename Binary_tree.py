#implement binary tree with all the traversal function 

class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#Insert element into the tree
    def Insert_tree(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left= BinaryTree(data)
                else:
                    self.left.Insert_tree(data)
            elif data > self.data: 
                if self.right is None: 
                    self.right = BinaryTree(data)
                else:
                    self.right.Insert_tree(data)
        else:
            self.data = data
                                 
# Inorder Traversal of a tree  
    def InOrderTrav(self, root):
        res=[]
        if root: 
            res=self.InOrderTrav(root.left)
            res.append(root.data)
            res=res + self.InOrderTrav(root.right)
        return res
    
# Pre-order Traversal of a tree  
    def PreOrderTrav(self, root):
        res=[]
        if root:
            res.append(root.data)
            res=res + self.PreOrderTrav(root.left)
            res=res + self.PreOrderTrav(root.right)
        return res
    
# Post-order Traversal of a tree  
    def PostOrderTrav(self, root):
        res=[]
        if root:
            res=res + self.PostOrderTrav(root.left)
            res=res + self.PostOrderTrav(root.right)
            res.append(root.data)
        return res

                        
#Print the Tree    
    def print_tree(self):
        if self.left: 
            self.left.print_tree()
        print(self.data),
        if self.right: 
            self.right.print_tree()
            
def main():
    num_node=int(input("enter the number of nodes in tree"))
    root= BinaryTree(int(input("enter the root")))
    for x in range(1,num_node):
        root.Insert_tree(int(input("enter the other nodes")))
    # root.Insert_tree(12)
    # root.Insert_tree(35)
    # root.Insert_tree(45)
    # root.Insert_tree(12)
    # root.Insert_tree(83)
    # root.Insert_tree(22)
    # root.Insert_tree(110)
    # root.Insert_tree(127)
    # root.Insert_tree(167)
    root.print_tree()    
    print("Inorder:",root.InOrderTrav(root))
    print("PreOrder:",root.PreOrderTrav(root))
    print("PostOrder:",root.PostOrderTrav(root))

if __name__ == "__main__":
    main()


    
