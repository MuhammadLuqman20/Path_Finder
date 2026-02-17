# AI Pathfinder - Uninformed Search Algorithms Visualizer

An interactive visualization tool for uninformed search algorithms with real-time GUI feedback and step-by-step animation.


## 📋 Overview

This project implements and visualizes six uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Depth-Limited Search (DLS)
- Iterative Deepening Depth-First Search (IDDFS)
- Bidirectional Search

The application features an interactive matplotlib-based GUI that allows users to watch algorithms explore the search space in real-time with step-by-step visualization.

---

## ✨ Features

- Interactive GUI Visualization with pause/resume and speed control  
- Step-by-step animation of node exploration  
- 6-Directional movement (Clockwise with Bottom-Right & Top-Left diagonals only)  
- Color-coded visualization (Frontier, Explored, Path, Obstacles)  
- Customizable grid size, obstacle density, start/goal positions  
- Algorithm statistics display (nodes explored, path length)  
- Terminal mode + GUI mode support  


## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies

```bash
pip install -r Testing-&-Setup/Requirements.txt


▶️ Run the Application
python Main-Files/Main.py

🎯 Implemented Algorithms
| Algorithm     | Complete | Optimal | Memory Efficient |
| ------------- | -------- | ------- | ---------------- |
| BFS           | ✅        | ✅       | ❌                |
| DFS           | ❌        | ❌       | ✅                |
| UCS           | ✅        | ✅       | ❌                |
| DLS           | ❌        | ❌       | ✅                |
| IDDFS         | ✅        | ✅       | ✅                |
| Bidirectional | ✅        | ✅       | ❌                |

🎨 Color Legend
⚪ White → Empty Cell
⬛ Dark Gray → Obstacle
🔵 Blue → Start
🟢 Green → Target
🟠 Orange → Frontier
🔴 Red → Explored
🟣 Purple → Final Path

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
├── README.md


🛠️ Dependencies
matplotlib (>=3.5.0)
numpy (>=1.21.0)
Install manually if needed:
pip install matplotlib numpy

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

📞 Support
If you face any issue:
Open an issue in the repository
Contact via email



