# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):

    # Syntax for reverse array in Python - list[::-1]

    # Cool, done in under 12 minutes
    # 65% runtime, 77% memory
    # Two pointers from both ends of the string
    # Syntax lessons - string.isalum() and string.lower()
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        def isalum_custom(char):
            if ord("A") <= ord(char) <= ord("Z"):
                return True 
            if ord("a") <= ord(char) <= ord("z"):
                return True 
            if ord("0") <= ord(char) <= ord("9"):
                return True 
            return False

        pointer = 0
        reverse_pointer = length - 1

        while pointer < reverse_pointer:
            # Remove all non-alphanumeric from consideration
            if isalum_custom(s[pointer]) == False:
                pointer += 1
            elif isalum_custom(s[reverse_pointer]) == False:
                reverse_pointer -= 1
            # If both pointers are alphanumeric, do the comparison
            else:
                if s[pointer].lower() == s[reverse_pointer].lower():
                    pointer += 1
                    reverse_pointer -= 1
                else:
                    return False

        return True


    

        
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
