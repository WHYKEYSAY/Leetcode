# Algorithm: Letter Combinations of a Phone Number

This problem is solved using **Backtracking**, which is a form of generic Depth-First Search (DFS). The goal is to explore all possible combinations of letters that the input digits could represent.

## Core Logic

1.  **Mapping**: First, we define a mapping from digits (2-9) to their corresponding letters, just like a telephone keypad.
    *   `2` -> "abc"
    *   `3` -> "def"
    *   ...
    *   `9` -> "wxyz"

2.  **Backtracking Function**: We define a recursive function `backtrack(index, path)`.
    *   `index`: The index of the digit we are currently processing in the input string.
    *   `path`: The current combination of letters we have built so far.

3.  **Base Case (Stopping Condition)**:
    *   If `index` equals the length of the input `digits`, it means we have processed all digits.
    *   We join the `path` list into a string and add it to our result list.
    *   Return (backtrack).

4.  **Recursive Step**:
    *   Get the current digit: `d = digits[index]`.
    *   Get the letters corresponding to `d` (e.g., if `d` is '2', letters are 'a', 'b', 'c').
    *   Loop through each `letter`:
        1.  **Choose**: Append `letter` to the `path`.
        2.  **Explore**: Call `backtrack(index + 1, path)` to process the *next* digit.
        3.  **Un-choose**: Pop `letter` from the `path`. This removes the last decision so we can try the next letter in the loop.

## Complexity Analysis

*   **Time Complexity**: $O(4^N \cdot N)$
    *   $N$ is the length of digits.
    *   In the worst case (e.g., digits 7 or 9), each digit maps to 4 letters.
    *   There are $4^N$ total combinations.
    *   For each combination, we spend $O(N)$ time to build the string.

*   **Space Complexity**: $O(N)$
    *   O(N) for the recursion stack depth.
    *   O(N) for the `path` list.
    *   (Ignoring the space required for the output list).
