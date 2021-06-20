class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}>'

def min_path_sum(root):
    min_value = float('inf')
    queue = [(root, root.value)]

    while queue:
        node, curr_sum = queue.pop()

        if not node.right and not node.left:
            if min_value > curr_sum:
                min_value = curr_sum
            continue
        
        if node.left:
            queue.append((node.left, curr_sum + node.left.value))
        if node.right:
            queue.append((node.right, curr_sum + node.right.value))
    
    return min_value

node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
print(min_path_sum(node))