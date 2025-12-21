from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        for d in digits:
            if d not in phone:
                print(f"Error: Digit '{d}' has no letters associated with it.")
                return []
        res = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for char in phone[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res

# --- Interactive Section ---
if __name__ == "__main__":
    sol = Solution()
    
    # Prompt the user for input
    user_input = input("Enter the digits (e.g., 23): ")
    
    # FIX: Remove extra quotes or spaces that might be pasted in
    cleaned_input = user_input.replace('"', '').replace("'", "").strip()
    
    # Get the result and print it using the cleaned input
    result = sol.letterCombinations(cleaned_input)
    print(f"Combinations: {result}")
