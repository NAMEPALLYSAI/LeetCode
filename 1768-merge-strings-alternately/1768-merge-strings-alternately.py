class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l=0
        r=0
        res=[]
        while l < len(w1) and r < len(w2):
            res.append(w1[l])
            l+=1
            res.append(w2[r])
            r+=1
        while l < len(w1):
            res.append(w1[l])
            l+=1
        while r < len(w2):
            res.append(w2[r])
            r+=1
        res=''.join(res)
        return res