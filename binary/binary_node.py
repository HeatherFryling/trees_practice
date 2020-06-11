class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_right_child(self, right_child):
        self.right_child = right_child

    def add_left_child(self, left_child):
        self.left_child = left_child

    def __str__(self):
        return "Node{val=" + str(self.value) + "}"