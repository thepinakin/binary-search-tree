class TreeNode():
    def __init__(self, key, leftChild, rightChild, parent):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent


class BinSearchTree():
    def __init__(self):
        self.root = None

    def create(self, val):

        if self.root == None:

            self.root = Node(val)

        else:

            current = self.root

            while 1:

                if val < current.key:

                    if current.leftChild:
                        current = current.leftChild
                    else:
                        current.leftChild = Node(val)
                        break;

                elif val > current.key:

                    if current.rightChild:
                        current = current.rightChild
                    else:
                        current.rightChild = Node(val)
                        break;

                else:
                    break

    def binaryTree(self):

        self.root.parent = 0
        queue = [self.root]
        out = []
        current_level = self.root.parent

        while len(queue) > 0:

            current_node = queue.pop(0)

            if current_node.parent > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.key) + " ")

            if current_node.leftChild:
                current_node.leftChild.parent = current_level + 1
                queue.append(current_node.leftChild)

            if current_node.rightChild:
                current_node.rightChild.parent = current_level + 1
                queue.append(current_node.rightChild)

        print("".join(out))

    def returnRoot(self):
        return self.root.key

    def addChild(self, key, Node):
        if (key < Node.key):
            if (Node.leftChild != None):
                self.addChild(key, Node.leftChild)
            else:
                Node.leftChild = TreeNode(key, None, None, Node)
        else:
            if (Node.rightChild != None):
                self.addChild(key, Node.rightChild)
            else:
                Node.rightChild = TreeNode(key, None, None, Node)

    def addNode(self, key):
        if self.root == None:
            self.root = TreeNode(key, None, None, None)
        else:
            self.addChild(key, self.root)

    def inorderTreeWalk(self, Node):
        if Node != None:
            self.inorderTreeWalk(Node.leftChild)
            print(Node.key)
            self.inorderTreeWalk(Node.rightChild)

    def TreeWalk(self, Node):
        if Node != None:
            print(Node.key)
            self.TreeWalk(Node.leftChild)
            self.TreeWalk(Node.rightChild)

    def TreeSearch(self, Node, key):
        if (Node == None or key == Node.key):
            return Node
        if key < Node.key:
            return self.TreeSearch(Node.leftChild, key)
        else:
            return self.TreeSearch(Node.rightChild, key)

    def TreeSuccessor(self, Node):
        if Node.rightChild != None:
            return self.TreeMinimum(Node.rightChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.rightChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode

    def TreePredeccessor(self, Node):
        if Node.leftChild != None:
            return self.TreeMaximum(Node.leftChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.leftChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode

    def TreeMinimum(self, Node):
        while Node.leftChild != None:
            Node = Node.leftChild
        return Node

    def TreeMaximum(self, Node):
        while Node.rightChild != None:
            Node = Node.rightChild
        return Node

    def TreeInsert(self, T, Node):
        p = Node.parent
        x = T.root
        while x != None:
            p = x
            if Node.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild
        Node.parent = p
        if p == None:
            T.root = Node  # Tree was empty
        elif Node.key < p.key:
            p.leftChild = Node
        else:
            p.rightChild = Node

    def preorderTreeWalk(self, Node):
        if Node != None:
            print(Node.key)
            self.preorderTreeWalk(Node.leftChild)
            self.preorderTreeWalk(Node.rightChild)

    def postorderTreeWalk(self, Node):
        if Node != None:
            self.postorderTreeWalk(Node.leftChild)
            self.postorderTreeWalk(Node.rightChild)
            print(Node.key)

def modSearch(root, Node):
    if root == None:
        return None

    if root.key == Node:
        return True

    if (modSearch(root.leftChild, Node) or
            modSearch(root.rightChild, Node)):
        print(root.key),
        return True
        print(Node)
    else:
        return False

def main():
    bt = BinSearchTree()
    data = [5, 4, 10, 3, 11, 12, 6, 7, 2, 1, 19, 8]
    data = [15, 6, 18, 3, 7, 17, 19, 2, 4, 13, 9]
    for val in data:
        bt.addNode(val)
    print("\nRoot Node")
    print(bt.returnRoot())

    print("\nTree Walk")
    bt.TreeWalk(bt.root)

    print("\nTree Minimum")
    print(bt.TreeMinimum(bt.root).key)

    print("\nTree Maximum")
    print(bt.TreeMaximum(bt.root).key)

    print("\nTree Successor")
    node = bt.TreeSearch(bt.root, 15)
    print(bt.TreeSuccessor(node).key)

    print("\nTree Predeccessor")
    node = bt.TreeSearch(bt.root, 15)
    print(bt.TreePredeccessor(node).key)

    print("\nNode Insert")
    tn = TreeNode(8, None, None, None)
    print(bt.TreeInsert(bt, tn))

    print("\nIn Order Tree Walk")
    bt.inorderTreeWalk(bt.root)

    for val in data:
        bt.create(val)
    print('\nBinary Search Tree')
    bt.binaryTree()

    print("\nPre Order Tree Walk")
    bt.preorderTreeWalk(bt.root)

    print("\nPost Order Tree Walk")
    bt.postorderTreeWalk(bt.root)

    print("\nModified Search")
    modSearch(bt.root, 8)


if __name__ == "__main__":
    main()
