def remove(node, value):
    while node.get_next() is not None:
        if node.get_element() is value:
            if node.get_previous() is None:
                node = node._next
                node.set_previous(None)
            else:
                prev_node = node.get_previous()
                node = node._next
                prev_node.set_next(node)
                node.set_previous(prev_node)

    return node
