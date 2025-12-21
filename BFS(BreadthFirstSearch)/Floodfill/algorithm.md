# Algorithm: BFS for Flood Fill (Graph Traversal)

## Core Concept
The "Flood Fill" algorithm is essentially a traversal on a 2D Graph.
- **Nodes**: Each pixel `(r, c)` in the grid.
- **Edges**: Connections to 4 adjacent pixels (Up, Down, Left, Right).
- **Condition**: An edge exists (or is traversable) only if the neighbor has the same `start_color`.

## BFS (Breadth-First Search) Approach
BFS is ideal here because it expands outwards from the starting pixel in layers, similar to how water spreads or a ripple moves in a pond.

### Steps
1.  **Start Node**: Identify the starting pixel `(sr, sc)` and its `start_color`.
2.  **Queue Initialization**: Put the start node into a Queue.
3.  **Processing Loop**:
    - While the Queue is not empty:
        - **Pop** a pixel `(r, c)` from the front.
        - **Update**: Change its color to `new_color`.
        - **Explore**: Look at all 4 neighbors (Up, Down, Left, Right).
        - **Filter**: If a neighbor is valid (inside grid) AND has the `start_color` AND has not been visited:
            - Add it to the Queue.
            - Mark it as visited (or change its color immediately to prevent re-adding).

## Complexity
- **Time Complexity**: $O(N)$
  - $N$ is the total number of pixels in the image.
  - In the worst case (all pixels are the same color), we visit every pixel exactly once.
- **Space Complexity**: $O(N)$
  - In the worst case, the Queue might hold most of the "boundary" or "diagonal" of the filled area, which scales with the image size.
