class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        dict2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 0
            else:
                dict[s[i]] += 1
            if t[i] not in dict2:
                dict2[t[i]] = 0
            else:
                dict2[t[i]] += 1    
        return True if dict == dict2 else False
