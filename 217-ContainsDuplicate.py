class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_sort = sorted(nums)
        for i in range(len(new_sort) - 1):
            if new_sort[i] == new_sort[i + 1]:
                return True
        return False

# Time: O(n)
# Space: O(1)
# Notes: can use a hashmap (better time efficiency, space becomes o(n))for another solution