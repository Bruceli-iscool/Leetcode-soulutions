class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        s.reverse()
        n = ""
        for k in s:
            n = n + k
        if n == str(x):
            return True
        else:
            return False
