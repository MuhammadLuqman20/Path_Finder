"""
Visualizer Module
Interactive matplotlib-based GUI for pathfinding visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, TextBox, RadioButtons, Slider
import numpy as np
import time

class PathfindingVisualizer:
    def __init__(self, grid_env, delay=0.05):
        """
        Initialize visualizer
        
        Args:
            grid_env: GridEnvironment instance
            delay: Delay between visualization steps (seconds)
        """
        self.grid_env = grid_env
        self.delay = delay
        
        # Color scheme
        self.colors = {
            'empty': '#FFFFFF',      # White
            'obstacle': '#2C3E50',   # Dark gray
            'start': '#3498DB',      # Blue
            'target': '#2ECC71',     # Green
            'frontier': '#F39C12',   # Orange
            'explored': '#E74C3C',   # Red
            'path': '#9B59B6'        # Purple
        }
        
        # Setup figure
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.fig.canvas.manager.set_window_title("GOOD PERFORMANCE TIME APP")
        
        # Initialize grid display
        self.setup_grid()
        
        plt.ion()  # Interactive mode
        plt.show()
        
    def setup_grid(self):
        """Setup initial grid display"""
        self.ax.clear()
        self.ax.set_xlim(-0.5, self.grid_env.cols - 0.5)
        self.ax.set_ylim(-0.5, self.grid_env.rows - 0.5)
        self.ax.set_aspect('equal')
        self.ax.invert_yaxis()  # Invert y-axis so (0,0) is top-left
        
        # Grid lines
        for i in range(self.grid_env.rows + 1):
            self.ax.axhline(y=i - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        for j in range(self.grid_env.cols + 1):
            self.ax.axvline(x=j - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        
        # Remove tick labels
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Title
        self.ax.set_title("GOOD PERFORMANCE TIME APP", fontsize=16, fontweight='bold', pad=20)
        
    def draw_cell(self, row, col, color, alpha=1.0):
        """Draw a colored cell at specified position"""
        rect = patches.Rectangle(
            (col - 0.5, row - 0.5),
            1, 1,
            linewidth=0,
            edgecolor='none',
            facecolor=color,
            alpha=alpha
        )
        self.ax.add_patch(rect)
        
    def draw_circle(self, row, col, color, size=0.3):
        """Draw a circle marker at specified position"""
        circle = patches.Circle(
            (col, row),
            size,
            color=color,
            zorder=10
        )
        self.ax.add_patch(circle)
        
    def update(self, frontier, explored, path, algorithm_name="Search", depth_info="", visit_order=None):
        """
        Update visualization
        
        Args:
            frontier: List of positions in frontier
            explored: List of explored positions
            path: List of positions in final path
            algorithm_name: Name of algorithm being visualized
            depth_info: Additional information to display
            visit_order: Dictionary mapping position to visit sequence number
        """
        self.setup_grid()
        
        # Draw static obstacles
        for i in range(self.grid_env.rows):
            for j in range(self.grid_env.cols):
                if self.grid_env.grid[i][j] == 1:
                    self.draw_cell(i, j, self.colors['obstacle'])
        
        # Draw explored nodes with visit order numbers
        for pos in explored:
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['explored'], alpha=0.6)
                # Add visit order number in top-left corner
                if visit_order and pos in visit_order:
                    self.ax.text(pos[1] - 0.4, pos[0] - 0.4, str(visit_order[pos]), 
                               ha='left', va='top',
                               fontsize=8, color='white', fontweight='bold')
        
        # Draw frontier nodes
        for pos in frontier:
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['frontier'], alpha=0.8)
        
        # Draw path
        for i, pos in enumerate(path):
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['path'], alpha=0.9)
                # Add path numbers
                self.ax.text(pos[1], pos[0], str(i), ha='center', va='center',
                           fontsize=8, color='white', fontweight='bold')
        
        # Draw start position
        if self.grid_env.start:
            self.draw_cell(self.grid_env.start[0], self.grid_env.start[1], 
                          self.colors['start'])
            self.ax.text(self.grid_env.start[1], self.grid_env.start[0], 'S',
                       ha='center', va='center', fontsize=14, color='white', fontweight='bold')
        
        # Draw target position
        if self.grid_env.target:
            self.draw_cell(self.grid_env.target[0], self.grid_env.target[1],
                          self.colors['target'])
            self.ax.text(self.grid_env.target[1], self.grid_env.target[0], 'T',
                       ha='center', va='center', fontsize=14, color='white', fontweight='bold')
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor=self.colors['start'], label='Start (S)'),
            patches.Patch(facecolor=self.colors['target'], label='Target (T)'),
            patches.Patch(facecolor=self.colors['obstacle'], label='Obstacle'),
            patches.Patch(facecolor=self.colors['frontier'], label='Frontier'),
            patches.Patch(facecolor=self.colors['explored'], label='Explored'),
            patches.Patch(facecolor=self.colors['path'], label='Path')
        ]
        self.ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1),
                      fontsize=9, framealpha=0.9)
        
        # Add algorithm info
        info_text = f"Algorithm: {algorithm_name}\n{depth_info}"
        info_text += f"\nExplored: {len(explored)} nodes"
        if path:
            info_text += f"\nPath Length: {len(path)}"
        
        self.ax.text(0.02, 1.02, info_text,
                    transform=self.ax.transAxes,
                    fontsize=10,
                    verticalalignment='bottom',
                    horizontalalignment='left',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # Update display
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        time.sleep(self.delay)
        
    def show_final_result(self, path, algorithm_name, stats):
        """
        Show final result with statistics
        
        Args:
            path: Final path
            algorithm_name: Name of algorithm
            stats: Dictionary with statistics
        """
        self.update(
            frontier=[],
            explored=stats.get('explored', []),
            path=path if path else [],
            algorithm_name=algorithm_name,
            depth_info=f"Completed! {stats.get('info', '')}",
            visit_order=stats.get('visit_order', {})
        )
        
        # Add completion message only if no path found
        if not path:
            message = "✗ No Path Found!"
            color = 'red'
            
            self.ax.text(0.5, 0.5, message,
                        transform=self.ax.transAxes,
                        fontsize=20,
                        fontweight='bold',
                        ha='center',
                        va='center',
                        color=color,
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor=color, linewidth=3))
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    def close(self):
        """Close the visualization window"""
        plt.close(self.fig)


class InteractiveVisualizer(PathfindingVisualizer):
    """Enhanced visualizer with interactive features"""
    
    def __init__(self, grid_env, delay=0.05):
        super().__init__(grid_env, delay)
        
        # Add buttons for interaction
        self.setup_buttons()
        
    def setup_buttons(self):
        """Setup interactive buttons"""
        from matplotlib.widgets import Button
        
        # Pause/Resume button
        ax_pause = plt.axes([0.7, 0.02, 0.1, 0.04])
        self.btn_pause = Button(ax_pause, 'Pause')
        self.paused = False
        
        def toggle_pause(event):
            self.paused = not self.paused
            self.btn_pause.label.set_text('Resume' if self.paused else 'Pause')
        
        self.btn_pause.on_clicked(toggle_pause)
        
        # Speed control
        ax_faster = plt.axes([0.82, 0.02, 0.08, 0.04])
        self.btn_faster = Button(ax_faster, 'Faster')
        
        def make_faster(event):
            self.delay = max(0.001, self.delay * 0.5)
            print(f"Speed increased! Delay: {self.delay:.3f}s")
        
        self.btn_faster.on_clicked(make_faster)
        
        ax_slower = plt.axes([0.6, 0.02, 0.08, 0.04])
        self.btn_slower = Button(ax_slower, 'Slower')
        
        def make_slower(event):
            self.delay = min(1.0, self.delay * 2)
            print(f"Speed decreased! Delay: {self.delay:.3f}s")
        
        self.btn_slower.on_clicked(make_slower)
        
    def update(self, frontier, explored, path, algorithm_name="Search", depth_info=""):
        """Override update to respect pause state"""
        while self.paused:
            plt.pause(0.1)
        
        super().update(frontier, explored, path, algorithm_name, depth_info)


class ConfigurableVisualizer:
    """Visualizer with configuration panel for GUI-based inputs"""
    
    def __init__(self):
        """Initialize the configurable visualizer with control panel"""
        # Create figure with subplots
        self.fig = plt.figure(figsize=(18, 10))
        self.fig.canvas.manager.set_window_title("AI Pathfinder - Interactive Visualizer")
        
        # Main visualization area (left side) - adjusted to prevent overlap
        self.ax_main = plt.subplot2grid((10, 10), (0, 0), colspan=6, rowspan=10)
        
        # Configuration area (right side)
        self.setup_config_panel()
        
        # State variables
        self.config = {
            'rows': 15,
            'cols': 15,
            'obs_prob': 0.15,
            'start_row': 0,
            'start_col': 0,
            'target_row': 14,
            'target_col': 14,
            'algorithm': 'BFS',
            'depth_limit': 20,
            'max_depth': 50
        }
        
        self.grid_env = None
        self.visualizer = None
        self.running = False
        self.stop_flag = False
        self.speed_delay = 0.05  # Default delay in seconds
        
        plt.ion()
        plt.show()
        
    def setup_config_panel(self):
        """Setup the configuration panel with all input controls"""
        # Base positions for right panel
        panel_left = 0.685
        panel_width = 0.28
        input_height = 0.028
        
        # Title
        ax_title = plt.axes([panel_left, 0.93, panel_width, 0.05])
        ax_title.axis('off')
        ax_title.text(0.5, 0.5, 'Configuration Panel', 
                     ha='center', va='center', fontsize=14, fontweight='bold',
                     bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        
        # Algorithm Selection (Radio buttons)
        ax_algo = plt.axes([panel_left + 0.02, 0.75, panel_width - 0.04, 0.18])
        self.radio_algo = RadioButtons(ax_algo, 
                                       ('BFS', 'DFS', 'UCS', 'DLS', 'IDDFS', 'Bidirectional'),
                                       active=0)
        
        def on_algo_change(label):
            self.config['algorithm'] = label
            # Show/hide depth inputs based on algorithm
            if label == 'DLS':
                self.textbox_depth_limit.set_active(True)
                self.textbox_max_depth.set_active(False)
            elif label == 'IDDFS':
                self.textbox_depth_limit.set_active(False)
                self.textbox_max_depth.set_active(True)
            else:
                self.textbox_depth_limit.set_active(False)
                self.textbox_max_depth.set_active(False)
        
        self.radio_algo.on_clicked(on_algo_change)
        
        # Grid Configuration Section
        ax_grid_title = plt.axes([panel_left, 0.69, panel_width, 0.03])
        ax_grid_title.axis('off')
        ax_grid_title.text(0.02, 0.5, 'Grid Configuration', 
                          fontsize=15, fontweight='bold', color='darkblue')
        
        # Grid inputs
        ax_rows = plt.axes([panel_left, 0.65, panel_width, input_height])
        self.textbox_rows = TextBox(ax_rows, 'Rows (10-30):', initial='15')
        self.textbox_rows.on_submit(lambda text: self.update_config('rows', text))
        
        ax_cols = plt.axes([panel_left, 0.615, panel_width, input_height])
        self.textbox_cols = TextBox(ax_cols, 'Cols (10-30):', initial='15')
        self.textbox_cols.on_submit(lambda text: self.update_config('cols', text))
        
        ax_obs = plt.axes([panel_left, 0.58, panel_width, input_height])
        self.textbox_obs = TextBox(ax_obs, 'Obstacles (0-0.3):', initial='0.15')
        self.textbox_obs.on_submit(lambda text: self.update_config('obs_prob', text))
        
        # Start/Goal Configuration Section
        ax_pos_title = plt.axes([panel_left, 0.54, panel_width, 0.03])
        ax_pos_title.axis('off')
        ax_pos_title.text(0.02, 0.5, 'Start & Goal Positions', 
                         fontsize=15, fontweight='bold', color='darkblue')
        
        # Position inputs
        ax_start_row = plt.axes([panel_left, 0.50, panel_width, input_height])
        self.textbox_start_row = TextBox(ax_start_row, 'Start Row:', initial='0')
        self.textbox_start_row.on_submit(lambda text: self.update_config('start_row', text))
        
        ax_start_col = plt.axes([panel_left, 0.465, panel_width, input_height])
        self.textbox_start_col = TextBox(ax_start_col, 'Start Col:', initial='0')
        self.textbox_start_col.on_submit(lambda text: self.update_config('start_col', text))
        
        ax_target_row = plt.axes([panel_left, 0.43, panel_width, input_height])
        self.textbox_target_row = TextBox(ax_target_row, 'Goal Row:', initial='14')
        self.textbox_target_row.on_submit(lambda text: self.update_config('target_row', text))
        
        ax_target_col = plt.axes([panel_left, 0.395, panel_width, input_height])
        self.textbox_target_col = TextBox(ax_target_col, 'Goal Col:', initial='14')
        self.textbox_target_col.on_submit(lambda text: self.update_config('target_col', text))
        
        # Algorithm Parameters Section
        ax_param_title = plt.axes([panel_left, 0.35, panel_width, 0.03])
        ax_param_title.axis('off')
        ax_param_title.text(0.02, 0.5, 'Algorithm Parameters', 
                           fontsize=15, fontweight='bold', color='darkblue')
        
        # Algorithm-specific parameters
        ax_depth = plt.axes([panel_left, 0.31, panel_width, input_height])
        self.textbox_depth_limit = TextBox(ax_depth, 'Depth Limit (DLS):', initial='20')
        self.textbox_depth_limit.on_submit(lambda text: self.update_config('depth_limit', text))
        
        ax_max_depth = plt.axes([panel_left, 0.275, panel_width, input_height])
        self.textbox_max_depth = TextBox(ax_max_depth, 'Max Depth (IDDFS):', initial='50')
        self.textbox_max_depth.on_submit(lambda text: self.update_config('max_depth', text))
        self.textbox_max_depth.set_active(False)
        
        # Speed Control Slider
        ax_speed_title = plt.axes([panel_left, 0.23, panel_width, 0.03])
        ax_speed_title.axis('off')
        ax_speed_title.text(0.02, 0.5, 'Visualization Speed', 
                           fontsize=15, fontweight='bold', color='darkgreen')
        
        ax_speed = plt.axes([panel_left, 0.195, panel_width, 0.02])
        self.slider_speed = Slider(ax_speed, '', 0.001, 0.5, 
                                   valinit=0.05, valstep=0.001)
        # Add speed labels
        ax_speed_labels = plt.axes([panel_left, 0.175, panel_width, 0.015])
        ax_speed_labels.axis('off')
        ax_speed_labels.text(0.0, 0.5, 'Fast', fontsize=8, ha='left')
        ax_speed_labels.text(1.0, 0.5, 'Slow', fontsize=8, ha='right')
        
        def on_speed_change(val):
            self.speed_delay = val
            if hasattr(self, 'main_visualizer') and self.main_visualizer:
                self.main_visualizer.delay = val
        
        self.slider_speed.on_changed(on_speed_change)
        
        # Action Buttons (3 buttons now)
        button_width = (panel_width - 0.02) / 3
        ax_start = plt.axes([panel_left, 0.09, button_width, 0.04])
        self.btn_start = Button(ax_start, 'Start', color='lightgreen', hovercolor='green')
        self.btn_start.on_clicked(self.on_start_clicked)
        
        ax_stop = plt.axes([panel_left + button_width + 0.01, 0.09, button_width, 0.04])
        self.btn_stop = Button(ax_stop, 'Stop', color='orange', hovercolor='darkorange')
        self.btn_stop.on_clicked(self.on_stop_clicked)
        self.btn_stop.active = False  # Disabled initially
        
        ax_reset = plt.axes([panel_left + 2 * (button_width + 0.01), 0.09, button_width, 0.04])
        self.btn_reset = Button(ax_reset, 'Reset', color='lightcoral', hovercolor='red')
        self.btn_reset.on_clicked(self.on_reset_clicked)
        
        # Info box at bottom
        ax_info = plt.axes([panel_left, 0.02, panel_width, 0.05])
        ax_info.axis('off')
        info_text = 'Configure parameters and click "Start"'
        ax_info.text(0.5, 0.5, info_text, 
                    ha='center', va='center', fontsize=8, style='italic',
                    bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
    def update_config(self, key, value):
        """Update configuration value"""
        try:
            if key in ['rows', 'cols', 'depth_limit', 'max_depth']:
                self.config[key] = int(value)
            elif key in ['start_row', 'start_col', 'target_row', 'target_col']:
                self.config[key] = int(value)
            elif key in ['obs_prob']:
                self.config[key] = float(value)
            print(f"Updated {key} = {self.config[key]}")
        except ValueError:
            print(f"Invalid value for {key}: {value}")
    
    def on_start_clicked(self, event):
        """Handle start button click"""
        if self.running:
            print("Algorithm is already running!")
            return
        
        self.running = True
        self.stop_flag = False
        self.btn_start.label.set_text('Running...')
        self.btn_start.color = 'gray'
        self.btn_stop.active = True  # Enable stop button
        
        # Initialize grid environment
        from Grid_Environment import GridEnvironment
        from Search_Algorithms import SearchAlgorithms
        
        try:
            # Create grid
            self.grid_env = GridEnvironment(
                self.config['rows'],
                self.config['cols'],
                self.config['obs_prob']
            )
            
            # Set start and target
            self.grid_env.set_start(self.config['start_row'], self.config['start_col'])
            self.grid_env.set_target(self.config['target_row'], self.config['target_col'])
            
            # Create visualizer for the main area
            self.setup_main_visualizer()
            
            # Run selected algorithm
            search = SearchAlgorithms(self.grid_env)
            start = self.grid_env.start
            target = self.grid_env.target
            
            result = None
            algorithm_name = ""
            
            if self.config['algorithm'] == 'BFS':
                algorithm_name = "Breadth-First Search"
                result = search.bfs(
                    start, target, 
                    self.main_visualizer
                )
            elif self.config['algorithm'] == 'DFS':
                algorithm_name = "Depth-First Search"
                result = search.dfs(
                    start, target, 
                    self.main_visualizer
                )
            elif self.config['algorithm'] == 'UCS':
                algorithm_name = "Uniform Cost Search"
                result = search.ucs(
                    start, target, 
                    self.main_visualizer
                )
            elif self.config['algorithm'] == 'DLS':
                algorithm_name = "Depth-Limited Search"
                result = search.depth_limited_search(
                    start, target, 
                    self.config['depth_limit'], 
                    self.main_visualizer
                )
            elif self.config['algorithm'] == 'IDDFS':
                algorithm_name = "Iterative Deepening DFS"
                result = search.iterative_deepening_dfs(
                    start, target, 
                    self.config['max_depth'], 
                    self.main_visualizer
                )
            else:  # Bidirectional
                algorithm_name = "Bidirectional Search"
                result = search.bidirectional_search(
                    start, target, 
                    self.main_visualizer
                )
            
            # Show final result
            stats = {
                'explored': search.explored_history,
                'info': '',
                'visit_order': search.visit_order
            }
            self.main_visualizer.show_final_result(result, algorithm_name, stats)
            
            print(f"\n{'='*60}")
            print(f"Algorithm: {algorithm_name}")
            if result:
                print(f"Path length: {len(result)}")
            else:
                print("✗ No path found!")
            print(f"Nodes explored: {len(search.explored_history)}")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self.running = False
            self.stop_flag = False
            self.btn_start.label.set_text('Start')
            self.btn_start.color = 'lightgreen'
            self.btn_stop.active = False  # Disable stop button
    
    def setup_main_visualizer(self):
        """Setup the main visualization area"""
        self.ax_main.clear()
        self.ax_main.set_xlim(-0.5, self.grid_env.cols - 0.5)
        self.ax_main.set_ylim(-0.5, self.grid_env.rows - 0.5)
        self.ax_main.set_aspect('equal')
        self.ax_main.invert_yaxis()
        
        # Grid lines
        for i in range(self.grid_env.rows + 1):
            self.ax_main.axhline(y=i - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        for j in range(self.grid_env.cols + 1):
            self.ax_main.axvline(x=j - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        
        self.ax_main.set_xticks([])
        self.ax_main.set_yticks([])
        self.ax_main.set_title("Pathfinding Visualization", fontsize=14, fontweight='bold')
        
        # Create a custom visualizer for this main axis
        self.main_visualizer = MainAreaVisualizer(self.grid_env, self.ax_main, self.fig, 
                                                  delay=self.speed_delay, 
                                                  stop_flag_callback=lambda: self.stop_flag)
    
    def on_stop_clicked(self, event):
        """Handle stop button click"""
        if self.running:
            self.stop_flag = True
            print("\n⚠️ Stopping algorithm...")
            self.btn_start.label.set_text('Stopping...')
            self.btn_start.color = 'yellow'
    
    def on_reset_clicked(self, event):
        """Handle reset button click"""
        self.ax_main.clear()
        self.ax_main.text(0.5, 0.5, 'Configure and click "Start"',
                         ha='center', va='center', fontsize=12,
                         transform=self.ax_main.transAxes)
        self.ax_main.axis('off')
        self.fig.canvas.draw()
        print("Reset! Configure parameters and click Start.")
    
    def show(self):
        """Display the interface"""
        self.on_reset_clicked(None)
        plt.show(block=True)


class MainAreaVisualizer:
    """Visualizer for the main display area in ConfigurableVisualizer"""
    
    def __init__(self, grid_env, ax, fig, delay=0.05, stop_flag_callback=None):
        self.grid_env = grid_env
        self.ax = ax
        self.fig = fig
        self.delay = delay
        self.stop_flag_callback = stop_flag_callback
        
        # Color scheme
        self.colors = {
            'empty': '#FFFFFF',
            'obstacle': '#2C3E50',
            'start': '#3498DB',
            'target': '#2ECC71',
            'frontier': '#F39C12',
            'explored': '#E74C3C',
            'path': '#9B59B6'
        }
    
    def draw_cell(self, row, col, color, alpha=1.0):
        """Draw a colored cell"""
        rect = patches.Rectangle(
            (col - 0.5, row - 0.5), 1, 1,
            linewidth=0, facecolor=color, alpha=alpha
        )
        self.ax.add_patch(rect)
    
    def update(self, frontier, explored, path, algorithm_name="Search", depth_info="", visit_order=None):
        """Update the visualization"""
        # Clear and redraw
        self.ax.clear()
        self.ax.set_xlim(-0.5, self.grid_env.cols - 0.5)
        self.ax.set_ylim(-0.5, self.grid_env.rows - 0.5)
        self.ax.set_aspect('equal')
        self.ax.invert_yaxis()
        
        # Grid lines
        for i in range(self.grid_env.rows + 1):
            self.ax.axhline(y=i - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        for j in range(self.grid_env.cols + 1):
            self.ax.axvline(x=j - 0.5, color='gray', linewidth=0.5, alpha=0.3)
        
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Draw obstacles
        for i in range(self.grid_env.rows):
            for j in range(self.grid_env.cols):
                if self.grid_env.grid[i][j] == 1:
                    self.draw_cell(i, j, self.colors['obstacle'])
        
        # Draw explored with visit order numbers
        for pos in explored:
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['explored'], alpha=0.6)
                # Add visit order number in top-left corner
                if visit_order and pos in visit_order:
                    self.ax.text(pos[1] - 0.4, pos[0] - 0.4, str(visit_order[pos]), 
                               ha='left', va='top',
                               fontsize=8, color='white', fontweight='bold')
        
        # Draw frontier
        for pos in frontier:
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['frontier'], alpha=0.8)
        
        # Draw path
        for pos in path:
            if pos != self.grid_env.start and pos != self.grid_env.target:
                self.draw_cell(pos[0], pos[1], self.colors['path'], alpha=0.9)
        
        # Draw start
        if self.grid_env.start:
            self.draw_cell(self.grid_env.start[0], self.grid_env.start[1], 
                          self.colors['start'])
            self.ax.text(self.grid_env.start[1], self.grid_env.start[0], 'S',
                       ha='center', va='center', fontsize=12, 
                       color='white', fontweight='bold')
        
        # Draw target
        if self.grid_env.target:
            self.draw_cell(self.grid_env.target[0], self.grid_env.target[1],
                          self.colors['target'])
            self.ax.text(self.grid_env.target[1], self.grid_env.target[0], 'T',
                       ha='center', va='center', fontsize=12, 
                       color='white', fontweight='bold')
        
        # Title with info
        title = f"{algorithm_name}"
        if depth_info:
            title += f" - {depth_info}"
        self.ax.set_title(title, fontsize=12, fontweight='bold')
        
        # Stats box
        info_text = f"Explored: {len(explored)}"
        if path:
            info_text += f" | Path: {len(path)}"
        
        self.ax.text(0.02, 1.02, info_text,
                    transform=self.ax.transAxes,
                    fontsize=10, verticalalignment='bottom',
                    horizontalalignment='left',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
        # Check stop flag before delay
        if self.stop_flag_callback and self.stop_flag_callback():
            return  # Exit early if stopped
        
        time.sleep(self.delay)
    
    def show_final_result(self, path, algorithm_name, stats):
        """Show final result"""
        self.update(
            frontier=[],
            explored=stats.get('explored', []),
            path=path if path else [],
            algorithm_name=algorithm_name,
            depth_info="Completed!",
            visit_order=stats.get('visit_order', {})
        )
        
        # Add result message only if no path found
        if not path:
            message = "✗ No Path Found!"
            color = 'red'
            
            self.ax.text(0.5, 0.5, message,
                        transform=self.ax.transAxes,
                        fontsize=16, fontweight='bold',
                        ha='center', va='center', color=color,
                        bbox=dict(boxstyle='round', facecolor='white', 
                                 alpha=0.9, edgecolor=color, linewidth=3))
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
