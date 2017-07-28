# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]
from util import Stack
from util import Queue
def genericSearch(problem, structure):
    data = structure()
    visitedSpots = set()
    case = {
        "solution": data,
        "isFound": False,
        "v": visitedSpots,
    }
    data.push((problem.getStartState(), [], 0))
    while not data.isEmpty():
        # Setting the three values equal to the current state, current node, and current path cost
        node, move, actionCost = data.pop()
        if node in visitedSpots:
            print("(TEST) State " + str(node) + " has already been traversed, no need to search it again.")
            continue
        visitedSpots.add(node)

        if problem.isGoalState(node):
            print("(TEST) Found a solution at node " + str(node))
            return move
        for nNode, nPath, nCost in problem.getSuccessors(node):
            print("(TEST) The current node is " + str(nNode))
            print("(TEST) The path for the following action is " + str(nPath))
            print("(TEST) The cost for the following path is " + str(nCost))
            data.push((nNode, move + [nPath], actionCost))
    return []
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    return genericSearch(problem, Stack)
    """
    Pseudocode:
    for each parent node (child of the root node)
        if parent node has a child node, call method again and search child node
        else go up one level and search the next adjacent node.
    
    """


    """
    Start = problem.getStartState()
    problem.getSuccessors(start)
    [('B', A -> B, cost (1), ('C' A -> C, 3)]
    - Storing the starting node in a variable
            A
        1 /   \ 3 
         B     C
       / | \  / | \  
    State = problem.getStartState()
    Create a while loop to iterate through the laugh
    while(not problem.isGoalState(state)):
        nextState = problem.getSuccessor(state)
        state = nextState
        print(state)
        - Setting the current node to the start node
    
    
    def Node():
    
        __init__(self, name, parent, child
    
    """






    "*** YOUR CODE HERE ***"


    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    """
    Pseudocode:
    Similar to DFS, but with a queue (FIFO)
    
    """
    return genericSearch(problem, Queue)
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
