# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    size = []
    height = 0
    height, size = getheights(tree, height, size)
    return max(size)


def getheights(tree, height, size):
    if not tree: return height, size
    if tree.left == None and tree.right == None:
        return height, size
    lheight, lsize = getheights(tree.left, height + 1, size)
    rheight, rsize = getheights(tree.right, height + 1, size)
    height = max(lheight, rheight)
    size.append(lheight + rheight)
    return height, size


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    size = []
    height = 0
    height, size = getheights(tree, height, size)
    return max(size)


def getheights(tree, height, size):
    if not tree: return height, size
    if tree.left == None and tree.right == None:
        return height, size
    lheight, lsize = getheights(tree.left, height + 1, size)
    rheight, rsize = getheights(tree.right, height + 1, size)
    height = max(lheight, rheight)
    size.append(lheight + rheight)
    return height, size

print()