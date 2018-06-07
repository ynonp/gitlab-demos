"""
Circular reference
"""

import weakref

class Node:
    def __init__(self, value=0, left=None, right=None):
        self._left = None
        self._right = None

        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    # def close(self):
    #     if self.left is not None:
    #         self.left.close()
    #     if self.right is not None:
    #         self.right.close()
    #
    #     self.parent = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is None: return
        node.parent = weakref.proxy(self)
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is None: return
        node.parent = weakref.proxy(self)
        self._right = node

    def __del__(self):
        print(f'Node {self.value} was deleted')

def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(5)
    root.left.left = Node(17)
    # print: 5
    print(root.left.left.parent.value)

main()
# here everything is deleted
print('--- the end')