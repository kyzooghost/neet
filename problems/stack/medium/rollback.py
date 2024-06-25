# Create a data structure with the following interface:
# It is possible to insert the same integer multiple time.
# It does not need to support forward rollback.

# ? Solution with set and bitmap
# Unsure - you can implement a set with a bitmap, unsure about using both

# Lesson 1 - Missed `checkpoint < 0` edge case
# Lesson 2 - Can use len(self.stack) rather than self.time(int) variable
# Lesson 3 - Come up with your own test cases

'''
public interface Datastructure { 
    void Insert(int number)  
    bool IsContain(int number)
    Checkpoint CreateCheckpoint() 
    void Rollback(Checkpoint)}
'''

from collections import defaultdict

class DataStructure:
    # O(N) space
    def __init__(self):
        self.counter = defaultdict(int)
        self.stack = []

    # O(1) time
    def insert(self, num):
        self.counter[num] += 1
        self.stack.append(num)

    # O(1) time
    def isContain(self, num):
        return self.counter[num] > 0

    # O(1) time
    def createCheckpoint(self):
        return len(self.stack)

    # O(N) time
    def rollback(self, checkpoint):
        if checkpoint >= len(self.stack): return
        # Forgot this edge case? It's acceptable because you can never get a negative number from 'createCheckpoint'
        if checkpoint < 0: return
        while checkpoint < len(self.stack):
            popped_num = self.stack.pop()
            self.counter[popped_num] -= 1

ds = DataStructure()
ds.insert(1)
checkpoint = ds.createCheckpoint()
ds.insert(2)
ds.rollback(checkpoint)
print(ds.isContain(1)) # true
print(ds.isContain(2)) #false

ds1 = DataStructure()
ds1.insert(1)
ds1.insert(2)
checkpoint = ds1.createCheckpoint()
ds1.insert(2)
ds1.rollback(checkpoint)
print(ds1.isContain(1)) # true
print(ds1.isContain(2)) # true
