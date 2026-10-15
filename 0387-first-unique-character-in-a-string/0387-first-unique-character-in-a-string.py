class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        for i in s:
            dici[i]=dici.get(i,0)+1
        
        for j in range(len(s)):
            if dici[s[j]] == 1:
                return j
        return -1      