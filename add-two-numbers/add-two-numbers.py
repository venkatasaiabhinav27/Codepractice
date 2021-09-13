# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp=None
        curr=l1
        list = None
        while(curr or l2):
            node=ListNode()
            if(curr and l2):
                val = curr.val + l2.val + carry
                carry = 0
                if(val>=10):
                    node.val=val%10
                    carry=1
                else:
                    node.val=val
                curr=curr.next
                l2=l2.next
            elif(curr):
                node.val=curr.val +carry
                carry=0
                if(node.val >=10):
                    node.val %=10
                    carry=1
                curr=curr.next
            else:
                node.val=l2.val +carry
                carry=0
                if(node.val >=10):
                    node.val %=10
                    carry=1                
                l2=l2.next
            if(list==None):
                list=node
            else:
                temp2 = list
                while(temp2):
                    if(temp2.next==None):                        
                        temp2.next=node
                        break
                    temp2=temp2.next
        
        if(carry==1):
            node=ListNode(1)
            temp2 = list
            while(temp2):
                if(temp2.next==None):                        
                    temp2.next=node
                    break
                temp2=temp2.next
        return list        
        prev=None
        curr=list
        while(curr.next):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr.next = prev
        return curr

            


                    
                    
                    
                    
        