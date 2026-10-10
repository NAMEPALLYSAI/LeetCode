class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        org=sorted(s)
        der=sorted(t)
        l=0
        r=0
        while l<len(org) and r<len(der):
            if len(org) != len(der) or org[l] != der[r]:
                return False
            elif org[l] == der[r]:
                l+=1
                r+=1
        return True
