from Double_Node import DNode

class BinaryNode(DNode):
    def __init__(self, element=None, parent_node=None, left_child=None, right_child=None):
        super().__init__(element)
        self._parent_node = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def get_parent(self):
        return self._parent_node

    def get_left(self):
        return self._left_child

    def get_right(self):
        return self._right_child

    def set_parent(self, new_parent):
        if self._parent_node is None:
            self._parent_node = new_parent

    def set_left(self, new_left):
        if self._left_child is None:
            self._left_child = new_left

    def set_right(self, new_right):
        if self._right_child is None:
            self._right_child = new_right