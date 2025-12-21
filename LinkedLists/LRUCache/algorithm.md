# Algorithm: LRU Cache

The **Least Recently Used (LRU)** cache evicts the item that hasn't been used for the longest time when the cache reaches its capacity.

To achieve **O(1)** time complexity for both `get` and `put` operations, we combine two data structures:

1.  **Hash Map (Dictionary)**: `key -> Node`
    *   Allows O(1) access to items.
2.  **Doubly Linked List (DLL)**:
    *   Maintains the order of usage.
    *   **Head**: Most Recently Used (MRU).
    *   **Tail**: Least Recently Used (LRU).
    *   Allows O(1) removal and insertion of nodes (since we have references to `prev` and `next`).

## Operations

### `get(key)`
1.  Check if `key` exists in the Hash Map.
2.  If No: Return `-1`.
3.  If Yes:
    *   Get the `Node` from the map.
    *   **Move Node to Head**: Remove it from its current position in DLL and insert it right after the dummy head.
    *   Return `node.value`.

### `put(key, value)`
1.  Check if `key` exists.
2.  If Yes:
    *   Update `node.value`.
    *   **Move Node to Head** (it's now the most recently used).
3.  If No:
    *   Create a new `Node(key, value)`.
    *   Add it to Hash Map.
    *   **Add Node to Head**.
    *   **Check Capacity**: If `size > capacity`:
        *   Remove the node at the **Tail** (LRU).
        *   Remove that key from the Hash Map.

## Complexity
*   **Time Complexity**: O(1) for both `get` and `put` because hash map lookups and linked list pointer updates are constant time.
*   **Space Complexity**: O(C), where C is the capacity, to store the nodes and map entries.
