import string
import random
# collections.Counter is a special dictionary for counting things
from collections import defaultdict, Counter

# We can keep this at 2, or even try 3!
N_GRAM_SIZE = 2 

def preprocess_text(file_path):
    """Reads a text file, cleans it, and returns a list of words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        print("Please check your file path.")
        return None
    
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    tokens = text.split()
    return tokens

def build_chain(tokens, n):
    """
    Builds a weighted N-gram Markov chain.
    
    The keys are (n)-word tuples.
    The values are Counter objects (dictionaries) mapping the 
    next word to its frequency (count).
    """
    # Use defaultdict to automatically create a Counter for new keys
    chain = defaultdict(Counter)
    
    if len(tokens) < n + 1:
        return chain

    for i in range(len(tokens) - n):
        key_tuple = tuple(tokens[i : i + n])
        next_word = tokens[i + n]
        
        # This will automatically count the occurrences
        # e.g., chain[("said", "the")]["hatter"] += 1
        chain[key_tuple][next_word] += 1
        
    return chain

def generate_text(chain, n, length=25):
    """Generates text by walking the weighted N-gram chain."""
    
    if not chain:
        return "The corpus was empty or too small to build a chain."

    current_key = random.choice(list(chain.keys()))
    generated_text = list(current_key)
    
    for _ in range(length - n):
        if current_key not in chain:
            break
            
        # --- This is the key change ---
        
        # 1. Get the dictionary of followers and their counts
        followers_with_counts = chain[current_key]
        
        # 2. Split into two separate lists: followers and their weights
        followers = list(followers_with_counts.keys())
        weights = list(followers_with_counts.values())
        
        # 3. Use random.choices() to pick one, respecting the weights
        #    (It returns a list, so we take the first item [0])
        next_word = random.choices(followers, weights=weights, k=1)[0]
        
        # ----------------------------------
        
        generated_text.append(next_word)
        
        # Update the key
        new_key_list = list(current_key[1:]) + [next_word]
        current_key = tuple(new_key_list)
        
    return ' '.join(generated_text)

# --- --- ---
#     MAIN
# --- --- ---

FILE_PATH = '../data/corpus.txt'
TEXT_LENGTH = 30 

tokens = preprocess_text(FILE_PATH)

if tokens:
    chain = build_chain(tokens, N_GRAM_SIZE)
    
    # Optional: You could add a 'print(chain)' here to see
    # the new dictionary structure, but it will be HUGE.

    print(f"--- Generated Text (N-Gram: {N_GRAM_SIZE}, Weighted) ---")
    new_text = generate_text(chain, N_GRAM_SIZE, length=TEXT_LENGTH)
    print(new_text)