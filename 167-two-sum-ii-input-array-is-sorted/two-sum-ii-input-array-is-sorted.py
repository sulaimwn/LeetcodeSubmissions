class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer=0 # start of array
        right_pointer = len(numbers)-1  #end of array
        while left_pointer < right_pointer: # keep cchecking till the two pointers meet

            # getting value @ the pointers
            left_value = numbers[left_pointer] 
            right_value = numbers[right_pointer]

            #add em
            current_sum = left_value + right_value

            #if the sum is too big decrease the larger value
            if current_sum > target:
                right_pointer -= 1
            #if the sum is too small increase the smaller value
            elif current_sum < target:
                left_pointer+=1

            else:
                return[left_pointer+1,right_pointer+1]
            #if its the same value the return the pos
            # for some reason its 1 index thats why theres +1
        