# python dont have maxheap, use minheap instead
# convert each value into negative
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones] 
        heapq.heapify(stone) #change list into minheap

        while len(stone) > 1:
            first = heapq.heappop(stone)
            second = heapq.heappop(stone)
            if second > first:
                heapq.heappush(stone, first - second)
        stone.append(0) # in case that there is no stone left
        return abs(stone[0])
