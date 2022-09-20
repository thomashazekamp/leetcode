class Solution:
    def isPalindrome(self, s: str) -> bool:
        palCheck = []
        for l in s.lower():
            if l.isalpha() or l.isdigit():
                palCheck.append(l)
        return palCheck == palCheck[::-1]
    # Time: O(n) since it only goes through the items once
    # Space: O(n) since we are using extra memory (list can also use a string instead)
    # Note: This is using built in functions