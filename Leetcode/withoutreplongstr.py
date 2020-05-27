class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = ''
        l = 0
        for c in s:
            if c in ls:
                if len(ls) > l:
                    l = len(ls)
                ls = ls[ls.index(c)+1:]
                #print(ls)
            ls+=c
            #print(ls)
        if len(ls) > l:
            l = len(ls)
        return l