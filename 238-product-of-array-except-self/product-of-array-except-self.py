class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [1] * n
        # an array filled with 1s

        product_of_everything_left = 1

        for i in range(n):
            #write it in before updating. pos0 is always 1

            answer[i] = product_of_everything_left
            
            product_of_everything_left *= nums[i]
            #then after u multiply by the next pos. for the next var
            # nums    = [1, 2, 3, 4]
            # answer  = [1, 1, 2, 6]

        product_of_everything_right = 1
        #nothings right of index so it starts at 1

         # range(n-1, -1, -1) is start, stop, step: begin at the last index,
         # count down by 1, stop BEFORE -1 — so index 0 is still included.
        for i in range(n-1,-1,-1):
            #same ordering but mirrored on right pass
            answer[i] *= product_of_everything_right
            #on first pass just multiply by 1, but then the multiplier multiplies by the next value

            product_of_everything_right *= nums[i]

        return answer