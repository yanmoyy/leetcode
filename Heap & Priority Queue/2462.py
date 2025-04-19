# 2462. Total Cost to Hire K Workers

from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_heap, right_heap = [], []
        total_cost = 0
        left, right = 0, n - 1

        c = candidates
        while left < c:
            heapq.heappush(left_heap, costs[left])
            left += 1
        while right >= max(left, n - c):
            heapq.heappush(right_heap, costs[right])
            right -= 1

        def pop_left():
            nonlocal total_cost, left
            total_cost += heapq.heappop(left_heap)
            if left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1

        def pop_right():
            nonlocal total_cost, right
            total_cost += heapq.heappop(right_heap)
            if left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1

        for _ in range(k):
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    pop_left()
                else:
                    pop_right()
            elif left_heap:
                pop_left()
            elif right_heap:
                pop_right()

        return total_cost
