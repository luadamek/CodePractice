# write a class that finds the longest distance between two nodes in a binary tree.
'''
     A
   C   B
  D E
 I   F
      G
       H

'''

class Node:
     def __init__(self, val, left=None, right=None):
         self.left = left
         self.right = right


#make some example trees
'''
     A
   B  C
 E
G
'''
tree_1 = Node(1, Node(2, Node(3, Node(4))), Node(5))
distance_1 = 4


'''
     A
   C   B
      E F
     G   H
    J     I
'''
tree_2 = Node(1, Node(3), Node(2, Node(4, Node(5), Node(6)), Node(7, right=Node(8, right=Node(9, right=Node(10))))))
distance_2 = 6

tree_3 = Node(1)
distance_3 = 0

tree_4 = Node(1, right=Node(2))
distance_4 = 1

def calc_distance_helper(n):
    if n is None: return -1, -1

    left_distance, left_turnaround_distance = calc_distance_helper(n.left)
    right_distance, right_turnaround_distance = calc_distance_helper(n.right)
    this_turnaround_distance = 2 + left_distance + right_distance

    # the maximum downward distance, and keep track of the longest turnaround distance
    return 1 + max(left_distance, right_distance), max(this_turnaround_distance, max(left_turnaround_distance, right_turnaround_distance))

def calc_distance(n):
    return max(calc_distance_helper(n))


if __name__ == "__main__":
    print("Testing")
    assert calc_distance(tree_1) == distance_1
    assert calc_distance(tree_2) == distance_2
    assert calc_distance(tree_3) == distance_3
    assert calc_distance(tree_4) == distance_4
