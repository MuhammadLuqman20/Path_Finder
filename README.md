AI Pathfinder - Uninformed Search Algorithms Visualizer

An interactive visualization tool for uninformed search algorithms with real-time GUI feedback and step-by-step animation.

📋 Overview

This project implements and visualizes six uninformed search algorithms:

Breadth-First Search (BFS)

Depth-First Search (DFS)

Uniform-Cost Search (UCS)

Depth-Limited Search (DLS)

Iterative Deepening Depth-First Search (IDDFS)

Bidirectional Search

The application features an interactive Matplotlib-based GUI that allows users to watch algorithms explore the search space in real-time with step-by-step visualization.

🔗 Repository Link:
https://github.com/MuhammadLuqman20/Path_Finder

✨ Features

Interactive GUI Visualization with pause/resume controls and speed adjustment

Step-by-Step Animation of node exploration

6-Directional Movement (strict clockwise order with specific diagonals)

Clear Color Coding for frontier, explored nodes, and final path

Customizable Grid Size, obstacle density, start/target positions

Algorithm Performance Statistics

Support for both GUI Mode and Terminal Mode

🚀 Installation
Prerequisites

Python 3.8 or higher

pip (Python package installer)

Install Dependencies
pip install -r Testing-&-Setup/Requirements.txt

📖 Usage
▶ Run the Application
python Main-Files/Main.py

🎯 Algorithms Implemented
1. Breadth-First Search (BFS)

Time Complexity: O(b^d)

Space Complexity: O(b^d)

Complete: ✅

Optimal: ✅ (uniform cost)

2. Depth-First Search (DFS)

Time Complexity: O(b^m)

Space Complexity: O(bm)

Complete: ❌

Optimal: ❌

3. Uniform-Cost Search (UCS)

Time Complexity: O(b^(1+⌊C*/ε⌋))

Space Complexity: O(b^(1+⌊C*/ε⌋))

Complete: ✅

Optimal: ✅

4. Depth-Limited Search (DLS)

Time Complexity: O(b^l)

Space Complexity: O(bl)

Complete: ❌

Optimal: ❌

5. Iterative Deepening DFS (IDDFS)

Time Complexity: O(b^d)

Space Complexity: O(bd)

Complete: ✅

Optimal: ✅ (uniform cost)

6. Bidirectional Search

Time Complexity: O(b^(d/2))

Space Complexity: O(b^(d/2))

Complete: ✅

Optimal: ✅

📁 Project Structure
Path_Finder/
├── Main-Files/
│   ├── Main.py
│   ├── Grid_Environment.py
│   ├── Search_Algorithms.py
│   └── Visualiser.py
├── Testing-&-Setup/
│   ├── Requirements.txt
│   └── Test_Algorithms.py
├── GIT_COMMIT_GUIDE.md
└── README.md

🎨 Color Legend

White → Empty Cell

Dark Gray → Static Obstacle

Blue (S) → Start Position

Green (T) → Target Position

Orange → Frontier Nodes

Red → Explored Nodes

Purple → Final Path

🔄 Movement Pattern (Strict Clockwise Order)

The algorithm expands neighbors in this exact order:

Up (-1, 0)

Right (0, 1)

Bottom (1, 0)

Bottom-Right (1, 1) — Diagonal

Left (0, -1)

Top-Left (-1, -1) — Diagonal

⚠️ Top-Right and Bottom-Left diagonals are NOT explored.

🛠️ Dependencies

matplotlib (>=3.5.0)

numpy (>=1.21.0)

Install using:

pip install -r Testing-&-Setup/Requirements.txt

👤 Author

Muhammad Luqman
Student ID: 23F-0640

GitHub: https://github.com/MuhammadLuqman20

Repository: https://github.com/MuhammadLuqman20/Path_Finder

Email: muhammadluqman66699@gmail.com

📚 Academic Information

Course: Artificial Intelligence
Assignment: AI Assignment 1 – Uninformed Search Algorithms
Semester: Spring 2026
