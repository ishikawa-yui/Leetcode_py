class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #242. Valid Anagram
        
        if len(s) != len(t):
            return False #as we no longer need to check whether it is an anagram
        
        #initialization of hashmaps:
        # key == char, value == number of occurences
        countS , countT = {}, {}

        for i in range(len(s)):
            #go thru the length of the strings at the same time use the size of the string (s or t)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            #here we use the get function as the first character may not even exist in the hashmap yet and in the get function you can set default value as 0.
            
            # here we are forming the hashmaps
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True