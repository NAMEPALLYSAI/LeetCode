class Solution:
    def maxArea(self,n: list[int]) -> int:
        l=0
        r=len(n)-1
        maxArea=float('-inf')
        while l < r:
            d = r-l
            hei = min(n[l],n[r])
            a = d * hei
            maxArea = max(maxArea,a)

            if n[l] <= n[r]:
                l+=1
            else:
                r-=1
        return maxArea
        