class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = defaultdict(int)
        output_list = []
        for num in nums:
            frequency_table[num] += 1
        
        for i in range(k):
            high = max(frequency_table, key=frequency_table.get)
            output_list.append(high)
            del frequency_table[high]
        
        return output_list