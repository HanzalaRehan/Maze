"""
Author(s): 1. Hanzala B. Rehan
Description: Uses BFS, DFS, Greedy and A* Search.
Date created: November 18th, 2024
Date last modified: November 18th, 2024
"""

from util import Node, StackFrontier, QueueFrontier, PriorityQueueFrontier
from maze import Maze


def breadth_first_search(start, maze):
    """
    Desc: Implements Breadth-First Search (BFS) to find the shortest path in an unweighted maze.
    Parameters:
        start (tuple): The starting position as (row, col).
        maze (Maze): An instance of the Maze class.
    returns:
        (list): A list of actions leading from the start to the goal, representing the shortest path.
    """
    # To be implemented by Abdullah Janjua
    pass


def depth_first_search(start, maze):
    """
    Desc: Implements Depth-First Search (DFS) to find a path in the maze.
          While DFS may not always find the shortest path, it explores deeper nodes first.
    Parameters:
        start (tuple): The starting position as (row, col).
        maze (Maze): An instance of the Maze class.
    returns:
        (list): A list of actions leading from the start to the goal (may or may not be the shortest path).
    """
    # To be implemented by Abdullah Janjua
    pass


def greedy_first_search(start, maze):
    """
    Desc: Implements Greedy Best-First Search to find a path in the maze.
          It uses a heuristic to prioritize nodes closer to the goal.
    Parameters:
        start (tuple): The starting position as (row, col).
        maze (Maze): An instance of the Maze class.
    returns:
        (list): A list of actions leading from the start to the goal (may not be optimal).
    """
    # To be implemented by Amna Akhtar Nawabi
    pass


def astar_first_search(start, maze):
    """
    Desc: Implements A* Search to find the shortest path in the maze.
          A* uses a combination of the actual path cost and a heuristic to efficiently find the optimal solution.
    Parameters:
        start (tuple): The starting position as (row, col).
        maze (Maze): An instance of the Maze class.
    returns:
        (list): A list of actions leading from the start to the goal, guaranteed to be the shortest path.
    """
    # To be implemented by Amna Akhtar Nawabi
    pass
