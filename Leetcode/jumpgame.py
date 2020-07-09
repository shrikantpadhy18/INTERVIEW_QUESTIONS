class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex=len(nums)-1
        
        if(len(nums)==1):
            return True
        
        for j in range(lastindex-1,-1,-1):
            data=nums[j]
            if(data+j>=lastindex):
                lastindex=j
        print(lastindex)          
        if((lastindex==1 and nums[0]>=1) or lastindex==0):
            return True
        else:
            return False
        