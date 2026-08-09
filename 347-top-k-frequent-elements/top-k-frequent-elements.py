class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        total_slots = len(nums) # how many nums in input

        #a dictionary count of how many times each number appears
        times_seen = {}
        for number in nums:
            times_seen[number] = times_seen.get(number, 0) + 1
            #adding to the key's occurence


        #step 2
        #One empty list for each possible frequency
        # Max frequency = lenght of input
        # plus one to ignore 0 (max cant be 0)
        numbers_at_frequency = []
        for slot in range(total_slots + 1):
            numbers_at_frequency.append([])
            #append an empty list
        
        #drop each number into a slot matching its frequency
        for number, frequency in times_seen.items():
            numbers_at_frequency[frequency].append(number)

        #step 3
        # read from the slots in reverse
        # add to result list until result=k
        result= []
        for frequency in range(total_slots, 0, -1):
            for number in numbers_at_frequency[frequency]:
                result.append(number)
                if len(result) == k:
                    return result
        