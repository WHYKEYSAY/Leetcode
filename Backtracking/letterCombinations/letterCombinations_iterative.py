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
        
        # Initialize queue with an empty string
        queue = deque([""])
        
        for d in digits:
            if d not in phone:
                 continue
                 
            # For the current digit, process all existing elements in the queue
            # We must capture the current size because the queue grows inside the loop
            current_size = len(queue)
            
            for _ in range(current_size):
                # Pop the existing prefix (e.g., "a")
                prefix = queue.popleft()
                
                # Append each new letter (e.g., "ad", "ae", "af")
                for letter in phone[d]:
                    queue.append(prefix + letter)
        
        return list(queue)

if __name__ == "__main__":
    sol = Solution()
    print(f"Combinations for '23': {sol.letterCombinations('23')}")
