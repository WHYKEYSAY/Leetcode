from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Performs a flood fill on the image starting from the pixel (sr, sc).
        
        Args:
        image: 2D list of integers representing the image.
        sr: Source row index.
        sc: Source column index.
        color: The new color to paint.
        """
        start_color = image[sr][sc]
        
        # Optimize: If the color is already the same, no changes needed.
        # This also prevents infinite loops if we rely purely on color checks without a visited set.
        if start_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        
        # We also keep a visited set if we want to strictly follow Graph structure,
        # but changing the color itself acts as "visiting" in this specific problem.
        # However, to match the provided image's logic (which emphasizes explicit graph style):
        visited = set()
        visited.add((sr, sc))
        
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            
            # Check 4 cardinal directions
            for nr, nc in self.get_neighbors(image, r, c, start_color):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
        return image

    def get_neighbors(self, image, r, c, start_color):
        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        neighbors = []
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if image[nr][nc] == start_color:
                    neighbors.append((nr, nc))
        return neighbors

# --- Interactive Section ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example Image (Grid)
    # 1 1 1
    # 1 1 0
    # 1 0 1
    test_image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    
    print("Original Image:")
    for row in test_image:
        print(row)
        
    # Start at (1, 1) which is center, change color 1 to 2
    res = sol.floodFill(test_image, 1, 1, 2)
    
    print("\nResult Image (Flood Fill (1, 1) -> 2):")
    for row in res:
        print(row)
