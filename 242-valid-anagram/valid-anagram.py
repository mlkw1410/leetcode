class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset = {}
        for n in s:
            hashset[n] = hashset.get(n, 0)+1
        for n in t:
            if n in hashset:
                hashset[n] -=1
                if hashset[n]==0:
                    del hashset[n]
        return len(hashset) == 0            