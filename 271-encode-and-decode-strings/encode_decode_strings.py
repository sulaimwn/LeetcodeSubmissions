class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + '#' + word
        #length, then a marker (#) then the word itself
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        while start < len(s):
            #traverse till we find # after length
            marker = start
            while s[marker] != "#":
                marker += 1
            length = int(s[start:marker]) #first length

            word_start = marker+1; #the word starts after the first hashtag
            word_end = word_start + length
            result.append(s[word_start:word_end])
            
            start = word_end #jump to next

        return result
