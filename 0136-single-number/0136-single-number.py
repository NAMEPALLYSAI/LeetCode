class Solution:
    def singleNumber(self, n: list[int]) -> int:
        dici={}
        for i in n:
            dici[i] = dici.get(i,0)+1
        for i in n:
            if dici[i] == 1:
                return i
        