

def inorder(node):
    if node is None:
        return []
    values = []
    values.extend(inorder(node.left))
    values.extend(node.value)
    values.extend(inorder(node.right))
    return values

def preorder(node):
    if node is None:
        return []
    values = []
    values.extend(node.value)
    values.extend(preorder(node.left))
    values.extend(preorder(node.right))
    return values

def postorder(node):
    if node is None:
        return []
    values = []
    values.extend(postorder(node.left))
    values.extend(postorder(node.right))
    values.extend(node.value)
    return values