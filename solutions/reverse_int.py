class Solution(object):
    def reverse(self, x):
        x = str(x)[::-1]
        if "-" in x:
            x = x.replace("-", "")
            x = "-" + x
        if int(x) > 2**31 or int(x) < -2**31:
            # prevent large numbers
            return 0
        return int(x)