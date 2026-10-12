class Solution:
    def removeDuplicates(self, n: list[int]) -> int:
        if len(n) <= 2:
            return len(n)

        l = 2
        r = 2

        while r < len(n):
            if n[r] != n[l - 2]:
                n[l] = n[r]
                l += 1

            r += 1

        return l
 

        