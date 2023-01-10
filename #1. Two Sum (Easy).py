class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Two Sum (Easy)

        prevmap = {} #hashmap following val : index entry

        #we traverse thru the array and keep adding the visited elements in the hashmap

        for i, n in enumerate(nums):
            diff = target - n #to get the only number we need from the array
            if diff in prevmap:
                return [prevmap[diff], i] #return the index of the elements that add up to
                                          #the value
            prevmap[n] = i  #if sol not found then update the hashmap
        return ":)"
