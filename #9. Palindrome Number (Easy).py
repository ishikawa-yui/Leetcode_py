class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 9. Palindrome Number (Easy)
        
        sum = 0
        temp = x
        while(x>0):
            r = x % 10 # here r stores the remainder
            sum = (sum * 10) + r 
            x = x // 10

        if(temp == sum):
            return True
        else:
            return False
