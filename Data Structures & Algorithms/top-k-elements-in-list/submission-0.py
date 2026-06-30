class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        minHeap=[]
        for ele, freq in freq_map.items():
            heapq.heappush(minHeap,(freq,ele))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return [element for frequency,element in minHeap]



        