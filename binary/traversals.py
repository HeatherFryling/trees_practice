class Traversals:

    def __init__(self):
        return

    # Visit the left branch, the root, then the right branch.
    def in_order(self, node):
        if node != None:
            self.in_order(node.left_child)
            print(node)
            self.in_order(node.right_child)

    # Visit the root before the children.
    def pre_order(self, node):
        if node != None:
            print(node)
            self.pre_order(node.left_child)
            self.pre_order(node.right_child)

    # Visit the node after all children
    def post_order(self, node):
        if node != None:
            self.post_order(node.left_child)
            self.post_order(node.right_child)
            print(node)
    
