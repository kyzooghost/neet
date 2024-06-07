# target must be >0
# position[i] must be < target
# speed must be > 0

# Just optimizing the space efficiency of Solution_V2
# 63% runtime, 51% memory
class Solution_V3(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 1: return 1
        # Sort - N lg N, O(N) space
        position_speeds = list(zip(position, speed))
        position_speeds.sort(key = lambda x: x[0], reverse=True)

        cur_time = float(target - position_speeds[0][0]) / float(position_speeds[0][1])
        resp = 1

        for i in range(1, len(position_speeds)):
            tmp_time = float(target - position_speeds[i][0]) / float(position_speeds[i][1])
            if tmp_time <= cur_time:
                continue
            else:
                resp += 1
                cur_time = tmp_time

        return resp

# Read one hint - don't use discrete approach but use time it takes for cars to reach the target
# Was able to solve in 15 minutes once I read the discussion hint (above)
# Ok got it 22% runtime, 38% memory
# Sigh, maintain a monotonically increasing stack of the completion time. Makes sense I guess
# I guess the key insight is that if you sort the cars by position in descending order, compute the time to get to the target, then car i that will take 7 seconds, will block the car i + 1 that will take 3 seconds, and you can merge the two
class Solution_V2(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 1: return 1
        # Sort - N lg N, O(N) space
        position_speeds = list(zip(position, speed))
        position_speeds.sort(key = lambda x: x[0], reverse=True)
        times = []
        for position, speed in position_speeds:
            times.append((target - position) / speed)
        print(times)
        # ? Maintain a monotonically decreasing stack
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
        return len(stack)



# Not sure how to solve this with a stack hmm
# First position - takes priority

# Keep track of all fleets at time
# If exceed, or meet at position, merge into 1 fleet with slower speed
# Dang 35 minutes, didn't come up with the solution. I think let's start again, this solution doesn't look like it will work
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 1: return 1
        # Sort - N lg N, O(N) space
        position_speeds = list(zip(position, speed))
        position_speeds.sort(key = lambda x: x[0], reverse=True)
        resp = 0
        # O(N * target)
        while position_speeds:
            tmp = []
            for position, speed in position_speeds:
                new_position = position + speed
                # Append to tmp
                if not tmp:
                    tmp.append((new_position, speed))
                # Check top of tmp, merge into fleet?
                else:
                    last_fleet_position, last_fleet_speed = tmp[-1]
                    # Caught up, merge into fleet
                    if new_position >= last_fleet_position:
                        tmp[-1] = (last_fleet_position, min(last_fleet_speed, speed))
                    else:
                        tmp.append((new_position, speed))
            
            # Short circuit
            if len(tmp) == 1:
                resp += 1
                break

            # Check for any merged fleets that passed target
            passed_target = 0
            for i in range(len(tmp)):
                if tmp[i][0] >= target:
                    passed_target += 1
                else:
                    break

            resp += passed_target
            position_speeds = tmp[passed_target:]

        return resp

sln = Solution_V3()
# print(sln.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
# print(sln.carFleet(10, [3], [3]))
# print(sln.carFleet(100, [0, 2, 4], [4, 2, 1]))
# print(sln.carFleet(16, [11,14,13,6], [2,2,6,7]))
print(sln.carFleet(31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]))

print(sln.carFleet(10, [6, 8], [3, 2]))


# print(sln.carFleet())

