
"""الگوریتم مرتب سازی روی درخت جستجوی دودویی
 با مرتبه ان لوگ ان به عنوان یک 
  روش مرتب سازی بر اساس این ایده  است 
  که درخت جستجوی دودویی را به عنوان یک مرتب سازی کناری استفاده می کند
    در این الگوریتم درخت جستجوی دودویی به صورت پایین 
    :به بالا مرتب می شود در اینجا یک پیاده سازی ممکن برای این الگوریتم در پایتون آمده است"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def binary_tree_sort(arr):
    if not arr:
        return arr

    # create a binary search tree
    root = Node(arr[0])
    for i in range(1, len(arr)):
        node = Node(arr[i])
        current = root
        while True:
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right

    # traverse the binary search tree in-order
    def traverse_in_order(node):
        if node is not None:
            yield from traverse_in_order(node.left)
            yield node.value
            yield from traverse_in_order(node.right)

    return list(traverse_in_order(root))
