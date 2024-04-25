# Author : Blake Leahy 

# must perform move - CLEARLY DEFINE A MOVE 
# First, get move performing function working. 
# Once moves are performed correctly, BFS 
# Must perform move on all of the initial/starting partitions
# columns, then perform moves on all the columns of the child partition, and so on 
# Once these are done, the goalPartition hit with the shortest path 
# backtracking from that goalPartition back to the root (initialPartition), 
# counting how many moves that is and outputting the 'partition steps' on the way to
# that goal partition from initial partition.
# 
# Must have a way to backtrack in BFS. Dictonary storing pointers from each partition to 
# its parent partition for easy backtracking of BFS tree structure.
# 
# Must conform to ParsingPartitions rules: Comments ignored, separator lines, etc 
# read in scenarios and call BFS on each scenario, within BFS is calls to performMove 

import sys 
from collections import deque 

def main(): 

    scenarios = ReadScenarios()
    totalScenarios = len(scenarios)

    for i, scenario in enumerate(scenarios):

        if len(scenario)==2: 

            initialPartition, finalPartition = map(lambda x: list(map(int, x.split())), scenario)
            shortestPath = BFS(initialPartition, finalPartition)

            if shortestPath is not None: 
                # initial partition included so -1 
                print("# Moves required:", len(shortestPath) - 1) 

                for partition in shortestPath:
                    PrintPartition(partition)

            else:

                print("# No solution possible")
                PrintPartition(initialPartition)
                PrintPartition(finalPartition)

        else:
            #  invalid or commentonly scenarios
            for line in scenario:
                print(line)

        # Print separator lines except for the last scenario
        if i < totalScenarios - 1:
            print("--------") 

def PerformMove(partition, columnIndex):
    
    newPartition = [] 
    columnHeight = 0

    # height of column by counting how many rows have atleast 'columnIndex' dots in ferrers
    for length in partition: 
        if length >= columnIndex:
            columnHeight += 1 
    
    if columnHeight > 0: 

        for length in partition: 

            if length >= columnIndex: 

                if length - 1 > 0:
                    newPartition.append(length-1)
            else: 
                newPartition.append(length)

        newPartition.append(columnHeight)
        newPartition.sort(reverse=True)
        #remove zeros from resulting partition
        newPartition = [x for x in newPartition if x > 0]

        return newPartition
    
    else: 
        # If column empty no move is made so return original partition without zeros
        return [x for x in partition if x > 0]

# BFS to explore all possible partitions, finding the shortest path. 
def BFS(initial,final):

    toVisit = deque() 
    visited = set()

    # initially append starting partition to the move sequence to start 
    toVisit.append((initial, [initial]))

    while toVisit:

        currentPartition, moves = toVisit.popleft()

        if currentPartition == final:
            return moves
        
        for columnIndex in range(1, max(currentPartition) + 1):

            newPartition = PerformMove(currentPartition, columnIndex)

            if tuple(newPartition) not in visited: 
                visited.add(tuple(newPartition))
                toVisit.append((newPartition, moves + [newPartition]))
    # if no solution is found 
    return None


# read scenarios from stdin 
def ReadScenarios(): 

    scenarios = [] 
    currentScenario = [] 
    for line in sys.stdin:

        line = line.rstrip('\n')
        if isBlank(line):
            continue 
        elif isComment(line):
            continue 
        elif isPartition(line):
            currentScenario.append(standardisePartition(line))
        elif isSeparator(line):
            if currentScenario:
                scenarios.append(currentScenario)
            currentScenario = []
        else: 
            currentScenario.append(f"# INVALID: {line}")
    
    if currentScenario: 
        scenarios.append(currentScenario)
    
    return scenarios 


def PrintPartition(partition):
    print(' '.join(map(str, partition)))


# ParsingPartitions rules 
    
def isBlank(line):
    return not line.strip()

def isComment(line):
    return line.startswith('#')

def isPartition(line):
    return all(part.isdigit() for part in line.replace(',', ' ').split())

def isSeparator(line):
    return set(line.strip()) == {'-'} and len(line.strip()) >= 3

def standardisePartition(partition):
    parts = sorted(map(int, partition.replace(',', ' ').split()), reverse=True)
    return ' '.join(map(str, parts))

if __name__ == "__main__":
    main()
