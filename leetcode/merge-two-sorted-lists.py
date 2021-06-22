# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(-1)
        cursor=head
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cursor.next = l1
                l1=l1.next
            else:
                cursor.next = l2
                l2=l2.next
                
            cursor = cursor.next
            
        if l1 != None:
            cursor.next = l1
        else:
            cursor.next = l2
            
        return head.next
        
        