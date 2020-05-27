class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ps=[]
        leftmost=0
        if(len(matrix)>0):
            rightmost=len(matrix[0])-1

            top=0
            col=len(matrix[0])
            bottom=len(matrix)-1

            r=0
            c=0
            while(leftmost<=rightmost and top<=bottom):

                for i in range(leftmost,rightmost+1):
                    print((r,i),end=" ")
                    if(leftmost<=rightmost and top<=bottom):
                        ps.append(matrix[r][i])
                    c=i

                top+=1

                for j in range(top,bottom+1):
                    print((j,c),end=" ")
                    if(leftmost<=rightmost and top<=bottom):
                        ps.append(matrix[j][c])
                    r=j


                rightmost-=1

                for s in range(rightmost,leftmost-1,-1):
                    print((r,s),end=" ")
                    if(leftmost<=rightmost and top<=bottom):
                        ps.append(matrix[r][s])

                    c=s

                bottom-=1

                for d in range(bottom,top-1,-1):
                    print((d,c),end=" ")
                    if(leftmost<=rightmost and top<=bottom):
                        ps.append(matrix[d][c])
                    r=d

                leftmost+=1

            
        
        
        return ps