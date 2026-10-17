class Solution:
    def kidsWithCandies(self, c: list[int], ec: int) -> list[bool]:
        higher=max(c)
        res=[]
        for i in c:
            if i+ec >= higher:
                res.append(True)
            else:
                res.append(False)
        return res
        