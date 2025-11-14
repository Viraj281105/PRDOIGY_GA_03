import string
import random

# We can now control the 'memory' of our model.
# N_GRAM_SIZE = 1 (Bigram model, like v1)
# N_GRAM_SIZE = 2 (Trigram model, uses 2 words to predict the 3rd)
# N_GRAM_SIZE = 3 (4-gram model, uses 3 words to predict the 4th)
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
    Builds an N-gram Markov chain dictionary.
    
    The keys are tuples of (n) words, and the values are
    lists of the words that follow those n-grams.
    """
    chain = {}
    
    # We need at least n+1 tokens to make one n-gram pair
    if len(tokens) < n + 1:
        return chain

    # Iterate through the tokens, stopping n words before the end
    for i in range(len(tokens) - n):
        # Create the n-gram key as a tuple
        # A tuple is used because it's "hashable" (can be a dict key)
        key_tuple = tuple(tokens[i : i + n])
        
        # The word that follows this n-gram
        next_word = tokens[i + n]
        
        if key_tuple not in chain:
            chain[key_tuple] = []
            
        chain[key_tuple].append(next_word)
        
    return chain

def generate_text(chain, n, length=25):
    """Generates text by walking the N-gram Markov chain."""
    
    if not chain:
        return "The corpus was empty or too small to build a chain."

    # Start by picking a random key from the chain
    current_key = random.choice(list(chain.keys()))
    
    # Initialize our generated text with the words from the first key
    generated_text = list(current_key)
    
    for _ in range(length - n):
        # Stop if our current key isn't in the chain
        # (This happens if we hit the end of the corpus)
        if current_key not in chain:
            break
            
        # Get the list of possible next words
        followers = chain[current_key]
        
        # Pick one at random
        next_word = random.choice(followers)
        
        # Add the new word to our text
        generated_text.append(next_word)
        
        # --- This is the key part ---
        # Update the current_key to be the *last n words*
        # We take the last (n-1) words from our old key and add the new word
        new_key_list = list(current_key[1:]) + [next_word]
        current_key = tuple(new_key_list)
        
    return ' '.join(generated_text)

# --- --- ---
#     MAIN
# --- --- ---

FILE_PATH = '../data/corpus.txt'
TEXT_LENGTH = 30 # You can still change this

# 1. Process the text
tokens = preprocess_text(FILE_PATH)

if tokens:
    # 2. Build the chain (now passing in N_GRAM_SIZE)
    chain = build_chain(tokens, N_GRAM_SIZE)

    # 3. Generate new text
    print(f"--- Generated Text (N-Gram Size: {N_GRAM_SIZE}) ---")
    new_text = generate_text(chain, N_GRAM_SIZE, length=TEXT_LENGTH)
    print(new_text)