# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr=[]
        while(head is not None):
            arr.append(head.val)
            head=head.next
        if(arr==arr[::-1]):
            return True 
        else:
            return False
            
            
