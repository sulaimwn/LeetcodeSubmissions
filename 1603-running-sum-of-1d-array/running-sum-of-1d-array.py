class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arrayt = []
        total =0
        for i in range(len(nums)):
            total+=nums[i]
            arrayt.append(total)

        return arrayt