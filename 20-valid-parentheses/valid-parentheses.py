class Solution:
    def isValid(self, s: str) -> bool:
        # lookup table. Keys are the closing brackets while values are opening
        # allows u to lookup a closer brackets opening 
        hashmap = {')':'(', '}':'{', ']':'['}
        
        #The stack , a normal python list
        # Last in, first out
        #we only touch its end via append or pop
        stk = []

        #for char in string
        for c in s:

            if c not in hashmap:
                #if our current char is an opener, add it to the stack
                stk.append(c)
            else:
                #if we're dealing with a closing bracket

                if not stk:
                    #closing bracket with no opener is invalid
                    return False
                else:

                    #removve the last item on our stack 
                    popped=stk.pop()

                    #but if the value we just removed isn't its corrensponding closer then we're likely dealing witha incorrectly nested bracket so we return false
                    if popped != hashmap[c]:
                        return False
        
        #if the stack is empty return true 
        return not stk
