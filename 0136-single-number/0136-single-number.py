class Solution:
    def singleNumber(self, n: list[int]) -> int:
        xor=0
        for i in n:
            xor^=i
        return xor
         
        