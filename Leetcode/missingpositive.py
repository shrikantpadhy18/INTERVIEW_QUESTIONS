class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(filter(lambda n:n>0,nums))
        if list(nums)==[]:
            return 1
        elif(len(list(nums))==1):
            if list(nums)[0]==0 or list(nums)[0]>1:
                return 1
            else:
                return list(nums)[0]+1
        else:
            
            
            ps=1
            print(ps)
            if list(nums)[0]>1:
                return 1
            while(ps<=list(nums)[-1]):
                if ps not in nums:
                    return ps
                ps+=1

            return max(nums)+1