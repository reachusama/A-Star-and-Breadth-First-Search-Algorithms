from queue import PriorityQueue
from Puzzle8 import *

node_expand_counter = 0
nodes_generated_counter = 0
maximum_pqueue_length = 0

def astar_search(problem):
    global node_expand_counter
    global nodes_generated_counter
    global maximum_pqueue_length

    count = 0
    expandedNodes = []
    root=TreeNode(problem,problem.initial_state,parent=None,g_value=count)
    pqueue = PriorityQueue()
    pqueue.put((root.f,count,root))

    while not pqueue.empty():
        next = pqueue.get()[2]
        expandedNodes.append(next.state)
        if maximum_pqueue_length < count:
            maximum_pqueue_length = count
        if next.goalp():
            del(pqueue)
            node_expand_counter = len(expandedNodes)
            return next.path()
        else:
            new_nodes = next.generate_new_tree_nodes()
            nodes_generated_counter = nodes_generated_counter + len(new_nodes)
            for new_node in new_nodes:
                 if new_node.state not in expandedNodes:
                     count += 1
                     pqueue.put((new_node.f,count,new_node))
    print('No solution')
    return NULL

def print_stats(output):
    global nodes_generated_counter
    global maximum_pqueue_length
    global node_expand_counter

    print("Number of Nodes Explored: ", node_expand_counter)
    print("Number of Nodes Generated: ", nodes_generated_counter)
    print("Maximum Queue Length: ", maximum_pqueue_length)
    print("Number of Moves: ",len(output)-1)
    print("\n")

problem = Puzzle8_Problem(Example1)
output=  astar_search(problem)
print('\nSolution Example 1:')
print_path(output)
print_stats(output)


wait = input("\nPRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2)
output=  astar_search(problem)
print('\nSolution Example 2:')
print_path(output)
print_stats(output)

wait = input("\nPRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3)
output=  astar_search(problem)
print('\nSolution Example 3:')
print_path(output)
print_stats(output)

wait = input("\nPRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4)
output=  astar_search(problem)
print('\nSolution Example 4:')
print_path(output)
print_stats(output)

wait = input("\nPRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example5)
output=  astar_search(problem)
print('\nSolution Example 5:')
print_path(output)
print_stats(output)
