class Solution:
    def topKFrequent(self, n: list[int], k: int) -> list[int]:
        dici={}
        for i in n:
            if i not in dici:
                dici[i] = 1
            else:
                dici[i]+=1
        res = sorted(dici,key=dici.get,reverse=True)
        return res[:k]
        
        
        