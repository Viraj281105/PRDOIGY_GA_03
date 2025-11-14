import string
import random

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

def build_chain(tokens):
    """Builds the Markov chain dictionary from a list of tokens."""
    chain = {}
    
    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i+1]
        
        if current_word not in chain:
            chain[current_word] = []
            
        chain[current_word].append(next_word)
        
    return chain

def generate_text(chain, length=25):
    """Generates text by walking the Markov chain."""
    
    # Check if the chain is empty
    if not chain:
        return "The corpus was empty or too small to build a chain."
        
    start_word = random.choice(list(chain.keys()))
    generated_text = [start_word]
    current_word = start_word
    
    for _ in range(length - 1):
        # Stop if we hit a word that has no followers
        if current_word not in chain:
            break
            
        followers = chain[current_word]
        next_word = random.choice(followers)
        
        generated_text.append(next_word)
        current_word = next_word
        
    return ' '.join(generated_text)

# --- --- ---
#     MAIN
# --- --- ---

# This path goes UP one level (from scripts) and DOWN into data
FILE_PATH = '../data/corpus.txt'
TEXT_LENGTH = 30 # You can change this

# 1. Process the text
tokens = preprocess_text(FILE_PATH)

if tokens:
    # 2. Build the chain
    chain = build_chain(tokens)

    # 3. Generate new text
    print(f"--- Generated Text (from {FILE_PATH}) ---")
    new_text = generate_text(chain, length=TEXT_LENGTH)
    print(new_text)