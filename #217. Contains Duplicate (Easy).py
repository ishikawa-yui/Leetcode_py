class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #initialization of hashset
        #insert all traversed values in the hasshset
        #and then keep comparing the next value with the values already in the hashset

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n) #only add when value not in hashmap

        return False

        #TIME : O(n)
        #SPACE : O(n)