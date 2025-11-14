# 🤖 Generative AI Task 3: Markov Chain Text Generator

This project is a submission for the **Prodigy InfoTech Generative AI Internship (Task 3)**.

The objective is to implement a simple text generation algorithm using Markov chains. This task involves creating a statistical model that predicts the probability of the next word based on the previous sequence of words. This implementation was built iteratively, starting from a simple bigram model and evolving to a more complex, statistically accurate, weighted N-gram model.

---

## 📂 Project Structure

The project is organized into data and script folders, with three distinct iterations of the algorithm.

```
PRDOIGY_GA_03/
├── data/
│   └── corpus.txt        # The training text file (e.g., Alice in Wonderland)
├── scripts/
│   ├── v1_simple_chain.py  # Iteration 1: Simple Bigram Model
│   ├── v2_ngram_chain.py   # Iteration 2: N-Gram Model (Trigram)
│   └── v3_weighted_chain.py  # Iteration 3: Weighted N-Gram Model
└── README.md               # This file
```

---

## 🧠 How It Works: The Concept

A **Markov chain** is a statistical model that describes a sequence of possible events. The core principle, known as the **Markov Property**, is that the probability of the next event depends *only* on the current event (or a fixed number of previous events), not the entire history.

**For Text Generation:**
* **State:** A "state" is the current word or a sequence of words (e.g., `"the"` or `("the", "cat")`).
* **Transition:** This is the probability of moving from one state to another (e.g., the probability that the word `"sat"` follows the state `("the", "cat")`).

Our model builds this chain by "reading" a text file and counting the frequency of all word-to-word transitions.

---

## 🚀 Iterative Development

This project was built in three main iterations to demonstrate the refinement of the algorithm.

### Iteration 1: `v1_simple_chain.py` (The Bigram Model)

This is a **first-order Markov chain**, or a **bigram** model.

* **Logic:** The next word depends on *only one* previous word.
* **Architecture:** A simple Python dictionary where:
    * **Key:** The current word (e.g., `"the"`).
    * **Value:** A **list** of all words that have ever followed it (e.g., `['quick', 'cat', 'quick']`).
* **Flaw:** The model has almost no context. The generated text sounds random and disconnected because it only considers a single-word history.

### Iteration 2: `v2_ngram_chain.py` (The N-Gram Model)

This is a **second-order Markov chain**, or a **trigram** model. It uses an **N-gram** size of 2.

* **Improvement:** The model is given more context. The next word depends on the previous *two* words.
* **Architecture:** The dictionary key is upgraded from a string to a **tuple** (which can be a dictionary key).
    * **Key:** A tuple of the previous `N` words (e.g., `("the", "quick")`).
    * **Value:** A **list** of all words that have followed that specific two-word sequence (e.g., `['brown', 'blue']`).
* **Result:** The generated text is immediately more coherent, as the two-word context preserves short-term "memory."

### Iteration 3: `v3_weighted_chain.py` (The Weighted Model)

This is the final and most statistically accurate model. It refines the N-gram model by adding **probabilistic weighting**.

* **Improvement:** Instead of treating all possible next words as equally likely, this model respects their *actual frequency* in the text.
* **Architecture:** The "Value" in the dictionary is changed from a list to a `Counter` object (a specialized dictionary).
    * **Key:** A tuple of `N` words (e.g., `("said", "the")`).
    * **Value:** A **dictionary** mapping each follower word to its *count* (e.g., `{"hatter": 10, "king": 5, "dodo": 1}`).
* **Logic:** When generating text, we use `random.choices()` and pass in these counts as `weights`. This means the model is 10x more likely to pick "hatter" than "dodo" after "said the," just as it was in the original text.
* **Result:** This produces the most authentic and plausible-sounding text, as it accurately mimics the statistical patterns of the source corpus.

---

## ⚙️ How to Run

You can run any of the three scripts to see the algorithm's output at different stages.

### Prerequisites

* Python 3.x

### Steps

1.  **Clone (or download) this repository:**
    ```bash
    git clone [your-repo-url]
    cd PRDOIGY_GA_03
    ```

2.  **Add a Corpus:**
    Find a large plain text (`.txt`) file. [Project Gutenberg](https://www.gutenberg.org/) is a great source. Download a book (e.g., *Alice's Adventures in Wonderland*) and save it as `corpus.txt` inside the `data/` folder.

3.  **Run the Scripts:**
    Navigate to the `scripts` folder and run any of the Python files.

    ```bash
    cd scripts
    ```

    **To run the simple bigram model:**
    ```bash
    python v1_simple_chain.py
    ```

    **To run the N-gram model:**
    ```bash
    python v2_ngram_chain.py
    ```

    **To run the final weighted N-gram model:**
    ```bash
    python v3_weighted_chain.py
    ```

---

## 📊 Example Output

The following examples were generated using the text of *Alice's Adventures in Wonderland* as the corpus. Notice how the coherence improves with each iteration.

> **Note:** Your output will be different every time you run the scripts.

### v1 (Simple Bigram)
This text is very random, jumping between unrelated ideas.

```
--- Generated Text (from ../data/corpus.txt) ---
enjoy the lobster quadrille that done” she began in a twinkling begins with a grin” “they lived at the king and was soon make out who had not open air
```

### v2 (N-Gram)
The output is much better. The phrases (`"so i should be like then"` and `"and she swam about"`) are grammatically connected, though the overall sentence still wanders.

```
--- Generated Text (N-Gram Size: 2) ---
hatter “so i should be like then” and she swam about trying to put his shoes off “give your evidence” the king said to itself in a deep voice “are
```

### v3 (Weighted N-Gram)
This is the most plausible output. The phrases are natural (`"said the king said to herself"`, `"a new idea to alice"`) and are chosen based on the author's actual statistical habits.

```
--- Generated Text (N-Gram: 2, Weighted) ---
would manage it “they were obliged to have it explained” said the king said to herself “after such a new idea to alice and all her knowledge as there seemed
```