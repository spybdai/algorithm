"""
traversal with preorder, inorder and postorder

"""

def inorder(tree, out_list):
    """
    return a list
    """
    if not tree:
        return 
    
    inorder(tree.left, out_list) 
    out_list.append(tree.value)
    inorder(tree.right, out_list) 

def preorder(tree, out_list):
    """
    """
    if not tree:
        return 
    
    out_list.append(tree.value)
    preorder(tree.left, out_list) 
    preorder(tree.right, out_list) 
    
def postorder(tree, out_list):
    """
    """
    if not tree:
        return 
    
    postorder(tree.left, out_list) 
    postorder(tree.right, out_list) 
    out_list.append(tree.value)
    
