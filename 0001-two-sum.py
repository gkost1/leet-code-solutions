class Solution(object):
    """
    The naive approach would be to double for-loop, checking each number, in the outer for loop, then checking its complement exists in the inner for-loop.

    However, by leveraging the use of a dictionary (hash map), we can hash the index of each number with the number it self. Then, later in the list, if we see 
    the complement of the current number is already in our list, then we can return the indexes immediately. Otherwise, add the number to the map and continue.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[num] = i
        

