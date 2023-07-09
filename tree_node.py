class TreeNode:
    def __init__(self, data):
        self.parent = None 
        self.children = []
        self.data = data 
    def add_child(self, child):
        self.children.append(child)
    def returnSelf(data):
        if data == self.data:
            return self

class BinaryTreeNode:
    def __init__(self, data):
        self.parent = None 
        self.left = None
        self.right = None
        self.data = data 
    def add_child_left(self, child):
        self.left = child
    def add_child_right(self, child):
        self.right = child
    def returnLeftChild(self):
        return self.left
    def returnRightChild(self):
        return self.right
    
    def returnSelf(self):
        return self.data

#clothes = TreeNode("potty")
#shirt = TreeNode("shirt")
#clothes.add_child(shirt)
#pant = TreeNode("pant")
#clothes.add_child(pant)
#Tshirt = TreeNode("Tshirt")
#shirt.add_child(Tshirt)
#print(clothes.children)