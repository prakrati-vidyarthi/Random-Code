class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
          return 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        max_val = 0
        for i in range(m):
          for j in range(n):
            if matrix[i][j] == "0":
              dp[i][j] = 0
              continue
              
            if not (i>0 and j>0):
              dp[i][j] = int(matrix[i][j])
              max_val = max(max_val, dp[i][j])
              continue
              
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            max_val = max(dp[i][j], max_val)
            
        return max_val * max_val
                          
