# Simulated-Annealing-Sudoku-Solver
Creates and solves sudoku puzzles using simulated annealing optimization method.

<br>

>To solve a sudoku puzzle, one must write all numerals from 1 to 9 into 9x9 grid board, with no repetetition across rows, columns nor 3x3 blocks.
>There are 6, 670, 903, 752, 021, 072, 936, 960 (10^21) possible solutions to solve a sudoku puzzle, which makes classic brute force approaches inconvenient.
>This program creates valid sudoku puzzles and solves them using simulated annealing method.
>Simulated annealing is a metaheuristic technique for approximating the global optimum of a given function.

<br>

![](https://github.com/atlasrule/Simulated-Annealing-Sudoku-Solver/blob/main/sudo.gif)

<br>

### How It Works?
>Program randomly fills every 3x3 block with random values from 1 to 9 and in each step it randomly swaps two numbers across blocks, and calculates the fitness value.  
>For sudoku problem defined fitness as a value to minimize. So less repetitions means closer we get to the global solution and zero fitness means puzzle has been solved.
>With each step we calculate the sum of each rows' and columns' numeral repetition numbers, and adjust the temperature until the puzzle is solved.
>To find the global minima, board states with better fitness values usualy accepted and annealing method gives worse states a chance and gradually lowers the worse chances until global optima is found. This process is called cooling. Initial temperature defines the stochasticity of the process.

<br>

### Usage
Run main.py, feel free to edit.

