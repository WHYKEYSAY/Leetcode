# Algorithm: Most Frequent Word

This document describes the algorithm to find the most frequent word in a paragraph.

## Steps

1.  **Normalize Text**
    *   **Goal**: Ensure consistency so that "The", "the", and "the." are treated as the same word.
    *   **Method**: Convert the entire paragraph to lowercase. Remove all punctuation marks (like periods, commas, exclamation points) using regular expressions (specifically replacing `[^\w\s]` with an empty string).

2.  **Tokenize**
    *   **Goal**: Break the normalized text into individual units (words).
    *   **Method**: Split the string by whitespace. This creates a list of words.

3.  **Count Frequencies**
    *   **Goal**: Determine how often each word appears.
    *   **Method**: Iterate through the list of words and maintain a count for each unique word. A hash map (dictionary in Python) or a specialized counter object acts as the data structure for this, mapping `word -> count`.

4.  **Find Maximum**
    *   **Goal**: Identify the word with the highest count.
    *   **Method**:  Retrieve the item from the frequency map with the largest integer value. In Python, `Counter.most_common(1)` optimizes this step.

## Complexity

*   **Time Complexity**: O(N), where N is the number of characters in the paragraph. Regex replacement, splitting, and counting each take linear time relative to the input size.
*   **Space Complexity**: O(M), where M is the number of unique words in the paragraph, to store the frequency map.
