# https://www.geeksforgeeks.org/counting-sort/
# https://www.youtube.com/watch?v=7zuGmKfUt7s

# Use for string sort, O(M + N) where M is # of input characters
class Solution(object):
    def stringSort(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_ascii_list = []
        s_ascii_max = 0
        s_ascii_min = 1000000
        s_length = len(s)

        # O(N) - Cast str into ascii code
        for i in range(s_length):
            s_ascii = ord(s[i])
            s_ascii_list.append(s_ascii)
            if s_ascii > s_ascii_max:
                s_ascii_max = s_ascii
            if s_ascii < s_ascii_min:
                s_ascii_min = s_ascii

        # O(N) Move ascii numbers from [s_ascii_min, s_ascii_max] to [0, s_ascii_max - ascii_range]
        # Space and time benefit to reduce M from s_ascii_max to 's_ascii_max - ascii_range'
        for i in range(s_length):
            s_ascii_list[i] -= s_ascii_min

        # Create count array - O(M) space
        ascii_range = s_ascii_max - s_ascii_min
        count_array = [0] * (ascii_range + 1)

        # Populate count array - O(N) time
        for i in range(len(s_ascii_list)):
            ascii = s_ascii_list[i]
            count_array[ascii] += 1
        
        # Convert count array into cumulative counts - O(M) time
        cumulative_count = 0
        for i in range(len(count_array)):
            cumulative_count += count_array[i]
            count_array[i] = cumulative_count
        
        # O(N) space - Create out array
        out_array = [0] * s_length

        # O(N) time - Iterate from back of original string, to populate out_array
        for i in range(s_length):
            char_ascii = s_ascii_list[s_length - i - 1]
            out_array_index = count_array[char_ascii] - 1
            # Update count_array
            count_array[char_ascii] = out_array_index
            # cast ascii back to original, insert into out_array
            original_char = chr(char_ascii + s_ascii_min)
            out_array[out_array_index] = original_char

        return ''.join(out_array)

solution = Solution()
print(solution.stringSort("zlnoafiwfwanfja"))