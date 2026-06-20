class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        for c in alphabets:
            if s.count(c) != t.count(c):
                return False
        return True