class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        
        for l in list(s):
            if l in dict:
                dict[l] += 1
            else:
                dict[l] = 1
        
        for l in list(t):
            if l not in dict:
                return False
            else:
                if dict[l] == 0:
                    return False
                dict[l] -= 1
        for value in dict.values():
            if value != 0:
                return False
        return True

# Time: O(s + t)
# Space: O(s + t)