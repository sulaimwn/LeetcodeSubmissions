class MinStack:

    def __init__(self):
        #the actual stack of values we push
        self.values = []
        #a parallel stack of minimums. after each operations minimums[i] is the smallest value among values[0] through values [i] . these 2 lists have same length
        self.minimums=[]
        

    def push(self, value: int) -> None:
        self.values.append(value)

        #with this value on top, work wout what the minimum of the whole stack is now

        # if stack is empty. the new value is minimum by default
        #otherwise compare against prev minimums.

        if not self.minimums:
            minimum_including_new_value = value
        else:
            previous_minimum=self.minimums[-1]
            #-1 returns an arrays last value
            #-1 of minimums= values min
            minimum_including_new_value = min(value, previous_minimum)
        self.minimums.append(minimum_including_new_value)




    def pop(self) -> None:
        #remove from both stacks.
        self.values.pop()
        self.minimums.pop()



    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()