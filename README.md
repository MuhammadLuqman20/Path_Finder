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
The application features an interactive matplotlib-based GUI that allows users to watch algorithms explore the search space in real-time with step-by-step visualization.

✨ Features
Interactive GUI Visualization: Real-time visualization with pause/resume controls and speed adjustment
Step-by-Step Animation: Watch how each algorithm explores the grid node by node
6-Directional Movement: Clockwise movement pattern with specific diagonals (Bottom-Right and Top-Left only)
Visual Distinction: Clear color-coding for frontier nodes, explored nodes, and final path
User-Defined Configuration: Customize grid size, start/target positions, obstacle density, and algorithm parameters
Multiple Algorithms: Compare behavior of 6 different uninformed search algorithms
Algorithm Statistics: Display nodes explored, path length, and execution details
🚀 Installation
Prerequisites
Python 3.8 or higher
pip (Python package installer)
Steps
Clone the repository

git clone https://github.com/AyaanHassanShah/AI_A1_22F_23F-0711.git
cd AI_A1_22F_23F-0711
Install dependencies

pip install -r Testing-&-Setup/Requirements.txt
📖 Usage
Running the Application
python Main-Files/Main.py
Using the Interface
GUI Mode (Recommended):

Select Algorithm: Choose from BFS, DFS, UCS, DLS, IDDFS, or Bidirectional Search
Configure Grid: Set grid dimensions (10-30) and obstacle density (0-0.3)
Set Positions: Define start and goal positions
Set Parameters: Configure depth limits for DLS/IDDFS if needed
Adjust Speed: Use the slider to control visualization speed (fast to slow)
Start Search: Click the green "Start" button to run the algorithm
Watch Visualization: Observe step-by-step exploration with color-coded cells
View Results: See the final path and statistics
Terminal Mode:

Select algorithm from menu (1-6)
Configure grid parameters
Set start and target positions
Watch the animated visualization
Example Session
Select Algorithm:
1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Uniform-Cost Search (UCS)
4. Depth-Limited Search (DLS)
5. Iterative Deepening DFS (IDDFS)
6. Bidirectional Search
0. Exit

Enter your choice: 1

Grid Configuration
Enter number of rows (10-30): 15
Enter number of columns (10-30): 15
Enter obstacle probability (0.0-0.3): 0.15

Enter start position (row col): 0 0
Enter target position (row col): 14 14

Visualization speed (fast/medium/slow): medium
🎯 Algorithms
1. Breadth-First Search (BFS)
Description: Explores nodes level by level using a queue
Time Complexity: O(b^d) where b is branching factor, d is solution depth
Space Complexity: O(b^d)
Complete: Yes (in finite spaces)
Optimal: Yes (for uniform step costs)
2. Depth-First Search (DFS)
Description: Explores as far as possible along each branch using a stack
Time Complexity: O(b^m) where m is maximum depth
Space Complexity: O(bm)
Complete: No (can get stuck in infinite loops)
Optimal: No
3. Uniform-Cost Search (UCS)
Description: Explores nodes in order of increasing path cost
Time Complexity: O(b^(1+⌊C*/ε⌋)) where C* is optimal cost
Space Complexity: O(b^(1+⌊C*/ε⌋))
Complete: Yes (if step costs > 0)
Optimal: Yes
4. Depth-Limited Search (DLS)
Description: Explores paths up to a specified depth limit
Time Complexity: O(b^l) where l is depth limit
Space Complexity: O(bl)
Complete: No (may miss solution beyond depth limit)
Optimal: No
5. Iterative Deepening DFS (IDDFS)
Description: Repeatedly applies DLS with increasing depth limits
Time Complexity: O(b^d) where d is solution depth
Space Complexity: O(bd)
Complete: Yes (in finite spaces)
Optimal: Yes (for uniform step costs)
6. Bidirectional Search
Description: Searches simultaneously from start and target until they meet
Time Complexity: O(b^(d/2))
Space Complexity: O(b^(d/2))
Complete: Yes
Optimal: Yes (with appropriate strategy)
📊 Performance Comparison
Algorithm	Time Complexity	Space Complexity	Memory Efficient	Optimal	Complete
BFS	O(b^d)	O(b^d)	❌	✅	✅
DFS	O(b^m)	O(bm)	✅	❌	❌
UCS	O(b^(1+⌊C*/ε⌋))	O(b^(1+⌊C*/ε⌋))	❌	✅	✅
DLS	O(b^l)	O(bl)	✅	❌	❌
IDDFS	O(b^d)	O(bd)	✅	✅	✅
Bidirectional	O(b^(d/2))	O(b^(d/2))	❌	✅	✅
📁 Project Structure
AI-Path-Finder/
├── Main-Files/
│   ├── Main.py                 # Main application entry point
│   ├── Grid_Environment.py     # Grid management and obstacle handling
│   ├── Search_Algorithms.py    # Algorithm implementations
│   └── Visualiser.py          # GUI visualization components
├── Testing-&-Setup/
│   ├── Requirements.txt        # Project dependencies
│   └── Test_Algorithms.py      # Unit tests
├── GIT_COMMIT_GUIDE.md        # Git workflow guide
└── README.md                   # This file
🎨 Color Legend
White: Empty cell
Dark Gray: Static obstacle
Blue (S): Start position
Green (T): Target/Goal position
Orange: Frontier nodes (in queue/stack, waiting to be explored)
Red: Explored nodes (already visited)
Purple: Final path from Start to Target
🛠️ Technical Details
Grid Environment
Support for 6-directional movement (specific diagonals only)
Static obstacles with configurable probability
Neighbor generation in strict clockwise order
Movement Pattern (Strict Clockwise Order)
The algorithm explores neighbors in this specific order:

6  1  X
 ↖ ↑  
5 ← • → 2
    ↓ ↘
X  3  4
Order:

Up (-1, 0)
Right (0, 1)
Bottom (1, 0)
Bottom-Right (1, 1) - Diagonal
Left (0, -1)
Top-Left (-1, -1) - Diagonal
Note: Top-Right and Bottom-Left diagonals are NOT explored as per task requirements.

Visualization Features
Real-time Updates: Grid updates after each step showing frontier and explored nodes
Step-by-Step Animation: Configurable delay between steps (0.001s to 0.5s)
Color-Coded Cells: Easy distinction between different node types
Interactive Controls: Pause/Resume, Speed adjustment, Start/Stop/Reset buttons
Algorithm Statistics: Live updates of explored node count, path length, and current state
Final Path Highlighting: Clear visualization of the solution path
🐛 Troubleshooting
Issue: Matplotlib window doesn't appear
Solution: Ensure you're not running in a headless environment. If using remote connection, enable X11 forwarding.

Issue: "No path found" message
Solution: Try reducing obstacle density or increasing grid size. Some configurations may not have valid paths.

Issue: Slow visualization
Solution: Use the "Faster" button or reduce grid size for better performance.

Issue: Import errors
Solution: Ensure all dependencies are installed:

pip install -r Testing-&-Setup/Requirements.txt
📚 Dependencies
matplotlib (>=3.5.0): GUI visualization
numpy (>=1.21.0): Grid operations and array management
🤝 Contributing
This is an academic project for AI Assignment 1. For suggestions or improvements:

Fork the repository
Create a feature branch
Make your changes
Submit a pull request
📝 License
This project is created for educational purposes as part of an AI course assignment.

👤 Author
Muhammad Luqman

Student ID: 23F-0640
GitHub: @MuhammadLuqman20
Email: muhammadluqman66699@gmail.com
🙏 Acknowledgments
Course: Artificial Intelligence
Assignment: AI Assignment 1 - Uninformed Search Algorithms
Semester: Spring 2026
📞 Support
For questions or issues:

Create an issue in the repository
Contact via email: muhammadluqman66699@gmail.com
Note: This project demonstrates uninformed search algorithms with interactive visualization. It's designed for educational purposes to understand algorithm behavior and performance characteristics.
