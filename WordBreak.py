class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [-1 for _ in range(len(s))]
        def wordbreak(string, index):
            if index == len(string):
                return True
            
            if not memo[index] == -1:
                return memo[index]
            
            for i in range(index+1, len(string)+1):
                if string[index:i] in wordDict and wordbreak(string, i):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
            
        return wordbreak(s, 0)
