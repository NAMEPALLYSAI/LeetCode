class Solution:
    def numRescueBoats(self, n: list[int], limit: int) -> int:
        n.sort()
        l=0
        r=len(n)-1
        count=0
        while l <= r:
            if n[l] + n[r] == limit or n[l] + n[r] < limit :
                count+=1
                l+=1
                r-=1
            elif n[r] > limit or n[l] + n[r] > limit:
                count+=1
                r-=1
            elif n[r] == n[l] :
                count+=1
                r-=1
        return count

         