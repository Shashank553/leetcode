'''Simple Logic
left = 0 → Starting character.
right = len(s)-1 → Last character.
isalnum() → Check if it's a letter or number.
not isalnum() → If it's a space or special character, skip it.
lower() → Converts both characters to lowercase, so 'A' and 'a' become the same.
If characters are different → False.
If the loop completes without mismatch → True.'''
#simple solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        while left<right:
            #skip special characters from  right
            while left<right and not s[left].isalnum():
                left +=1

            #skip special characters from right
            while left<right and not s[right].isalnum():
                right -=1

            #compare characters(ignore uppercase/lowercase)
            if s[left].lower() !=s[right].lower():
                return False

            #compare both pointers
            left=left+1
            right=right-1

        return True