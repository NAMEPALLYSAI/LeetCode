class Solution:
    def threeSum(self, n: list[int]) -> list[list[int]]:
        n.sort()
        i=0
        res=[]
        while i < len(n)-2:
            if i>0 and n[i] == n[i-1]:
                i+=1
                continue
            j=i+1
            k=len(n)-1
            while j < k:
                if n[i] + n[j] + n[k] == 0:
                    res.append([n[i],n[j],n[k]])
                    j+=1
                    k-=1
                    while j <k and n[j] == n[j-1]:
                        j+=1
                    while j<k and n[k] == n[k+1]:
                        k-=1

                elif n[i] + n[j] + n[k] < 0:
                    j+=1
                else:
                    k-=1
            i+=1
        return res
                







         