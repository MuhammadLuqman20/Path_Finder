"""
Main Execution File
AI Pathfinder - Uninformed Search Algorithms Visualizer
"""

import sys
from Grid_Environment import GridEnvironment
from Search_Algorithms import SearchAlgorithms
from Visualiser import InteractiveVisualizer, ConfigurableVisualizer
import matplotlib.pyplot as plt

def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║           AI PATHFINDER VISUALIZER                       ║
    ║         Uninformed Search Algorithms                     ║
    ║                                                          ║
    ║  Algorithms: BFS, DFS, UCS, DLS, IDDFS, Bidirectional    ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)

def main_gui():
    """Launch GUI-based interactive visualizer"""
    print("\nLaunching GUI Interface...")
    print("="*60)
    print("Use the configuration panel on the right to:")
    print("  1. Select algorithm (BFS, DFS, UCS, DLS, IDDFS, or Bidirectional)")
    print("  2. Configure grid size and obstacles")
    print("  3. Set start and goal positions")
    print("  4. Click 'Start Search' to run")
    print("="*60)
    
    visualizer = ConfigurableVisualizer()
    visualizer.show()

def main_terminal():
    """Legacy terminal-based interface"""
    print("\nWelcome to AI Pathfinder (Terminal Mode)!")
    print("This program visualizes uninformed search algorithms.")
    
    while True:
        choice = get_user_choice()
        
        if choice == 0:
            print("\nThank you for using AI Pathfinder!")
            print("Goodbye! 👋")
            sys.exit(0)
        
        # Setup grid
        rows, cols, obs_prob = setup_grid()
        grid_env = GridEnvironment(rows, cols, obs_prob)
        
        # Set start and target
        set_start_target(grid_env)
        
        # Visualization speed
        speed_choice = input("\nVisualization speed (fast/medium/slow, default medium): ").lower() or "medium"
        delay = {'fast': 0.01, 'medium': 0.05, 'slow': 0.2}.get(speed_choice, 0.05)
        
        # Create visualizer
        visualizer = InteractiveVisualizer(grid_env, delay=delay)
        
        # Run algorithm
        run_algorithm(choice, grid_env, visualizer)
        
        # Close visualizer
        visualizer.close()
        plt.close('all')
        
        # Continue?
        continue_choice = input("\nRun another algorithm? (y/n): ").lower()
        if continue_choice != 'y':
            print("\nThank you for using AI Pathfinder!")
            print("Goodbye! 👋")
            break

def get_user_choice():
    """Get algorithm choice from user"""
    print("\n" + "="*60)
    print("Select Algorithm:")
    print("="*60)
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Uniform-Cost Search (UCS)")
    print("4. Depth-Limited Search (DLS)")
    print("5. Iterative Deepening DFS (IDDFS)")
    print("6. Bidirectional Search")
    print("0. Exit")
    print("="*60)
    
    while True:
        try:
            choice = int(input("\nEnter your choice (0-6): "))
            if choice in [0, 1, 2, 3, 4, 5, 6]:
                return choice
            else:
                print("Invalid choice! Please select 1-6 or 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def setup_grid():
    """Setup grid with user-defined parameters"""
    print("\n" + "="*60)
    print("Grid Configuration")
    print("="*60)
    
    # Grid size
    while True:
        try:
            rows = int(input("Enter number of rows (10-30, default 15): ") or "15")
            cols = int(input("Enter number of columns (10-30, default 15): ") or "15")
            if 10 <= rows <= 30 and 10 <= cols <= 30:
                break
            print("Please enter values between 10 and 30.")
        except ValueError:
            print("Invalid input! Using default 15x15.")
            rows, cols = 15, 15
            break
    
    # Obstacle probability
    while True:
        try:
            obs_prob = float(input("Static obstacle probability (0.0-0.3, default 0.15): ") or "0.15")
            if 0.0 <= obs_prob <= 0.3:
                break
            print("Please enter a value between 0.0 and 0.3.")
        except ValueError:
            print("Invalid input! Using default 0.15.")
            obs_prob = 0.15
            break
    
    return rows, cols, obs_prob

def set_start_target(grid_env):
    """Set start and target positions"""
    print("\n" + "="*60)
    print("Setting Start and Target Positions")
    print("="*60)
    print(f"Grid size: {grid_env.rows}x{grid_env.cols}")
    print("Coordinates are (row, col) starting from (0, 0)")
    
    # Set start
    while True:
        try:
            start_input = input(f"Enter start position (e.g., 0 0) [default: 0 0]: ") or "0 0"
            start_row, start_col = map(int, start_input.split())
            if grid_env.is_valid(start_row, start_col) and grid_env.grid[start_row][start_col] != 1:
                grid_env.set_start(start_row, start_col)
                break
            print("Invalid position or obstacle present! Try again.")
        except:
            print("Invalid input! Using default (0, 0).")
            grid_env.set_start(0, 0)
            break
    
    # Set target
    while True:
        try:
            target_input = input(f"Enter target position (e.g., {grid_env.rows-1} {grid_env.cols-1}) [default: {grid_env.rows-1} {grid_env.cols-1}]: ") or f"{grid_env.rows-1} {grid_env.cols-1}"
            target_row, target_col = map(int, target_input.split())
            if grid_env.is_valid(target_row, target_col) and grid_env.grid[target_row][target_col] != 1:
                if (target_row, target_col) != (grid_env.start[0], grid_env.start[1]):
                    grid_env.set_target(target_row, target_col)
                    break
                print("Target cannot be same as start! Try again.")
            else:
                print("Invalid position or obstacle present! Try again.")
        except:
            print(f"Invalid input! Using default ({grid_env.rows-1}, {grid_env.cols-1}).")
            grid_env.set_target(grid_env.rows-1, grid_env.cols-1)
            break

def run_algorithm(choice, grid_env, visualizer):
    """Run selected algorithm"""
    search = SearchAlgorithms(grid_env)
    start = grid_env.start
    target = grid_env.target
    
    print("\n" + "="*60)
    print("Running Algorithm...")
    print("="*60)
    print("Watch the visualization window!")
    print("Controls: Use Pause/Resume and Speed buttons")
    print("="*60)
    
    result = None
    algorithm_name = ""
    
    try:
        if choice == 1:  # BFS
            algorithm_name = "Breadth-First Search (BFS)"
            result = search.bfs(start, target, visualizer)
        
        elif choice == 2:  # DFS
            algorithm_name = "Depth-First Search (DFS)"
            result = search.dfs(start, target, visualizer)
        
        elif choice == 3:  # UCS
            algorithm_name = "Uniform-Cost Search (UCS)"
            result = search.ucs(start, target, visualizer)
        
        elif choice == 4:  # DLS
            depth_limit = int(input("Enter depth limit (default 20): ") or "20")
            algorithm_name = "Depth-Limited Search (DLS)"
            result = search.depth_limited_search(start, target, depth_limit, visualizer)
        
        elif choice == 5:  # IDDFS
            max_depth = int(input("Enter maximum depth (default 50): ") or "50")
            algorithm_name = "Iterative Deepening DFS (IDDFS)"
            result = search.iterative_deepening_dfs(start, target, max_depth, visualizer)
        
        elif choice == 6:  # Bidirectional
            algorithm_name = "Bidirectional Search"
            result = search.bidirectional_search(start, target, visualizer)
        
        # Show final result
        stats = {
            'explored': search.explored_history,
            'info': '',
            'visit_order': search.visit_order
        }
        visualizer.show_final_result(result, algorithm_name, stats)
        
        # Print results
        print("\n" + "="*60)
        print("Results:")
        print("="*60)
        if result:
            print(f"  Path length: {len(result)}")
            print(f"  Nodes explored: {len(search.explored_history)}")
        else:
            print("✗ No path found!")
            print(f"  Nodes explored: {len(search.explored_history)}")
        print("="*60)
        
        input("\nPress Enter to continue...")
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main execution function with mode selection"""
    print_banner()
    
    print("\n" + "="*60)
    print("Select Mode:")
    print("="*60)
    print("1. GUI Mode (Recommended) - Interactive interface")
    print("2. Terminal Mode - Command-line interface")
    print("0. Exit")
    print("="*60)
    
    while True:
        try:
            mode = input("\nEnter your choice (0-2): ")
            if mode == '1':
                main_gui()
                break
            elif mode == '2':
                main_terminal()
                break
            elif mode == '0':
                print("\nGoodbye! 👋")
                sys.exit(0)
            else:
                print("Invalid choice! Please enter 1, 2, or 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        print("Goodbye! 👋")
        sys.exit(0)
