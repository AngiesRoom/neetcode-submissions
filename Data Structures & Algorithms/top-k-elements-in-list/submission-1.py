class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        n = len(nums)
        freq = [[] for i in range(n + 1)]

        for x, c in hashmap.items():
            freq[c].append(x)

        res = []

        for l in range(len(freq) -1, 0, -1):
            for z in freq[l]:
                res.append(z)
                if len(res) == k:
                    return res