class Solution:
    def longestValidParentheses(self, s: str) -> int:
        h=[]
        if s=="":
            return 0
        for i in range(len(s)):
            for j in range(len(s)-1,i-1,-1):
                #print(s[i:j+1])
                m=s[i:j+1]
                ls=[]
                ans=0
                for p in m:
                    if p=="(":
                        ls.append(p)
                    else:
                        if(ls==[]):
                            ans=1
                            break
                            
                        else:
                            ls.pop(-1)
                            
                            
                if(ls==[] and ans!=1):
                    h.append(len(m))
                            
        print(h)  
        if h!=[]:
            return max(h)                    
        else:
            return 0