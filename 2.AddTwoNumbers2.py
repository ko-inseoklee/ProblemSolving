class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = 0
        tenary = 1
        while True:
            num1 += int(l1.val) * tenary
            tenary = tenary * 10
            if l1.next == None:
                break
            else:
                l1 = l1.next
        
        num2 = 0
        tenary = 1
        while True:
            num2 += int(l2.val) * tenary
            tenary = tenary * 10
            if l2.next == None:
                break
            else:
                l2 = l2.next
                
        snum = num1 + num2
        init_val = snum % 10
        
        result = ListNode(init_val,None)
        temp = result
        snum = snum // 10
        while snum != 0:
            temp.next = ListNode(0,None)
            temp = temp.next
            temp.val = snum % 10
            snum = snum // 10
            
        return result