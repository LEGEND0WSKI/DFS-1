# // Time Complexity :O(m*n) traversal and BFS
# // Space Complexity : O(m*n) matrix max queue 
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : Failed to code using Memoisation DFS


# // Your code here along with comments explaining your approach

# DFS w Memoisation issues//
# 2 pass possible
#BFS approach  with 0
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        m = len(mat)
        n = len(mat[0])

        q = deque()

        for i in range(m):                  # 0's in queue and 1s as -1 for visited
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        dist = 1
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for di in dirs:                                         # 4 directions
                    r = di[0] + curr[0]
                    c = di[1] + curr[1]

                    if 0 <= r < m and 0 <= c < n and mat[r][c] == -1:   # add to queue and update
                        mat[r][c] = dist
                        q.append((r,c))
            dist+=1

        return mat