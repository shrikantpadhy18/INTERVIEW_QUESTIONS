# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        pt=head
        ct=0
        
        if head==None:
            return head
        while(pt!=None):
            pt=pt.next
            ct+=1
        
        frompos=ct-(k%ct)
        ls=[]
        dt=head
        kt=None
        ds=[]
        while(frompos!=0):
            kt=dt
            dt=dt.next
            frompos-=1
            ds.append(kt.val)
        
        
        ls=[]
        while(dt!=None):
            ls.append(dt.val)
            dt=dt.next
        print("ls",ls)
        print("ds",ds)
        ls.extend(ds)
        head.val=ls[0]
        pt=head.next
        for i in range(1,len(ls)):
            pt.val=ls[i]
            pt=pt.next
        return head
