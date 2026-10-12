class Solution:
    def groupAnagrams(self, s: list[str]) -> list[list[str]]:
        dici={}
        for i in s:
            news = "".join(sorted(i))
            if news not in dici:
                dici[news] =[]
            
            dici[news].append(i)
        return list(dici.values())
        