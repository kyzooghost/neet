# List for each key, with (timestamp, value)
# All timestamps of set are strictly increasing
# Ok done in 21 minutes - 18% runtime, 51% memory
# Use this property - 'All the timestamps timestamp of set are strictly increasing.' which enables binary search of timestamp
from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dict: return ""
        if timestamp < self.dict[key][0][0]: return ""
        # timestamp will be >= first timestamp recorded
        l, r = 0, len(self.dict[key]) - 1
        index = l

        while l <= r:
            mid = (l + r) // 2
            if self.dict[key][mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                index = max(index, mid)

        return self.dict[key][index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)