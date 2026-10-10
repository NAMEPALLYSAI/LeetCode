class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l=0
        while l < len(n)-1:
            r=l+1

            while r < len(n):
                if n[l] + n[r] == target:
                    return [l,r]
                r+=1
            l+=1
             
        

         
        