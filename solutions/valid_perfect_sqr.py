class Solution(object):
    def isPerfectSquare(self, num):
        x = num**0.5
        z, y = str(x).split(".")
        y = int(y)
        if y != 0:
            return False
        else:
            return True