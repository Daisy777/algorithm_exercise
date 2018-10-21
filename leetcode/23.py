# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         first_node = None
#         current_location = None
#         # pointers to node in each list
#         pointers = [x[0] for x in lists]

#         while any(pointers):
#             # remove none val in time
#             min_index = pointers.index(min(pointers, key = lambda x: x.value))

#             if not first_node:
#                 first_node = pointers[min_index]
#                 current_location = first_node
#             else:
#                 node = pointers[min_index]
#                 current_location.next = node
#                 if node.next:
#                     pointers[min_index] = node.next 
#                 else:
#                     pointers.pop(min_index)
                
#                 current_location = current_location.next

#         return first_node

# Time Limit Exceeded

    