from binary_node import Node
from tree import Tree
from traversals import Traversals

def main():
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(1)
    node6 = Node(8)
    node7 = Node(7)
    node8 = Node(6)

    my_tree = Tree(node1)
    node1.add_left_child(node2)
    node1.add_right_child(node6)
    node2.add_left_child(node4)
    node2.add_right_child(node3)
    node6.add_left_child(node7)
    node6.add_right_child(node8)

    trav = Traversals()
    trav.post_order(my_tree.root)




main()


