class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create ans dict
        ans = defaultdict(list)

        # loop through each word
        for word in strs:
            # create a hashmap([0]x26)
            hmap = [0]*26
            # loop through each character
            for c in word:
                # get index of the character by using ord(a)-ord(character)
                # at the char index, increment the hashmap value by 1
                hmap[ord(c)-ord('a')]+=1
            
            ans[tuple(hmap)].append(word)
        # return a list of the values
        return list(ans.values())
