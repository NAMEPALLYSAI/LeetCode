class Solution:
    def containsDuplicate(self, n: list[int]) -> bool:
        # return len(set(n)) != len(n)
        n.sort()
        l=0
        r=1
        while r <= len(n)-1:
            if n[l] == n[r]:
                return True
            else:
                r+=1
                l+=1
        return False


  