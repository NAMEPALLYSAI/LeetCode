class Solution:
    def maxOperations(self, n: List[int], k: int) -> int:
        n.sort()
        l=0
        r=len(n)-1
        count=0
        while l < r:
            if n[l] + n[r] == k:
                count+=1
                l+=1
                r-=1
            elif n[l] + n[r] > k:
                r-=1
            else:
                l+=1
        return count
        