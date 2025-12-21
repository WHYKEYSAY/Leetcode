from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Validating input first
        for d in digits:
            if d not in phone:
                print(f"Error: Digit '{d}' is invalid.")
                return []
        
        # Initialize the queue with an empty string
        # This represents the "root" of our decision tree before picking any digits
        queue = deque([""])
        
        # Loop through each digit in the input string
        for d in digits:
            # We need to process all nodes at the current level (current length)
            # queue len changes as we append, so we must store the size before the inner loop
            current_level_size = len(queue)
            
            for _ in range(current_level_size):
                # Pop the existing combination from the front
                current_string = queue.popleft()
                
                # Append each possible letter for the NEW digit
                for char in phone[d]:
                    queue.append(current_string + char)
        
        return list(queue)

# --- Interactive Section ---
if __name__ == "__main__":
    sol = Solution()
    user_input = input("Enter digits (e.g., 23): ")
    cleaned_input = user_input.replace('"', '').replace("'", "").strip()
    result = sol.letterCombinations(cleaned_input)
    print(f"Combinations: {result}")
