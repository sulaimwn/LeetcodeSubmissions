class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        result = []

        nums.sort() # needed for the 2sum ii part

        for i, first in enumerate(nums):
            if i>0 and first==nums[i-1]:
                continue 
                # skip if the a value is equal to the prior
                #we already did it so js skip
                # also i>0 used to avoid grabbing a neg indexx

            #now try 2sum ii to get b and c values
            left=i+1
            right=len(nums)-1

            while left<right:
                current_sum=first+nums[left]+nums[right]
                # a,b, and c added
                if current_sum<0:
                    left+=1
                elif current_sum>0:
                    right-=1
                else:
                    #valid tripple found
                    result.append([first,nums[left],nums[right]])
                    
                    #regular left moving . keep going there might be more
                    left+=1


                    #skipping duplicate left values
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
        return result