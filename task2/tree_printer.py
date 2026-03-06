from PrettyPrint import PrettyPrintTree

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_heap(heap):
    pt = PrettyPrintTree(lambda x: [x for x in [x.left, x.right] if x is not None], lambda x: x.val)
    
    nodes = [BinaryTree(i) for i in heap.data]
    for i in range(len(nodes)):
        l = heap.left_child(i)
        r = heap.right_child(i)
        if l < len(nodes):
            nodes[i].left = nodes[l]
        if r < len(nodes):
            nodes[i].right = nodes[r]
    
    pt(nodes[0])
