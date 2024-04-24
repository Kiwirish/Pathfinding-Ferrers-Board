# Author : Blake Leahy 

# Etude 5 - Pathfinding partitions 

# Partition represented by ferrers board, where partition:
# 5 4 3 1 can be represented by: 

#   * * * * *
#   * * * *
#   * * *
#   *

# We remove a column off the ferrers board to get: 

#   * * * *
#   * * *
#   * *
#   *

# That removed column is to be swapped/replaced with a ROW of the same length to get: 

#   * * * *
#   * * *
#   * * *
#   * *
#   *

# ^^^ This is ONE MOVE - one column to row swap is one move 
# minimum possible number of moves to get from initial to final partition?

# initialPartitions sum should be equal to finalPartitions sum - do by checking:
# if sum(initialPartition) != sum(finalPartition) then return because final partition reached 

# Approach: 

# - Partitions need to be easily trackable for comparison between moves to track how many 
# of each number each partition holds - collections.Counter? 
# - Partition transformations from intial to final partition need to be represented in a list ? 
# - First, check for: if sum(initialPartition) != sum(finalPartition) then return because final partition reached 
# - Next, check if Counter(currentPartition) = finalPartitionCounter and when it is, no moves needed 
# - if partitioon isn't already at finalPartition from counter check, merge?: 
# - joining rows with other rows? as in 1 1 1 to 3 example: 
# - merge rows to combine all ferers ' dots' into one row 
# so if your initial partition is : 
#   1 1 1 so:   
#   *
#   *
#   * 
# And your goal partition is: 
#   3 so:
#   * * *
# Then the initalPartitions rows can be merged to get the final where the partition sum 
# merge when initalPartition length > final partition length - moves+=1 
# - if initalPartitions counter and finalPartitions counter aren't equal AND initalPartitions 
# length isn't greater than finalPartitions length then split rows? 
# make copy of initialPartition to be currentPartition going into splitting loop(s) 
# loop over currentPartition, looking for an index that's greater than 1 
# and if that's found, append a 1 (or a * in ferrers) to currentPartition (appends to the end) 
# then remove 1 (or a * in ferrers) from currentPartitions current index (current *'s line being looked over in loop)
# then move = move + 1 
# then append a copy of the currentPartition to list storing transformations as this partition was one of the steps to transform initial to final 
# If the currentPartition matches the finalPartition after looping over and doing the splits,
# then break out of while loop early as initial=final condition is now met 

# LeastMoves(initialPartition, finalPartition) returns moves, partitionPhases ? 



# PartitionPhases = transformations? 

# For multiple partition inputs, need condition check of '----': isSeparatorLine(line) 
# from stdin, writing to stdout 
# Maybe just test with inside-script testCases to start? 


# 7 April Version only works for very small partitions, any larger partitions, it breaks 

# it also doesn't order outputted transformations correctly, ie [2 2] to [1 1 1 1] example 
# Must find a way to explore the least possible moves, then the next least possible moves etc, 
# Breadth-First-Search? over Depth First Search? 
# BFS to find shortest partition path rather than starting at longest like DFS? 
# BFS gurantees that the first time a node (final partition) is seen,
# it is encountered with the shortest path possible from the source (initial partition) 
# BFS: represent partitions as nodes. 
# Explore all nodes (partitions) at the present depth, then move onto the nodes at the next depth level, 
# so, the least moves partition nodes will be found first, and if there aren't any, then more move requiring nodes are explored 
# Implementing BFS for a partition pathfinding context:
# 
#
#

def BFS(initialPartition, finalPartition): 
    return None 


def LeastMoves(initialPartition, finalPartition):
    from collections import Counter 

    if sum(initialPartition) != sum(finalPartition):
        return None
    initialPartitionCounter = Counter(initialPartition)
    finalPartitionCounter = Counter(finalPartition) 

    # No moves needed as partitions already same
    if initialPartitionCounter == finalPartitionCounter:
        moves = 0
        partitionPhases = [] 
    elif len(initialPartition) > len(finalPartition):
        moves = 1
        partitionPhases = [initialPartition, finalPartition] 
    else: 
        moves = 0 
        partitionPhases = [initialPartition]
        currentPartition = initialPartition[:] # vopy
        
        while Counter(currentPartition) != finalPartitionCounter:

            for i in range(len(currentPartition)):
                
                if currentPartition[i] > 1: 

                    currentPartition.append(1) 
                    currentPartition[i] -= 1
                    moves +=1 
                    partitionPhases.append(currentPartition[:]) # copy of currentpartition into storage of transformations / phases toward goal partition
                    break 
            if Counter(currentPartition) == finalPartitionCounter:
                break 
    return moves, partitionPhases

test = [([1,1,1],[3]),([2, 2],[1,1,1,1])]

# loop over and print phases and moves for ea test 
for initialPartition, finalPartition in test:
    moves, partitionPhases = LeastMoves(initialPartition,finalPartition)
    print('# Moves required: ', moves)
    for phase in partitionPhases: 
        print(phase)
    print('--------')


