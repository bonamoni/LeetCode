class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        d = {}
        maxLen = 0
        left = 0
        right = 0
        while(right<n):
            #shrink
            if(s[right] in d and d[s[right]]>=left):
                left = d[s[right]]+1
            d[s[right]]=right
            maxLen = max(maxLen,right-left+1)
            right+=1
        return maxLen