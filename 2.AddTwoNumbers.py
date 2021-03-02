# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0,None)
        num1 = l1.val
        num2 = l2.val
        nextNum = 0
        temp.val = (num1 + num2 + nextNum) % 10
        nextNum = (num1 + num2 + nextNum) // 10
        result = temp
        while(l1.next != None or l2.next != None or nextNum != 0):
            temp.next = ListNode(0,None)
            temp = temp.next
            if(l1.next == None):
                num1 = 0
            else:
                l1 = l1.next
                num1 = l1.val
            if(l2.next == None):
                num2 = 0
            else:
                l2 = l2.next
                num2 = l2.val
            temp.val = (num1 + num2 + nextNum) % 10
            nextNum = (num1 + num2 + nextNum) // 10
        return result
        
