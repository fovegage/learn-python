class Node:
    def __init__(self, value):
        self.value = value
        self._items = []

    def __repr__(self):
        return 'Node{!r}'.format(self.value)


node = Node(1)
