class Solution:
    def productExceptSelf(self, n: list[int]) -> list[int]:
        res = [1] * len(n)

        lp = 1
        for i in range(len(n)):
            res[i] = lp
            lp *= n[i]

        rp = 1
        for i in range(len(n) - 1, -1, -1):
            res[i] *= rp
            rp *= n[i]

 
        return res
 

         
        