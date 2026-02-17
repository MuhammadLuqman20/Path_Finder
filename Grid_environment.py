"""
Grid Environment Module
Handles grid creation and obstacles
"""

import random
import numpy as np

class GridEnvironment:
    def __init__(self, rows=10, cols=10, obstacle_probability=0.15):
        """
        Initialize grid environment
        
        Args:
            rows: Number of rows in grid
            cols: Number of columns in grid
            obstacle_probability: Probability of static obstacles
        """
        self.rows = rows
        self.cols = cols
        
        # 0 = empty, 1 = obstacle, 2 = start, 3 = target
        self.grid = np.zeros((rows, cols), dtype=int)
        
        # Add static obstacles
        self._generate_obstacles(obstacle_probability)
        
        # Start and target positions
        self.start = None
        self.target = None
        
    def _generate_obstacles(self, probability):
        """Generate random static obstacles"""
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < probability:
                    self.grid[i][j] = 1
                    
    def set_start(self, row, col):
        """Set start position"""
        if self.is_valid(row, col):
            self.grid[row][col] = 2
            self.start = (row, col)
            
    def set_target(self, row, col):
        """Set target position"""
        if self.is_valid(row, col):
            self.grid[row][col] = 3
            self.target = (row, col)
            
    def is_valid(self, row, col):
        """Check if position is within grid bounds"""
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_walkable(self, row, col):
        """Check if position is walkable (not obstacle)"""
        if not self.is_valid(row, col):
            return False
        return self.grid[row][col] != 1
    
    def get_neighbors(self, row, col):
        """
        Get valid neighbors in strict clockwise order with specific diagonals
        Order: Up, Right, Bottom, Bottom-Right (diagonal), Left, Top-Left (diagonal)
        Note: Does NOT include Top-Right or Bottom-Left diagonals
        """
        # 6 directions as per task requirement
        directions = [
            (-1, 0),   # Up
            (0, 1),    # Right
            (1, 0),    # Bottom
            (1, 1),    # Bottom-Right (diagonal)
            (0, -1),   # Left
            (-1, -1)   # Top-Left (diagonal)
        ]
        
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_walkable(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def clear_cell(self, row, col):
        """Clear a cell (set to empty)"""
        if self.is_valid(row, col):
            self.grid[row][col] = 0
            
    def reset(self):
        """Reset grid to initial state"""
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self._generate_obstacles(0.15)
        if self.start:
            self.set_start(self.start[0], self.start[1])
        if self.target:
            self.set_target(self.target[0], self.target[1])
