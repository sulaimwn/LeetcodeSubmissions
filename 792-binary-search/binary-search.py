class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        dont do this
         for i,v in enumerate(nums):
            if nums[i] == target:
                return i
        if target not in nums:
            return -1
        """

        left=0 #left index
        right=len(nums)-1 # right index

        #keep going while window has atleast 1 element

        while left<= right:
            middle=(left+right)//2  # floor div

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                 # middle is too small so look at everthing right of middle
                left = middle+1
            else:
                #middle is too big. look at everything left of middle
                right=middle-1
        return -1