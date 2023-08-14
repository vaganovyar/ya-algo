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

    def tree_bfs(self):
        queue = [self.root]
        arr = []
        while len(queue) != 0:
            now = queue.pop(0)
            if now is None:
                continue
            arr.append(now.value)
            queue.append(now.left)
            queue.append(now.right)

        return arr


# Пример входных данных с доски
"""
8 5 3 10 6 9 8
"""


def tree_sort(arr):
    tree = Tree()
    for elem in arr:
        tree.add_value(elem)

    return tree.tree_sort()


def tree_bfs(arr):
    tree = Tree()
    for elem in arr:
        tree.add_value(elem)

    return tree.tree_bfs()


print(*tree_bfs(list(map(int, input().split()))))
