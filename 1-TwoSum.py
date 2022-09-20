class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        final = []
        
        for index, num in enumerate(nums):
            check = target - num
            if check in dict:
                final.append(dict[check])
                final.append(index)
                return final
            else:    
                dict[num] = index
        
        # Time = O(n), since it only goes through the list once
        # Space = O(n), since it will have to hold a hashmap/dict