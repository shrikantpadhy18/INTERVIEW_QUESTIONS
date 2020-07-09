class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ps=[1]*(len(nums))
        print(ps)
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i] and ps[j]<ps[i]+1):
                    ps[j]=ps[i]+1
        if(ps==[]):
            return 0
        return(max(ps))
                    