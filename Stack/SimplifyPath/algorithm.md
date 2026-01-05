# Simplify Path Algorithm

## Problem Statement
Given an absolute path for a Unix-style file system, transform it into its simplified canonical path.

## Approach: Stack-Based
The problem asks us to resolve relative path components like `.` (current directory) and `..` (parent directory) to produce a clean, absolute path. A **Stack** is an ideal data structure for this because directory traversal is a Last-In, First-Out (LIFO) operation in the context of resolving paths (simplifying `a/b/..` requires removing `b`, which was the last item added).

### Logic
1.  **Split the Input String**: 
    - We split the input `path` by the slash delimiter `/`. This gives us a list of directory names and potential empty strings (caused by consecutive slashes like `//` or trailing slashes).
    
2.  **Process Components**:
    - Iterate through each component in the split list.
    - **Ignore**: 
        - Empty strings (`""`): These result from multiple consecutive slashes (e.g., `//` splits to `""`, `""`).
        - Single periods (`.`): These represent the current directory and have no effect on the path.
    - **Go Back (Pop)**:
        - Double periods (`..`): These represent moving up to the parent directory. If the stack is not empty, we pop the top element (the directory we just "entered"). If the stack is empty (we are at the root), we do nothing (since we can't go higher than root).
    - **Enter Directory (Push)**:
        - Any other string is treated as a valid directory name. We push it onto the stack.

3.  **Construct Result**:
    - After processing all components, the stack contains the valid sequence of directories from the root.
    - Join these components with `/` and prepend a starting `/` to form the absolute path.

### Complexity Analysis
-   **Time Complexity**: $O(N)$, where $N$ is the length of the string. We iterate through the string once (during the split) and then iterate through the components once.
-   **Space Complexity**: $O(N)$ for the stack and the array of split components. In the worst case (e.g., `/a/b/c/...`), the stack stores all directory names.

### Example Walkthrough
Input: `/home//foo/`
1.  Split by `/` -> `['', 'home', '', 'foo', '']`
2.  Process:
    -   `''`: ignore.
    -   `'home'`: push to stack. Stack: `['home']`
    -   `''`: ignore.
    -   `'foo'`: push to stack. Stack: `['home', 'foo']`
    -   `''`: ignore.
3.  Join stack with `/` -> `"home/foo"`
4.  Prepend `/` -> `"/home/foo"`
