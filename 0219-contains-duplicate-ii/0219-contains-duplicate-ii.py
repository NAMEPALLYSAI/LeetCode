class Solution:
    def containsNearbyDuplicate(self, n: list[int], k: int) -> bool:
        dici={}
        for idx,val in enumerate(n):
            if val in dici and idx - dici[val] <=k:
                return True
            else:
                dici[val] = idx
        return False
             


        