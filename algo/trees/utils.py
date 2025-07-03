
def inorder_traversal(node):
    """order: L-C-R -- remember in order as clock-wise"""
    if node is None:
        return []
    values = []
    values.extend(inorder_traversal(node.left))
    values.append(node.value)
    values.extend(inorder_traversal(node.right))
    return values


def preorder_traversal(node):
    """order: C-L-R -- remember pre-order as first center and then clock-wise"""
    if node is None:
        return []
    values = list()
    values.append(node.value)
    values.extend(preorder_traversal(node.left))
    values.extend(preorder_traversal(node.right))
    return values


def postorder_traversal(node):
    """order: L-R-C -- remember post-order as clock-wise but having the center after"""
    if node is None:
        return []
    values = list()
    values.extend(postorder_traversal(node.left))
    values.extend(postorder_traversal(node.right))
    values.append(node.value)
    return values


def level_order_traversal(node):
    """order breath-first, ie have all the same level together"""
    # to implement solution with queue
    pass
