class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        length=0
        while(temp!=None):
            temp=temp.next
            length+=1
        
        print(length)
        reqd=length-n
        if reqd==0:
            if length==1:
                return None
            else:
                return head.next
        else:
            
            pt=head
            behind=None
            while(reqd!=0):
                behind=pt
                pt=pt.next
                reqd-=1

            adder=pt.next
            behind.next=adder
            return head