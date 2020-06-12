class Solution:
    def canCross(self, stones: List[int]) -> bool:
        denoter=[]
        
        if len(stones)==2:
            return(stones[0]+1==stones[1])
            
        else:
            for k in range(1,len(stones)-1):
                lastindex=len(stones)-k-1
                jump=stones[len(stones)-1]-stones[lastindex]
                for j in range(lastindex-1,0,-1):
                    if stones[j]+jump==stones[lastindex]:
                        lastindex=j

                    elif(stones[j]+jump+1==stones[lastindex]):
                        lastindex=j
                        jump=jump+1

                    elif(stones[j]+jump-1==stones[lastindex]):
                        lastindex=j
                        jump=jump-1
                
                denoter.append([lastindex,jump])
            
            for p in denoter:
                
                if p[0]==1 and (stones[0]+p[1]==stones[1] or stones[0]+p[1]+1==stones[1] or stones[0]+p[1]-1==stones[1]):    
                    return True
                                
            return False
            
            
