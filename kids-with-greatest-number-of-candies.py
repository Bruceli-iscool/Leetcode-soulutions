class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        for f in range(len(candies)):
            z = candies[f] + extraCandies
            x = 0
            for g in range(len(candies)):
                if candies[g] > z:
                    ans.append(False)
                    x = 1
                    break
            if x == 1:
                continue
            else:
                ans.append(True)


        return ans
        
