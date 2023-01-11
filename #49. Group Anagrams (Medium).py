class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         #49. Group Anagrams (Medium)

        ans = collections.defaultdict(list) #we map charcount to the list of anagrams
        # for ex ant and tan have the same list of characters a, n and t so we use this as a key 
        # and the n we use the list of anagrams as the value

        for s in strs:
            count = [0] * 26# for a ... z

            for c in s:
                #here we are mapping the lowercase letters from 0 and not their ASCII value
                count[ord(c) - ord("a")] += 1 #so to get the value of c from 0 we subtract the ASCII value of "a" from it
            ans[tuple(count)].append(s)
        return ans.values()
