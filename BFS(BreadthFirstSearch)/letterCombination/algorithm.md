# Algorithm: Breadth-First Search (Iterative)

## Core Concept
Unlike Backtracking, which dives deep into one path until it hits the end (Depth-First), the **BFS (Breadth-First Search)** approach builds all combinations **layer by layer**.

1.  **Layer 0**: Start with an empty string `""`.
2.  **Layer 1**: Take the first digit (e.g., '2'). Extend the empty string with 'a', 'b', 'c'.
    *   Result: `["a", "b", "c"]`
3.  **Layer 2**: Take the next digit (e.g., '3'). Extend *each* string from Layer 1 with 'd', 'e', 'f'.
    *   "a" -> "ad", "ae", "af"
    *   "b" -> "bd", "be", "bf"
    *   "c" -> "cd", "ce", "cf"
    *   Result: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

## Data Structure
We use a **Queue** (De-queue) to manage the processing order.
- **FIFO (First-In-First-Out)** ensures that we process "older" (shorter) strings before the newly created longer ones.
- However, for this specific problem, since we process the entire "level" at once, a simple list replacement strategy works too, but a Queue is the standard BFS implementation.

## Complexity
- **Time**: $O(4^N \cdot N)$
  - Same as backtracking. We visit every final combination once.
- **Space**: $O(4^N)$
  - This is the main difference. BFS stores the **widest** part of the tree.
  - At the last step, the queue holds **all** $4^N$ combinations.
  - Backtracking only holds one path of length $N$.
