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



