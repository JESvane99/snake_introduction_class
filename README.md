# Snake Game - Python Introduction Course

A comprehensive set of Jupyter notebooks that introduce Python fundamentals through building and exploring a Snake game using Python's `turtle` module. Suitable for classroom use with high school students.

**Language Note:** All notebooks are written in Danish.

## Notebooks Overview

### 1. **slangespil_uddannelse.ipynb** (Main Educational Notebook)
The primary learning resource for students. This notebook:
- Introduces key Python concepts progressively with guided steps
- Demonstrates variables, data types, functions, and control structures
- Shows how code changes directly affect program behavior
- Includes print statements and type demonstrations to build understanding
- Features the complete, working Snake game

**Best for:** First-time learners following along with instructor guidance

### 2. **slangespil_laerervejledning.ipynb** (Teacher's Guide)
Comprehensive instructor resource mirroring the educational notebook with:
- Pedagogical notes and learning objectives for each section
- Discussion questions and activity suggestions
- Common misconceptions to address
- Detailed explanations of complex concepts
- Tips for demonstrating concepts interactively

**Best for:** Teachers preparing lessons and explaining concepts

### 3. **slangespil_simpelt.ipynb** (Simplified Version)
A condensed version of the game with:
- All explanatory text removed
- Only the essential code cells
- Same game functionality as the main notebook
- Less intimidating for students who prefer minimal guidance

**Best for:** Students who want to focus purely on code without detailed explanations

### 4. **slangespil_fejljagt.ipynb** (Debugging Exercise)
A version intentionally containing bugs for students to find and fix:
- Multiple bugs with varying difficulty levels
- Hints provided as cell comments
- Bugs cover common programming errors:
  - Type errors (strings vs numbers)
  - Logic errors (incorrect operators)
  - Game mechanics issues (collision detection, scoring)
  - Data structure problems (lists vs tuples)

**Best for:** Hands-on debugging practice and reinforcing understanding

## How to Use

### For Students (Getting Started)
1. **Start with `slangespil_uddannelse.ipynb`**
   - Read the "Guided Steps" section at the top
   - Run all cells to play one round
   - Modify variables to see immediate effects
   - Try the "Free Exploration" section

2. **Experiment and Modify**
   - Change colors: `slange_farve = "blue"`
   - Adjust speed: `forsinkelse = 0.05`
   - Modify board size: `spil_bredde = 1200`
   - Re-run cells to see changes take effect

3. **Deepen Understanding**
   - Review the teacher's guide notes for deeper explanations
   - Try the debugging notebook to find and fix bugs
   - Use the simplified version if you prefer less text

### For Teachers (Running a Lesson)
1. **Preparation**
   - Review `slangespil_laerervejledning.ipynb` before class
   - Prepare examples of code modifications to demonstrate

2. **Live Demonstration**
   - Run the main notebook to show the working game
   - Change a variable and re-run to show dynamic behavior
   - Explain the learning objectives

3. **Guided Exploration**
   - Have students follow the guided steps
   - Pause at key concepts to discuss learning objectives
   - Encourage experimentation with code changes

4. **Free Exploration**
   - Let students modify and build on the game
   - Circulate and address questions
   - Use errors as teaching moments

5. **Wrap-up**
   - Review debugging notebook for common errors
   - Discuss what was learned about Python
   - Suggest extensions and next steps

## Key Learning Concepts

The notebooks introduce students to:
- **Variables and Data Types:** Integers, floats, strings, booleans, tuples
- **Operators:** Arithmetic (+, -, *, /, //), comparison (==, !=), logical (and, or)
- **Control Structures:** if/elif/else statements, while loops
- **Functions:** Definition, parameters, return values, global variables
- **Data Structures:** Lists, tuples, appending and iteration
- **Object-Oriented Programming:** Turtle objects, attributes, methods
- **Debugging:** Reading error messages, identifying and fixing bugs

## Requirements

- Python 3.7+ [tested with Python 3.14.2]
- Jupyter Notebook or JupyterLab
- No additional packages required (uses only built-in `turtle`, `time`, and `random` modules)

## Usage Instructions

### Anaconda Installation (Recommended for Beginners)

* Install Anaconda from https://www.anaconda.com/products/distribution
* Open Anaconda Navigator and launch Jupyter Notebook
* Navigate to the project directory and open the notebooks


#### Pure python installation and running notebooks

```bash
# Install Jupyter if you don't have it
pip install jupyter

# Navigate to the project directory
cd path/to/introduction_snake

# Start Jupyter
jupyter notebook

# Open any .ipynb file and run cells with Shift+Enter
```

## Attribution

The original game concept was based on https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900 and has been extensively rewritten and restructured for educational purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

