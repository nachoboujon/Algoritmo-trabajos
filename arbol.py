class BinaryTree:
    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
        
        #la funcion tiene que devolver
    def insert_node(self, value):
        def __insert (root, value):
            if root is None:
                print ('Crear nodo')
                return BinaryTree.__Node(value)
            elif value< root.value:
                print ('Insertar izquierda')
                root.left = BinaryTree.__Node(value)
            else:
                print ('Insertar derecha')
                root.right = BinaryTree.__Node(value)
            return root
            
        self.root = __insert(self.root, value)
        
    def preorden (self):
        def __preorden(root):
            if root is not None:
                print (root.value)
                print (f'Izquierda de {root.value}')
                __preorden(root.left)
                print (f'Derecha de {root.value}')
                __preorden(root.right)
        if self.root is not None:
            __preorden(self.root)


tree = BinaryTree()
tree.insert_node(19)
tree.insert_node(7)
tree.insert_node(31)
tree.insert_node(11)
tree.insert_node(21)
tree.insert_node(10)
print (tree.root.value, tree.root.left.value, tree.root.right.value)