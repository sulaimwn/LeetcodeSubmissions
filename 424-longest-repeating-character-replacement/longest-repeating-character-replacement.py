class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # this shows how many times each char appers inside a window
        char_counts = {}

        #length of the longest affordable window, our output
        longest_window =0

        #left edge of window
        left = 0

        #highest count any single character has ever reached in a window.
        #its never decreased even when the window shrinks
        highest_count_seen =0


        for right in range(len(s)):

            #this is the current char being handled. 
            incoming_char = s[right]

            #this is used to add to char_counts.  increment its value OR add it in
            char_counts[incoming_char] = char_counts.get(incoming_char, 0) + 1



            #we check to see if the char we just added is the highest single character seen in a window

            highest_count_seen = max(highest_count_seen, char_counts[incoming_char])




            #this loop is used to ensure the window is affordable. if the window isnt affordable and k cant account for all the changes needed to make it 1 single char, it moves the L until the window is small enough so it can

            #eventhough its weird that highest_count_seen doesnt adjust for the window. It doest matter becauseee ...... if the current window isnt larger than our best answer so far than it doesnt matter anyway
            # AABA 1k  Valid   highestcount 3  sends a longestwindow of 4
            # AABAB  >k
            # ABAB   thats valid even tho its not . but it only sends a window of 4
            # ABABA   moves left 
            # BABA   sends window of 4 even tho its not valid. but it doesnt matter
            # BABAA Moves left
            # ABAAA  thats 5-4 !>k  send window of 5
            # ABAAAA 6-5!>k sends window of 6 .. etc
            # the window can only grow if highest_count_seen goes up.
            while(right-left+1)-highest_count_seen >k:
                outgoing_char=s[left]
                char_counts[outgoing_char] -=1
                left+=1
            
            #now we know this ccurent widnow on hand is affordable. so we check to see if it can be our output
            longest_window=max(longest_window, right-left+1)
        
        return longest_window

        