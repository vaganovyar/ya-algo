class Node:
    def __init__(self, value, next_node=None):
        self.next_node = next_node
        self.value = value


class List:
    def __init__(self, root=None):
        self.root = root
        self.last = root

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
            self.last = self.root
        else:
            self.last.next_node = Node(value)
            self.last = self.last.next_node

    def reverse(self):
        root = self.root
        now_node = self.root.next_node
        last_node = self.root
        while now_node is not None:
            next_node = now_node.next_node
            now_node.next_node = last_node
            last_node = now_node
            now_node = next_node
        self.root = last_node
        self.last = root
        self.last.next_node = None

    def to_list(self):
        arr = []
        now_node = self.root
        while now_node is not None:
            arr.append(now_node.value)
            now_node = now_node.next_node

        return arr


a = list(map(int, input().split()))
l = List()
for i in a:
    l.append(i)
print(l.to_list())
l.reverse()
print(l.to_list())
