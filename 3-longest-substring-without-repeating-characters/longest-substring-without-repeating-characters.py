class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Set stores characters currently inside our window
        # used to check duplicates
        charSet = set()

        #left side of our sliding window
        l=0

        #length of valid substring so far
        res=0


        #r right side of our sliding window
        for r in range(len(s)):
            
            #if s[r] is already in the window we have a duplicat character
            # so just remove it and move on
            while s[r] in charSet:
                charSet.remove(s[l])

                l+=1

            charSet.add(s[r])
            #now we know for sure s[r]  isnt duplicate so we can add to our window


            #this is used to decide the longest substring so far
            #r-l+1 is basically checking the current window length
            #plus one because both l and r included in substring
            res=max(res,r-l+1)

        #return the longest substring length found
        return res