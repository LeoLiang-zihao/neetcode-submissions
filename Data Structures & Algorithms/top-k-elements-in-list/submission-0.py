class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num , c in count.items():
            freq[c].append(num)

        res = []

        for c in range(len(nums), 0 , -1):
            for num in freq[c]:
                res.append(num)

                if len(res) == k:
                    return res
            