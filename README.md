# convert-Regex-to-DFA

A Python-based tool that compiles Regular Expressions (RegEx) into Deterministic Finite Automata (DFA) through a step-by-step mathematical approach. The project also visually renders the generated NFA and DFA graphs using Graphviz.

---

## 🧠 Algorithms Used

This project simulates the core Lexical Analysis phase of a compiler using the following algorithms:

1. **Shunting Yard Algorithm:** Parses the standard regular expression (infix) and converts it into Postfix notation, explicitly adding concatenation dots.
2. **Thompson's Construction:** Converts the postfix regular expression into a Non-deterministic Finite Automaton (NFA) using epsilon transitions.
3. **Subset Construction (Powerset Construction):** Eliminates non-determinism by converting the NFA into a DFA. It calculates epsilon-closures to group NFA states into single, unique DFA states.

---

## 📂 Project Structure

* `Parser.py`: Handles the Shunting Yard algorithm and string processing.
* `NFA.py`: Contains the `NFA` and `State` classes, and implements Thompson's construction (union, concat, star).
* `DFA.py`: Implements the Subset Construction algorithm to determinize the NFA.
* `Graph.py`: The main execution script. It ties all modules together and uses `graphviz` to draw the state machines.
* `.github/workflows/generate_graphs.yml`: CI/CD automation to run the code and generate graphs directly on GitHub.

---

## ⚙️ How to Use

### 1. Run on GitHub Actions (No Installation Required!)
Thanks to GitHub Actions, you don't even need to clone the repo to generate graphs:
1. Go to the **Actions** tab in this repository.
2. Click on **Generate Automata Graphs** on the left menu.
3. Click **Run workflow**, enter your custom Regex (e.g., `(a|b)*abb`), and hit run.
4. Download your generated NFA and DFA `.png` graphs from the **Artifacts** section at the bottom of the run page.

### 2. Run Locally
To run the project on your own machine:

**Prerequisites:** You must have Python installed, as well as the Graphviz system package.
* Ubuntu: `sudo apt install graphviz`
* Windows: Download from the [Graphviz website](https://graphviz.org/download/) and add it to your system PATH.

**Installation & Execution:**
```bash
# Clone the repository
git clone [https://github.com/aminpy83/convert-Regex-to-DFA.git](https://github.com/aminpy83/convert-Regex-to-DFA.git)
cd convert-Regex-to-DFA

# Install the Python requirements
pip install graphviz

# Run the program with your regex
python Graph.py "(a|b)*abb"
