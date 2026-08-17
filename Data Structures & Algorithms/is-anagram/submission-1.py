class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset_s = set()
        hashset_t = set()
        hashset_s.add(s)
        hashset_t.add(t)
        if sorted(s) == sorted(t):
            return True
        return False