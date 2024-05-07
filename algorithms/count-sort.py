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

        # O(N)
        for i in range(len(s)):
            s_ascii = ord(s)
            s_ascii_list.append(s_ascii)
            if s_ascii > s_ascii_max:
                s_ascii_max = s_ascii
        
        # Create count array
        count_array = [0] * (s_ascii_max + 1)

        # Populate count array
        for i in range(len(s_ascii_list)):
            ascii = s_ascii_list[i]
            count_array[ascii] += 1
        
        # Convert count array into cumulative counts
        cumulative_count = 0
        for i in range(len(s_ascii_list)):
            cumulative_count += count_array[i]
            count_array[i] = cumulative_count
        
        # Create out array
        out_array = [0] * len(s)

        # TODO - s_ascii_list -> sorted out_array, using count_array 
        # print(cumulative_count)
