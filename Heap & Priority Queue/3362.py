import heapq


class Solution(object):
    def maxRemoval(self, nums, queries):
        queries.sort(key=lambda x: x[0])
        available = []
        assigned = []
        count = 0
        k = 0
        for i in range(len(nums)):
            while assigned and assigned[0] < i:
                heapq.heappop(assigned)
            while k < len(queries) and queries[k][0] <= i:
                heapq.heappush(available, -queries[k][1])
                k += 1
            while len(assigned) < nums[i] and available and -available[0] >= i:
                heapq.heappush(assigned, -heapq.heappop(available))
                count += 1
            if len(assigned) < nums[i]:
                return -1
        return len(queries) - count
