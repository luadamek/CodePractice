"""
Given a list of K sorted linked lists, in ascending order, write a piece of code that merges them together
into a single sorted linked list.

I could just keep track of the smallest element among the linked lists,
and append this to the final sorted linked list. However, every time I push to the final linked list,
I need to find the next smalest element. This is an O(K) operation. I need to do this for every element.
This gives O(K * N) if all lists are of length N.

A better solution would be to use a heap and a dictionary. The heap would store the values of the head of each
linked list. Popping and finding the next smallest value is an O(log(K)) operation. building the heap is an O(K)
operation, but only happens once. When I pop an item from the heap, I need to know what list it came from, so I
can get the next element from that linked list and put it into the heap. I can use a dictionary for this to keep
an O(1) lookup time. Duplicates can be handled by keeping the value of the dictionary in a linkedlist. The time
complexity of this approach would be O(log(K) * N), which is much better.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def repr_helper(self, depth = 0):

        to_return = ""
        if depth == 0: to_return = "LinkedList( "

        if self.next is None:
            return to_return + str(self.val) + " )"
        else:

            return to_return + "{} -> {}".format(self.val,self.next.repr_helper(depth = depth + 1))

    def __repr__(self):
        return self.repr_helper(depth = 0)


# a function to check if two lists are the same
def compare_lists(list1, list2):
    if list1 is None and list2 is None: return True
    elif list1 is None and list2 is not None: return False
    elif list1 is not None and list2 is None: return False
    elif list1.val == list2.val: return compare_lists(list1.next, list2.next)
    else: return False


#    heap = []            # creates an empty heap
#    heappush(heap, item) # pushes a new item on the heap
#    item = heappop(heap) # pops the smallest item from the heap
 #   item = heap[0]       # smallest item on the heap without popping it
 #   heapify(x)           # transforms list into a heap, in-place, in linear time
 #   item = heapreplace(heap, item) # pops and returns smallest item, and adds

# value_to_index_dict: a dictionary to keep track of which linked list the smallest value came from

# a function to add a new index for a given value
def update_value_to_index_dict(value_to_index_dict, val, i):
    if val not in value_to_index_dict:
        value_to_index_dict[val] = ListNode(i)
    else:
        value_to_index_dict[val] = ListNode(i, next=value_to_index_dict[val])

# a function to remove and index given a value
def pop_value_to_index_dict(value_to_index_dict, val):
    index = value_to_index_dict[val].val
    #update the value_to_index_dict
    if value_to_index_dict[val].next is None:
        del value_to_index_dict[val]
    else:
        value_to_index_dict[val] = value_to_index_dict[val].next
    return index

import heapq
def mergeKLists(lists):
    firstnode = None
    currnode = None

    #build the heap: 
    heap = [el.val for el in lists]
    heapq.heapify(heap)

    #get the dictionary of values to linked list indices 
    value_to_index_dict = {}
    for i in range(0, len(lists)):
        val = lists[i].val
        update_value_to_index_dict(value_to_index_dict, val, i)

    while heap:
        minval = heap[0]
        index = pop_value_to_index_dict(value_to_index_dict, minval)

        #get the next item
        next_item = lists[index].next
        if next_item is not None: #if there is a next item, push it to the heap
            heapq.heapreplace(heap, next_item.val)
            update_value_to_index_dict(value_to_index_dict, next_item.val, index)
            lists[index] = next_item #update the head of the list to point at the next entry
        else:
            heapq.heappop(heap)

        #append to the linkedlist
        if firstnode is None:
            firstnode = ListNode(minval)
            currnode = firstnode
        else:
            currnode.next = ListNode(minval)
            currnode = currnode.next

    return firstnode


if __name__ == "__main__":
    list_1_1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
    list_1_2 = ListNode(3,ListNode(6,ListNode(8)))
    list_1_3 = ListNode(7, ListNode(9, ListNode(10)))
    combined_list_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10))))))))))

    assert compare_lists(list_1_1, list_1_1)
    assert not compare_lists(list_1_2, list_1_1)

    assert compare_lists(mergeKLists([list_1_1, list_1_2, list_1_3]), combined_list_1)

    list_2_1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
    list_2_2 = ListNode(3)
    combined_list_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert compare_lists(mergeKLists([list_2_1, list_2_2]), combined_list_2)

    combined_list_3 = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(4, ListNode(5, ListNode(5))))))))
    assert compare_lists(mergeKLists([list_1_1, list_1_1]), combined_list_3)


