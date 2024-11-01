class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        result = [-1] * n
        
        queue = deque([(0, 'red', 0), (0, 'blue', 0)])
        visited = set([(0, 'red'), (0, 'blue')])
        
        while queue:
            node, color, distance = queue.popleft()
            
            if result[node] == -1 or distance < result[node]:
                result[node] = distance
            
            if color == 'red':
                next_color = 'blue'
                neighbors = blue_graph[node]
            else:
                next_color = 'red'
                neighbors = red_graph[node]
            
            for neighbor in neighbors:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, next_color, distance + 1))
        
        return result