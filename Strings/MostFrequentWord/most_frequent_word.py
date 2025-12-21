import re
from collections import Counter

def get_most_frequent_word(paragraph):
    """
    Finds the most frequent word in a paragraph, ignoring punctuation and case.
    
    Args:
        paragraph (str): The input text.
        
    Returns:
        tuple: A tuple containing the most frequent word and its count, e.g., ('word', 5).
               Returns (None, 0) if the input contains no valid words.
    """
    # 1. Normalize: Set to lowercase and remove all punctuation.
    cleaned_text = re.sub(r'[^\w\s]', '', paragraph.lower())
    
    # 2. Tokenize: Split the text into a list of words.
    words = cleaned_text.split()
    
    if not words:
        return None, 0
    
    # 3. Count: Use collections.Counter to get word frequencies.
    word_counts = Counter(words)
    
    # 4. Find most common: .most_common(1) returns a list [('word', count)]
    most_common_pair = word_counts.most_common(1)[0]
    
    return most_common_pair

if __name__ == "__main__":
    # Example usage:
    text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    word, count = get_most_frequent_word(text)
    print(f"Word: '{word}', Count: {count}")  # Output: Word: 'the', Count: 3
