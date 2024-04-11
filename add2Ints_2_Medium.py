class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def value_of_llist(self,llist):
        num = i = 0
        node = llist

        while node:
            v= node.val
            print("v={}".format(v))
            num += v*(10**i)
            i+=1
            node = node.next
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=n2=i=0

        n1=self.value_of_llist(l1)
        n2=self.value_of_llist(l2)
       
        total=n1+n2

        print("n1={}; n2={}; total={}".format(n1,n2,total))
