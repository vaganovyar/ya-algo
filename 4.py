class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def add_value(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_value(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_value(value)

    def left_this_right_way(self, arr):
        if self.left is not None:
            self.left.left_this_right_way(arr)
        arr.append(self.value)
        if self.right is not None:
            self.right.left_this_right_way(arr)


class Tree:
    root = None

    def __init__(self, root: Node = None):
        self.root = root

    def add_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add_value(value)

    def tree_sort(self):
        arr = []
        self.root.left_this_right_way(arr)

        return arr


# Пример входных данных с доски
"""
7
8
5
10
3
6
9
12
"""
elements_number = int(input())
tree = Tree()
for i in range(elements_number):
    tree.add_value(int(input()))

print(*tree.tree_sort())
