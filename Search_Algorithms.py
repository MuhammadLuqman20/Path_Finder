"""
Search Algorithms Module
Implements multiple search algorithms: DLS, IDDFS, Bidirectional, BFS, DFS, and UCS
"""

from collections import deque
import heapq

class SearchAlgorithms:
    def __init__(self, grid_env):
        """
        Initialize search algorithms
        
        Args:
            grid_env: GridEnvironment instance
        """
        self.grid_env = grid_env
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}  # Track visit order for visualization
        
    def depth_limited_search(self, start, target, limit, visualizer=None):
        """
        Depth-Limited Search (DLS)
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            limit: Depth limit
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        visit_counter = [0]  # Use list to allow modification in nested function
        
        def dls_recursive(node, depth, path, explored):
            """Recursive DLS helper"""
            # Check for stop flag
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    return 'STOPPED'
            
            if depth > limit:
                return None
            
            if node == target:
                return path
            
            explored.add(node)
            self.explored_history.append(node)
            visit_counter[0] += 1
            self.visit_order[node] = visit_counter[0]
            
            # Visualization update
            if visualizer:
                self.frontier_history.append([node])
                visualizer.update(
                    frontier=[node],
                    explored=list(explored),
                    path=[],
                    algorithm_name="Depth-Limited Search (DLS)",
                    depth_info=f"Current Depth: {depth}/{limit}",
                    visit_order=self.visit_order
                )
            
            # Get neighbors
            neighbors = self.grid_env.get_neighbors(node[0], node[1])
            
            for neighbor in neighbors:
                if neighbor not in explored:
                    new_path = path + [neighbor]
                    result = dls_recursive(neighbor, depth + 1, new_path, explored)
                    if result == 'STOPPED':
                        return 'STOPPED'
                    if result is not None:
                        return result
            
            return None
        
        explored = set()
        result = dls_recursive(start, 0, [start], explored)
        
        # Check if stopped
        if result == 'STOPPED':
            if visualizer:
                visualizer.update(
                    frontier=[],
                    explored=list(explored),
                    path=[],
                    algorithm_name="Depth-Limited Search (DLS)",
                    depth_info="Stopped by user",
                    visit_order=self.visit_order
                )
            return None
        
        if result:
            self.path = result
            if visualizer:
                visualizer.update(
                    frontier=[],
                    explored=list(explored),
                    path=result,
                    algorithm_name="Depth-Limited Search (DLS)",
                    depth_info=f"Path Found! Length: {len(result)}",
                    visit_order=self.visit_order
                )
        
        return result
    
    def iterative_deepening_dfs(self, start, target, max_depth=50, visualizer=None):
        """
        Iterative Deepening Depth-First Search (IDDFS)
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            max_depth: Maximum depth to search
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        
        for depth_limit in range(max_depth):
            # Check for stop flag before each iteration
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    if visualizer:
                        visualizer.update(
                            frontier=[],
                            explored=self.explored_history,
                            path=[],
                            algorithm_name="Iterative Deepening DFS (IDDFS)",
                            depth_info="Stopped by user",
                            visit_order=self.visit_order
                        )
                    return None
            
            result = self.depth_limited_search(start, target, depth_limit, visualizer)
            
            if result is not None:
                self.path = result
                if visualizer:
                    visualizer.update(
                        frontier=[],
                        explored=self.explored_history,
                        path=result,
                        algorithm_name="Iterative Deepening DFS (IDDFS)",
                        depth_info=f"Found at depth {depth_limit}! Path length: {len(result)}",
                        visit_order=self.visit_order
                    )
                return result
            
            # Update visualization between depth iterations
            if visualizer:
                visualizer.update(
                    frontier=[],
                    explored=self.explored_history,
                    path=[],
                    algorithm_name="Iterative Deepening DFS (IDDFS)",
                    depth_info=f"Trying depth limit: {depth_limit + 1}",
                    visit_order=self.visit_order
                )
        
        return None
    
    def bidirectional_search(self, start, target, visualizer=None):
        """
        Bidirectional Search - searches from both start and target simultaneously
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        visit_counter = 0
        
        # Forward search from start
        frontier_forward = deque([start])
        explored_forward = {start: None}
        
        # Backward search from target
        frontier_backward = deque([target])
        explored_backward = {target: None}
        
        meeting_point = None
        
        while frontier_forward and frontier_backward:
            # Check for stop flag
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    if visualizer:
                        visualizer.update(
                            frontier=[],
                            explored=self.explored_history,
                            path=[],
                            algorithm_name="Bidirectional Search",
                            depth_info="Stopped by user",
                            visit_order=self.visit_order
                        )
                    return None
            
            # Forward step
            if frontier_forward:
                current_forward = frontier_forward.popleft()
                
                # Track visit order
                if current_forward not in self.visit_order:
                    visit_counter += 1
                    self.visit_order[current_forward] = visit_counter
                
                # Check if we met the backward search
                if current_forward in explored_backward:
                    meeting_point = current_forward
                    break
                
                # Explore neighbors
                neighbors = self.grid_env.get_neighbors(current_forward[0], current_forward[1])
                for neighbor in neighbors:
                    if neighbor not in explored_forward:
                        frontier_forward.append(neighbor)
                        explored_forward[neighbor] = current_forward
                
                # Visualization
                if visualizer:
                    self.frontier_history.append(list(frontier_forward) + list(frontier_backward))
                    self.explored_history = list(explored_forward.keys()) + list(explored_backward.keys())
                    
                    visualizer.update(
                        frontier=list(frontier_forward) + list(frontier_backward),
                        explored=self.explored_history,
                        path=[],
                        algorithm_name="Bidirectional Search",
                        depth_info=f"Forward: {len(explored_forward)} | Backward: {len(explored_backward)}"
                    )
            
            # Backward step
            if frontier_backward:
                current_backward = frontier_backward.popleft()
                
                # Track visit order
                if current_backward not in self.visit_order:
                    visit_counter += 1
                    self.visit_order[current_backward] = visit_counter
                
                # Check if we met the forward search
                if current_backward in explored_forward:
                    meeting_point = current_backward
                    break
                
                # Explore neighbors
                neighbors = self.grid_env.get_neighbors(current_backward[0], current_backward[1])
                for neighbor in neighbors:
                    if neighbor not in explored_backward:
                        frontier_backward.append(neighbor)
                        explored_backward[neighbor] = current_backward
                
                # Visualization
                if visualizer:
                    self.frontier_history.append(list(frontier_forward) + list(frontier_backward))
                    self.explored_history = list(explored_forward.keys()) + list(explored_backward.keys())
                    
                    visualizer.update(
                        frontier=list(frontier_forward) + list(frontier_backward),
                        explored=self.explored_history,
                        path=[],
                        algorithm_name="Bidirectional Search",
                        depth_info=f"Forward: {len(explored_forward)} | Backward: {len(explored_backward)}",
                        visit_order=self.visit_order
                    )
        
        # Reconstruct path if meeting point found
        if meeting_point:
            # Build forward path
            forward_path = []
            node = meeting_point
            while node is not None:
                forward_path.append(node)
                node = explored_forward[node]
            forward_path.reverse()
            
            # Build backward path
            backward_path = []
            node = explored_backward[meeting_point]
            while node is not None:
                backward_path.append(node)
                node = explored_backward[node]
            
            # Combine paths
            self.path = forward_path + backward_path
            
            if visualizer:
                visualizer.update(
                    frontier=[],
                    explored=self.explored_history,
                    path=self.path,
                    algorithm_name="Bidirectional Search",
                    depth_info=f"Paths met! Total length: {len(self.path)}",
                    visit_order=self.visit_order
                )
            
            return self.path
        
        return None
    
    def reconstruct_path(self, came_from, target):
        """
        Reconstruct path from came_from dictionary
        
        Args:
            came_from: Dictionary mapping node -> parent node
            target: Target position
            
        Returns:
            List of positions representing path
        """
        path = []
        current = target
        
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        
        path.reverse()
        return path
    
    def bfs(self, start, target, visualizer=None):
        """
        Breadth-First Search (BFS)
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        
        queue = deque([start])
        parent = {start: None}
        visited = {start}
        steps = 0
        visit_counter = 0
        
        while queue:
            steps += 1
            
            # Check for stop flag
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    if visualizer:
                        visualizer.update(
                            frontier=list(queue),
                            explored=list(visited),
                            path=[],
                            algorithm_name="Breadth-First Search (BFS)",
                            depth_info="Stopped by user"
                        )
                    return None
            
            current = queue.popleft()
            self.explored_history.append(current)
            visit_counter += 1
            self.visit_order[current] = visit_counter
            
            if current == target:
                self.path = self.reconstruct_path(parent, current)
                if visualizer:
                    visualizer.update(
                        frontier=[],
                        explored=self.explored_history,
                        path=self.path,
                        algorithm_name="Breadth-First Search (BFS)",
                        depth_info=f"Path Found! Length: {len(self.path)}",
                        visit_order=self.visit_order
                    )
                return self.path
            
            neighbors = self.grid_env.get_neighbors(current[0], current[1])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
            
            # Visualization update
            if visualizer and steps % 2 == 0:
                visualizer.update(
                    frontier=list(queue),
                    explored=self.explored_history,
                    path=[],
                    algorithm_name="Breadth-First Search (BFS)",
                    depth_info=f"Explored: {len(self.explored_history)} nodes",
                    visit_order=self.visit_order
                )
        
        return None
    
    def dfs(self, start, target, visualizer=None):
        """
        Depth-First Search (DFS)
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        
        stack = [start]
        parent = {start: None}
        visited = {start}
        explored_set = set()
        steps = 0
        visit_counter = 0
        
        while stack:
            steps += 1
            
            # Check for stop flag
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    if visualizer:
                        visualizer.update(
                            frontier=stack,
                            explored=self.explored_history,
                            path=[],
                            algorithm_name="Depth-First Search (DFS)",
                            depth_info="Stopped by user",
                            visit_order=self.visit_order
                        )
                    return None
            
            current = stack.pop()
            
            if current in explored_set:
                continue
            
            explored_set.add(current)
            self.explored_history.append(current)
            visit_counter += 1
            self.visit_order[current] = visit_counter
            
            if current == target:
                self.path = self.reconstruct_path(parent, current)
                if visualizer:
                    visualizer.update(
                        frontier=[],
                        explored=self.explored_history,
                        path=self.path,
                        algorithm_name="Depth-First Search (DFS)",
                        depth_info=f"Path Found! Length: {len(self.path)}",
                        visit_order=self.visit_order
                    )
                return self.path
            
            neighbors = self.grid_env.get_neighbors(current[0], current[1])
            neighbors.reverse()  # For DFS, reverse to explore in specific order
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)
            
            # Visualization update
            if visualizer and steps % 2 == 0:
                visualizer.update(
                    frontier=stack[-10:] if len(stack) > 10 else stack,  # Show last 10 for clarity
                    explored=self.explored_history,
                    path=[],
                    algorithm_name="Depth-First Search (DFS)",
                    depth_info=f"Explored: {len(self.explored_history)} nodes",
                    visit_order=self.visit_order
                )
        
        return None
    
    def ucs(self, start, target, visualizer=None):
        """
        Uniform Cost Search (UCS)
        
        Args:
            start: Start position (row, col)
            target: Target position (row, col)
            visualizer: Visualizer instance for GUI updates
            
        Returns:
            List of positions representing path, or None if not found
        """
        self.frontier_history = []
        self.explored_history = []
        self.path = []
        self.visit_order = {}
        
        heap = [(0, start)]
        parent = {start: None}
        cost = {start: 0}
        visited = set()
        frontier_set = {start}
        steps = 0
        visit_counter = 0
        
        while heap:
            steps += 1
            
            # Check for stop flag
            if visualizer and hasattr(visualizer, 'stop_flag_callback'):
                if visualizer.stop_flag_callback and visualizer.stop_flag_callback():
                    if visualizer:
                        visualizer.update(
                            frontier=list(frontier_set),
                            explored=self.explored_history,
                            path=[],
                            algorithm_name="Uniform Cost Search (UCS)",
                            depth_info="Stopped by user",
                            visit_order=self.visit_order
                        )
                    return None
            
            current_cost, current = heapq.heappop(heap)
            
            if current in frontier_set:
                frontier_set.remove(current)
            
            if current in visited:
                continue
            
            visited.add(current)
            self.explored_history.append(current)
            visit_counter += 1
            self.visit_order[current] = visit_counter
            
            if current == target:
                self.path = self.reconstruct_path(parent, current)
                if visualizer:
                    visualizer.update(
                        frontier=[],
                        explored=self.explored_history,
                        path=self.path,
                        algorithm_name="Uniform Cost Search (UCS)",
                        depth_info=f"Path Found! Cost: {current_cost:.2f}",
                        visit_order=self.visit_order
                    )
                return self.path
            
            neighbors = self.grid_env.get_neighbors(current[0], current[1])
            for neighbor in neighbors:
                if neighbor not in visited:
                    # Calculate move cost (diagonal = 1.414, straight = 1)
                    row_diff = abs(neighbor[0] - current[0])
                    col_diff = abs(neighbor[1] - current[1])
                    
                    if row_diff == 1 and col_diff == 1:
                        move_cost = 1.414
                    else:
                        move_cost = 1.0
                    
                    new_cost = current_cost + move_cost
                    
                    if neighbor not in cost or new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        parent[neighbor] = current
                        heapq.heappush(heap, (new_cost, neighbor))
                        frontier_set.add(neighbor)
            
            # Visualization update
            if visualizer and steps % 2 == 0:
                visualizer.update(
                    frontier=list(frontier_set),
                    explored=self.explored_history,
                    path=[],
                    algorithm_name="Uniform Cost Search (UCS)",
                    depth_info=f"Explored: {len(self.explored_history)} | Cost: {current_cost:.2f}",
                    visit_order=self.visit_order
                )
        
        return None
