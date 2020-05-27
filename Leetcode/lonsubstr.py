class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        
        ans=0
        result= ""
        for i in range(0,len(s)):
            j=len(s)-1
            while(j>=i and j>=0):
                k=s[i:j+1]
                
                if(k==k[::-1] and len(k)>ans):
                    result=k
                    ans=len(k)
                
                j-=1
           
       
        return result
        
        
        
        