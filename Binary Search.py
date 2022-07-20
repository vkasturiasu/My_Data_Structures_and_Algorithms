class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,child):
        if child == self.data:
            return
        elif child< self.data:
            if self.left is None:
                self.left = BinaryTree(child)
                return


            self.left.add_child(child)

        elif child> self.data:
            if self.right is None:
                self.right = BinaryTree(child)
                return

            self.right.add_child(child)

    def search(self, value):
        if value == self.data:
            return True

        elif value< self.left:
            if self.left == None:
                return False

            self.left.search(value)

        elif value > self.right:
            if self.right == None:
                return False
            self.right.search(value)

    def inorder_triversal(self):
        inorder = []
        if self.left:
            inorder += self.left.inorder_triversal()
        inorder.append(self.data)


        if self.right:
            inorder += self.right.inorder_triversal()

        return inorder

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        elements = self.inorder_triversal()
        s = 0
        for i in elements:
            s += i
        return s

    def post_order_triversal(self):
        elements =[]
        if self.left:
            elements += self.left.post_order_triversal()
        if self.right:
            elements += self.right.post_order_triversal()

        elements.append(self.data)
        return elements


    def pre_order_triversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.post_order_triversal()
        if self.right:
            elements += self.right.post_order_triversal()
        return elements

    def deleting(self, element):
        if self.data <element:
            if self.right:
                self.right = self.right.deleting(element)
        elif self.data > element:
            if self.left:

                self.left = self.left.deleting(element)
        else:
            if self.left == None and self.right == None:
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.deleting(max_val)
        return self


def build_tree(elements):
    root = BinaryTree(elements[0])
    for i in elements:
        root.add_child(i)
    return root


# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree



if __name__ == "__main__":
    a = build_tree([15,7,12,14,20,23,27,88])
    a.deleting(27)
    print(a.inorder_triversal())










