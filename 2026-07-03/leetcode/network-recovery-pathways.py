# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Network Recovery Pathways
# ║  Difficulty : Hard
# ║  Date       : 2026-07-03
# ║  URL        : https://leetcode.com/problems/network-recovery-pathways/
# ╚══════════════════════════════════════════════════════════════╝

import collections

"""
Problem Analysis:
The goal is to find a path from node 0 to node n-1 such that:
1. All nodes on the path are 'online'.
2. The total cost of edges on the path <= k.
3. We want to maximize the minimum edge-cost (score) among all such paths.

Approach:
1. The graph is a Directed Acyclic Graph (DAG).
2. The "maximum of minimums" objective suggests that we can binary search on the possible 
   edge costs.
3. For a fixed value X, we want to know if there exists a path from 0 to n-1 such that:
    - Every edge on the path has cost >= X.
    - Every node on the path is online.
    - The sum of edge costs <= k.
4. Since the graph is a DAG, for a fixed X, we can find the shortest path (minimum total cost) 
   from node 0 to node n-1 using Dynamic Programming or Topological Sort.
5. If the shortest path cost <= k, then a path with a score of at least X exists.

Complexity:
- Let n be the number of nodes and m be the number of edges.
- Sorting all unique edge costs takes O(m log m).
- Binary search takes O(log m) iterations.
- In each iteration, we perform a topological sort traversal, which takes O(n + m).
- Total Time Complexity: O(m log m + (n + m) * log m).
- Total Space Complexity: O(n + m) to store the graph.
"""

class Solution:
    def solve(self, n: int, edges: list[list[int]], online: list[bool], k: int) -> int:
        # 1. Build the graph and identify the topological order
        # Since it's a DAG, we can pre-compute the topological sort once.
        adj = collections.defaultdict(list)
        in_degree = [0] * n
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
        
        topo_order = []
        queue = collections.deque([i for i in range(n) if in_degree[i] == 0])
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # 2. Collect all unique edge costs for binary search
        all_costs = sorted(list(set(edge[2] for edge in edges)))
        
        def check(min_allowed_cost):
            """
            Checks if there is a path from 0 to n-1 using only edges >= min_allowed_cost,
            only online nodes, and with total cost <= k.
            """
            # dist[i] = minimum total cost to reach node i from node 0
            # Initialize with infinity.
            dist = [float('inf')] * n
            dist[0] = 0
            
            # Process nodes in topological order
            for u in topo_order:
                if dist[u] == float('inf'):
                    continue
                # Optimization: if u is offline, it can't be part of a valid path
                # Note: 0 and n-1 are guaranteed to be online.
                if not online[u]:
                    continue
                
                for v, cost in adj[u]:
                    # The path must only use edges with cost >= min_allowed_cost
                    # and the destination node must be online.
                    if cost >= min_allowed_cost and online[v]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
            
            return dist[n - 1] <= k

        # 3. Binary search on the unique edge costs
        low = 0
        high = len(all_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(all_costs[mid]):
                ans = all_costs[mid]
                low = mid + 1  # Try to find a larger minimum edge cost
            else:
                high = mid - 1 # The cost is too restrictive, try smaller
                
        return ans

# The provided interface in the prompt is slightly different from standard LeetCode 
# (e.g., function name), but this logic solves the described problem.
