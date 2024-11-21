# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:23:31 2024
ALGORITHM OPTIMIZATION


@author: rober ugalde



Exercise 1
Code Optimization for Text Processing
"""



from collections import Counter
import string

def clean_text(text):
    """
    Converts text to lowercase and removes punctuation marks.
    """
    translator = str.maketrans('', '', string.punctuation)  # Create translation table for removing punctuation
    return text.lower().translate(translator)

def count_frequencies(words):
    """
    Counts the frequency of each word using Counter from collections.
    """
    return Counter(words)

def get_top_n_words(frequencies, n=5):
    """
    Returns the n most common words and their frequencies.
    """
    return frequencies.most_common(n)

def process_text(text):
    """
    Main function to process text: clean, count frequencies, and find top words.
    """
    # Clean text and split into words
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    # Count word frequencies
    word_frequencies = count_frequencies(words)

    # Get the 5 most common words
    top_5_words = get_top_n_words(word_frequencies, n=5)

    # Display results
    for word, frequency in top_5_words:
        print(f"'{word}': {frequency} times")

# Example text
text = """
    In the heart of the city, Emily discovered a quaint little café, hidden away from the bustling streets. 
    The aroma of freshly baked pastries wafted through the air, drawing in passersby. As she sipped on her latte, 
    she noticed an old bookshelf filled with classics, creating a cozy atmosphere that made her lose track of time.
"""

# Process and analyze text
process_text(text)



"""
Exercise 2
Code Optimization for List Processing




project 2

"""

import math

def is_prime(n):
    """
    Check if a number is prime.
    Optimized for efficiency by reducing redundant checks.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):  # Check factors of 6k ± 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def process_list(list_):
    """
    Process the list: filter even numbers, double them, calculate the sum, 
    and check if the sum is prime.
    """
    # Filter, double, and sum in a single comprehension
    doubled_sum = sum(num * 2 for num in list_ if num % 2 == 0)
    
    # Check if the result is prime
    prime = is_prime(doubled_sum)
    
    return doubled_sum, prime

# Example list
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Process the list
result, result_prime = process_list(list_)
print(f"Result: {result}, Prime? {'Yes' if result_prime else 'No'}")



