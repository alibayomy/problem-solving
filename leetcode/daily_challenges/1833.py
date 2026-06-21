import heapq
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ice_creams = 0
        heapq.heapify(costs)
        while coins > 0 and costs:
            min_ice_cream = heapq.heappop(costs)
            coins -= min_ice_cream
            if coins < 0:
                break
            ice_creams += 1
        return ice_creams
costs = [1,3,2,4,1]
coins = 7
solution = Solution()
print(solution.maxIceCream(costs,coins))