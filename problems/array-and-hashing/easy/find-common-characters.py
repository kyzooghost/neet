class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {}
        for char in words[0]:
            dict[char] = dict.get(char, 0) + 1
        
        for i in range(1, len(words)):
            word = words[i]
            tmp_dict = {}
            for char in word:
                tmp_dict[char] = tmp_dict.get(char, 0) + 1

            for char in dict.keys():
                if char not in tmp_dict:
                    del dict[char]
                else:
                    dict[char] = min(dict[char], tmp_dict[char])

        resp = []
        for char in dict.keys():
            for i in range(dict[char]):
                resp.append(char)
        return resp
