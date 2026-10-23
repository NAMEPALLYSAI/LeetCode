class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x=str(x)
            if x[:] == x[-1::-1]:
                return True
        return False 
        