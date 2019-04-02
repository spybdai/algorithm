"""
Construct a Binary Tree from Preorder and Inorder

in[]   = {4, 8, 2, 5, 1, 6, 3, 7}
pre[] = {1, 2, 4, 8, 5, 3, 6, 7} 

"""

from tree import Node
from depth_first_traversal import inorder as inorder_traversal
from depth_first_traversal import postorder as postorder_traversal
from depth_first_traversal import preorder as preorder_traversal

pre_index = 0

def build_tree(preorder, inorder, start, end):
    """
    build with preorder and inorder
    """
    global pre_index 

    if start > end:
        return None

    print pre_index, start, end, preorder[pre_index]

    node = Node(value=preorder[pre_index])
    pre_index += 1

    if end == start:
        return node

    in_index = search(inorder, node.value, start, end)
    
    node.left = build_tree(preorder, inorder, start, in_index-1)
    node.right = build_tree(preorder, inorder, in_index+1, end)

    return node

def build_tree_2(postorder, inorder, start, end):
    """
    build with postorder and inorder
    """

    global pre_index
    if start > end:
        return None
    
    #print pre_index, start, end, postorder[pre_index]

    node = Node(value=postorder[pre_index])
    pre_index -= 1

    if end == start:
        return node

    in_index = search(inorder, node.value)

    node.right = build_tree_2(postorder, inorder, in_index+1, end)
    node.left = build_tree_2(postorder, inorder, start, in_index-1)

    return node


def search(array, value, start, end):
    for index in range(start, end+1):
        if array[index] == value:
            return index
    return -1

def test_build_tree():
    global pre_index 
    pre_index = 0
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    preorder = [1, 2, 4, 8, 5, 3, 6, 7]

    tree = build_tree(preorder, inorder, 0, len(inorder)-1) 
    # test with traversal
    preorder_output_list = []
    inorder_output_list = []
    preorder_traversal(tree, preorder_output_list)
    inorder_traversal(tree, inorder_output_list)
    print preorder_output_list == preorder
    print inorder_output_list == inorder

    pre_index = 0
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']

    tree = build_tree(preorder, inorder, 0, len(inorder)-1) 
    
    # test with traversal
    preorder_output_list = []
    inorder_output_list = []
    preorder_traversal(tree, preorder_output_list)
    inorder_traversal(tree, inorder_output_list)
    print preorder_output_list == preorder
    print inorder_output_list == inorder 
   
def test_build_tree_2():
    global pre_index

    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    postorder = ['D', 'E', 'B','F', 'C', 'A']
    pre_index = len(inorder) -1
    tree = build_tree_2(postorder, inorder, 0, len(inorder)-1) 

    postorder_output_list = []
    postorder_traversal(tree, postorder_output_list)
    print postorder_output_list == postorder

    inorder_output_list = []
    inorder_traversal(tree, inorder_output_list)
    print postorder_output_list == postorder

if __name__ == '__main__':
    test_build_tree()
    #test_build_tree_2()
