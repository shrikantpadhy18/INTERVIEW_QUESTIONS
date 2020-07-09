class Solution:
    def coiner(self,coins,amt,dp):
        
        if(amt<0):
            dp[amt]=9999
            return 9999
        elif(amt==0):
            dp[amt]=0
            return 0
        
        
        
        if(dp.get(amt,None)!=None):
            return dp[amt]
        ans=9999
        for i in coins:
            ans=min(ans,1+self.coiner(coins,amt-i,dp))
        #print(ans)
        dp[amt]=ans
        return ans
            
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=dict()
        ans=self.coiner(coins,amount,dp)
        if(ans==9999):
            return -1
        else:

            return ans