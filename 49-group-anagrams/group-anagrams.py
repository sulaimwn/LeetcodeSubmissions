class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = defaultdict(list)
        #a dictionary that automatically creates empty lists if key doesnt exist
        for word in strs:
            letter_counts = [0]*26
            # list of 26 zeroes
            for character in word:
                letter_index = ord(character) - ord("a")
                #ascii indexing for each character

                letter_counts[letter_index] += 1
                #increase count for character at its index in the big list if its seen

            frequency_key = tuple(letter_counts)
            #make the frequency letter key a tuple so it works as dict keys
            anagram_groups[frequency_key].append(word)
            #add the current word to the group with the same frequency letter key

        grouped_words = list(anagram_groups.values())
        #Convert the list of sorted words based off frequencyletterkey 
        return grouped_words

        