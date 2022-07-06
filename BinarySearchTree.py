
class Node():

    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        self.root = self.insertRec(self.root,key)

    def insertRec(self,node,key):
        nodeToRet = node
        if node == None:
            node = Node(key)
            nodeToRet = node
        else:
            if node.key < key:
                node.right = self.insertRec(node.right,key)
            elif node.key > key:
                node.left = self.insertRec(node.left,key)
            else:
                print("Repeated key not supported!")
        return nodeToRet

    def insert_iter(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            cursor = self.root
            inserted = False
            while not inserted:
                if val > cursor.info:
                    if cursor.right != None:
                        cursor = cursor.right
                    else:
                        cursor.right = Node(val)
                        inserted = True
                else:
                    if cursor.left != None:
                        cursor = cursor.left
                    else:
                        cursor.left = Node(val)
                        inserted = True
                        
    # For non-decreasing order
    def inorderTraversalToList(self, node):
        res = []
        if node:
            res = self.inorderTraversalToList(node.left) 
            res.append(node.key)
            res = res + self.inorderTraversalToList(node.right)
        return res

    # For copy the tree
    def preorderTraversalToList(self, node):
        res = []
        if node:
            res.append(node.key)
            res = self.inorderTraversalToList(node.left)
            res = res + self.inorderTraversalToList(node.right)
        return res

    # For delete the tree
    def postorderTraversalToList(self, node):
        res = []
        if node:
            res = self.inorderTraversalToList(node.left)
            res = res + self.inorderTraversalToList(node.right)
            res.append(node.key)
        return res

    def printTree(self):
        print("Print Inorder: ")
        elements = self.inorderTraversalToList(self.root)
        for element in elements:
            print(f"- {element}")

    def height(self, root):
        if (root.left is None) and (root.right is None):
            return 0
        elif (root.left is None):
            return 1 + self.height(root.right)
        elif (root.right is None):
            return 1 + self.height(root.left)
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

class Card:
    
    def __init__(self, val) -> None:
        self.values = {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14,
        }
        self.val = val

    def __lt__(self, other):
        return self.values[self.val] < self.values[other.val]

    def __gt__(self, other):
        return self.values[self.val] > self.values[other.val]

    def __str__(self):
        return self.val

tree = BinarySearchTree()
cardsStrings = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for card in cardsStrings:
    tree.insert( Card(card))

tree.printTree()