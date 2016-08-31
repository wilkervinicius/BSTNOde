class BSTNode(object):
    #inicializa classe
    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

        # insere
    def add(self,node):
        if node.key < self.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.add(node)
        if node.key >= self.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.add(node)

    # se tem filho a esquerda
    def hasLeftChild(self):
        if self.left:
            return True
        return False


    # localiza valor
    def search(self, key):
        if key == self.key:
            return self
        if key < self.key and self.left:
            return self.left.search(key)
        if key > self.key and self.right:
            return self.right.search(key)

    # imprime lista ordenada
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.key)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def pos_order(self):
        if self.left:
            self.left.pos_order()
        if self.right:
            self.right.pos_order()
        print (self.key)

    # retorna menor valor
    def find_minimum(self):
        if self.left:
            return self.left.find_minimum()
        return self

    # retorna maior valor
    def find_maximum(self):
        if self.right:
            return self.right.find_maximum()
        return self

    # se tem filho a direito
    def hasRightChild(self):
        if self.right:
            return True
        return False

   # é root ou raiz
    def isRoot(self):
        if self.parent:
            return False
        return True

    # é filho a esquerda
    def isLeftChild(self):
        if self.parent:
            if self.key < self.parent:
                return True
    # é filho a direita
    def isRightChild(self):
        if self.parent:
            if self.key < self.parent:
                return True
   # é folha?
    def isLeaf(self):
        if self.left:
            return False
        elif self.right:
            return False
        else:
            return True
    # informa se tem filhos
    def hasAnyChildren(self):
        if self.left or self.right:
            return True
        return False
    # informa se tem dois filhos
    def hasBothChildren(self):
        if self.left and self.right:
            return True
        return False











# Aulas Anteriores
# root = BSTNode(10)
#
# root.left = BSTNode(7)
# root.right = BSTNode(18)
#
# root.left.left = BSTNode(3)
# root.left.right = BSTNode(9)
# root.left.left.left = BSTNode(1)
# root.left.right.left = BSTNode(8)
#
# root.right.left = BSTNode(11)

root = BSTNode(10)
root.add(7)
root.add(18)
root.add(3)
root.add(1)
root.add(8)
root.add(11)




print("===== Executando in-order =====")
print(root.in_order())

print("===== Executando pre-order =====")
print(root.pre_order())

print("===== Executando pos-order =====")
print(root.pos_order())

print ("===== Executando minimo =====")
minimo = root.find_minimum()
print(minimo)
print("===== Executando maximo =====")
maximo = root.find_maximum()
print(maximo)
