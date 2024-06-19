from collections import defaultdict, deque

# Gg O(E) time complexity, O(E) space complexity
# Guarantee that you have at least one Eulerian path - either 0 or 2 (start and end) nodes have odd degrees
# No issues if all nodes have even degree
# A Eulerian cycle is a Eulerian path, but not the reverse
# If all nodes have even degree, then every 'entrance' must have an 'exit'
# Can only get stuck at the odd degree node - 'the end'
# When you backtrack, you remove 1 edge from the next last node - becomes new 'end'.
# It was even previously - the matching edge is on our current path
# So if there are any further paths out, they must form a cycle back to this node
class Solution_LeetSolution(object):
    def findItinerary(self, tickets):
        # Sort so that lower lexical case airport visited first
        targets = defaultdict(list)
        tickets.sort(key = lambda x:x[1], reverse = True)
        for src, dst in tickets:
            targets[src].append(dst)

        print(targets)
        # print(targets)
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            # Write path backwards
            # Guarantee that when you get stuck, the remaining form a cycle?
            # Also that you visit the cycle in smallest lexical order - get stuck in smallest lexical order, then explore side-cycles in smallest lexical order
            route.append(airport)
            print(route, targets)

        visit('JFK')
        return route[::-1]

# Well slightly cleaner but same solution - backtrack + greedy
# Got TLE for 80/81 still lol
# Still O(E^2) worst case due to backtracking
class Solution_AfterNeet(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # E lg E -> Sort in ascending order
        tickets.sort(key = lambda x:x[1])

        routes = defaultdict(deque)
        for src, dst in tickets:
            routes[src].append(dst)

        self.resp = ['JFK']
        def dfs(port):
            if len(self.resp) == len(tickets) + 1:
                return True
            
            num_dst = len(routes[port])
            for _ in range(num_dst):
                dst = routes[port].popleft()
                self.resp.append(dst)
                if dfs(dst): return True
                self.resp.pop()
                routes[port].append(dst)

            return False

        dfs("JFK")
        return self.resp
    
# Hmm, another way is to pre-sort the tickets so that the first path explored will have the lowest lexical order
# Then E lg E - where E = len(tickets), or number of edges
# But still running into TLE for 80/81 cases lol
# No bottleneck is actually the backtracking, E^2
class Solution_V2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # N lg N -> Sort in ascending order
        tickets.sort(key = lambda x:x[1])

        routes = defaultdict(deque)
        for src, dst in tickets:
            routes[src].append(dst)

        self.resp = None
        def dfs(port, cur_path):
            if self.resp: return
            cur_path.append(port)

            # Used all tickets
            if len(cur_path) == len(tickets) + 1:
                # Deep copy
                itinerary = []
                for p in cur_path:
                    itinerary.append(p)
                self.resp = itinerary
                return
            else:
                num_dst = len(routes[port])
                for _ in range(num_dst):
                    dst = routes[port].popleft()
                    dfs(dst, cur_path)
                    routes[port].append(dst)

            cur_path.pop()
        
        # Start dfs from 'JFK'
        dfs("JFK", [])
        return self.resp

# All start from 'JFK'
# from -> to
# Itinerary in order
# If multiple valid itineraries, return itinerary with smallest lexical order when read as a single string
# At least one valid itinerary
# Must use all tickets once and once only
# Create adjacency matrix, there are multiple
# Topological sort starting from 'JFK'
# Can only use all tickets once - not visit the ports only once, but use all tickets only once
# DFS from 'JFK'
# There is no constraint saying that pair of [from, to] can be unique
# So how can we keep track of remaining paths?

# Lol basically took an hour, and got time limited exceeded for 11 out of 81 test cases on Leetcode
# But it is running for the test cases
# This question is hard though, you not only have to find all the possible paths, but also find the path with the lowest lexigraphical order
# Hmm I think my solution is correct, but it is not efficient enough, because the DFS is worst case n^n
# And how about the sort algorithm - well this is fit for a count sort, so it becomes O(26N)

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Store possible itineraries
        itineraries = []

        # src -> String[dst]
        routes = defaultdict(deque)
        
        for src, dst in tickets:
            routes[src].append(dst)
        
        def dfs(port, cur_path):
            cur_path.append(port)

            # Used all tickets
            if len(cur_path) == len(tickets) + 1:
                # Deep copy
                itinerary = []
                for p in cur_path:
                    itinerary.append(p)
                itineraries.append(itinerary)
            else:
                num_dst = len(routes[port])
                for _ in range(num_dst):
                    dst = routes[port].popleft()
                    dfs(dst, cur_path)
                    routes[port].append(dst)

            cur_path.pop()
        
        # Start dfs from 'JFK'
        dfs("JFK", [])
        # Find the smallest lexical order
        cur_sort_ptr = 3
        while len(itineraries) > 1 and cur_sort_ptr < (len(tickets) + 1) * 3:
            cur_word_index = cur_sort_ptr // 3
            cur_word_letter = cur_sort_ptr % 3
            temp_min_itineraries = [itineraries[0]]

            for i in range(1, len(itineraries)):
                cur_min_letter = temp_min_itineraries[0][cur_word_index][cur_word_letter]
                cur_letter = itineraries[i][cur_word_index][cur_word_letter]
                if ord(cur_letter) < ord(cur_min_letter):
                    temp_min_itineraries = [itineraries[i]]
                elif ord(cur_letter) == ord(cur_min_letter):
                    temp_min_itineraries.append(itineraries[i])

            itineraries = temp_min_itineraries
            cur_sort_ptr += 1

        return itineraries[0]
    
sln = Solution_LeetSolution()
print(sln.findItinerary([["JFK","AAA"], ["AAA","CCC"], ["CCC","DDD"], ["DDD","AAA"], ["DDD","YYY"], ["YYY","DDD"], ["DDD","BBB"], ["BBB","CCC"], ["CCC","ZZZ"], ["ZZZ","DDD"]]))

# print(sln.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# print(sln.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(sln.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
# print(sln.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]))



# print(sln.findItinerary())