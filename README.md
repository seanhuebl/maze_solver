# Maze Generator and DFS Solver

A graphical Python application that generates a randomized maze and animates a depth-first-search (DFS) solution, including visible backtracking.

## Project background

This repository was completed as a Boot.dev guided project in September 2024. Boot.dev supplied the project requirements and learning sequence; the Python implementation was written independently without supplied solution code.

## Features

- Randomized maze generation using recursive DFS/backtracking
- Animated DFS traversal with successful moves and backtracking paths
- Object-oriented design for the maze, cells, drawing primitives, and window
- Optional seeded generation for repeatable behavior
- Unit tests for grid dimensions, entrance and exit behavior, and deterministic solving

## Requirements

- Python 3.8 or newer
- Tkinter

Tkinter is included with many Python installations. On Ubuntu or Debian, install it with:

~~~bash
sudo apt-get install python3-tk
~~~

## Run the application

~~~bash
git clone https://github.com/seanhuebl/maze_solver.git
cd maze_solver
python3 src/main.py
~~~

Alternatively, on macOS or Linux:

~~~bash
./main.sh
~~~

## Run the tests

~~~bash
python3 -m unittest discover -s src -p "test*.py"
~~~

Alternatively:

~~~bash
./test.sh
~~~

## Project structure

- `src/main.py` configures and starts the visualization.
- `src/maze.py` generates and solves the maze.
- `src/cell.py` represents individual cells and draws traversal moves.
- `src/line.py` provides drawing primitives.
- `src/window.py` manages the Tkinter canvas and event loop.
- `src/tests.py` contains the unit tests.

## Implementation note

The internal grid is organized around x/y coordinates, so the outer collection represents columns and the inner collection represents rows. This matches the visualization's coordinate model, even though row-major ordering is more conventional for matrix-oriented code.
