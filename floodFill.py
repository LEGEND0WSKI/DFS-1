# // Time Complexity :O(m*n) for every node
# // Space Complexity :O(m*n) for recursion worst case all elements
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : DFS improper boundary condition
# i<0 or i==m , we can use OR
# 0 <i <m we use and

# // Your code here along with comments explaining your approach

#DFS
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        oldColor = image[sr][sc]                            # find oldcolor index
        if oldColor == color:                               # compare
            return image
        self.dfs(image,sr,sc,oldColor,color,m,n)            # recursion main
        return image

    def dfs(self,image,i,j,oldColor,color,m,n):
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        if 0 <= i < m and 0 <= j < n and image[i][j] == oldColor: # inbounds
            image[i][j] = color                                   # change color

            for di in dirs:
                r = i + di[0]
                c = j + di[1]
                
                self.dfs(image,r,c,oldColor,color,m,n)            # 4 x recursion dfs
        else:                                                     # out of bounds
            return

#BFS
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        m = len(image)
        n = len(image[0])

        oldColor = image[sr][sc]
        if oldColor == color:
            return image

        q = deque()
        q.append(sr)                                                    # row in queue
        q.append(sc)                                                    # colmn in queue
        image[sr][sc] = color

        while q:
            r = q.popleft()                                             # popped row
            c = q.popleft()                                             # popped column 

            for di in dirs:
                nr = r + di[0]
                nc = c + di[1]
                
                if 0 <= nr <m and 0<= nc <n and image[nr][nc] == oldColor:
                    image[nr][nc] = color
                    q.append(nr)
                    q.append(nc)
        
        return image