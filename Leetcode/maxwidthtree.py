class Solution:
    def widthOfBinaryTree(self, root):
        if(root==None):
            return 0
        else:
            queue=[]
            queue.append([root,0])
            maxwidth=0
            while(queue!=[]):
                
                ct=len(queue)
                
                first=queue[0]
                while(ct!=0):
                    second=queue.pop(0)
                    if(second[0].left!=None):
                        queue.append([second[0].left,2*second[1]])
                    if(second[0].right!=None):
                        queue.append([second[0].right,2*second[1]+1])
                    ct-=1
                    
                
                maxwidth=max(maxwidth,second[1]-first[1]+1)
            return maxwidth