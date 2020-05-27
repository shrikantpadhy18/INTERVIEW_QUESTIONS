class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=99999
        ps=0
        ls=[]
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k):
                su=nums[i]+nums[j]+nums[k]
                if(abs(su-target)==0):
                    return su
                if(abs(su-target)<ans):
                    ans=abs(su-target)
                    ps=su
                    
                if su>target:
                    k-=1
                if su<target:
                    j+=1
                    
                        
        return(ps)