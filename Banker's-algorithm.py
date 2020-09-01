""" Author: Muham'mad Anwar , Muhammad Ramadan  sec:3 CS """




# Get the Need for each process
def calcNeed(need, max, alloc):
    # calculate need for each P
    for i in range(P):
        for j in range(R):

            # need of instance = max instance - alloc instance
            need[i][j] = max[i][j] - alloc[i][j]
    print('need matrix :\t', need)



# check system is in safe state or not
def isSafe(processes, avail, max, alloc):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)

    # calc neeed matrix
    calcNeed(need, max, alloc)

    # mark all process as infinsih
    finish = [0] * P

    # store safe sequence
    safeSeq = [0] * P

    # make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

    # while processes not finished or not in a safe sate
    count = 0
    while (count < P):

        # Find processes that is not finished and whose needs can be statisfied with current work[] resources
        found = False
        for p in range(P):

            # check if a process is finished
            if (finish[p] == 0):
          
                # check if for all resources of current P is less than work
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break
               
                # if all needs of p were satisfied
                if (j == R - 1):
                    
                    # Add the allocated resources of current P to the available/work resources
                    for k in range(R):
                        work[k] += alloc[p][k]

                    # Add this process to safe sequence.
                    safeSeq[count] = p
                    count += 1

                    # Mark this p as finished
                    finish[p] = 1

                    found = True
                
            print('available matrix \t', work)

        # If we could not find a next process
        # in safe sequence.
        if (found == False):
            print("System is not in safe state")
            return False

    # If system is in safe state then
    # safe sequence will be as below
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True


# Num of processes
P = 5
# Num  of Resources
R = 3

processes = [0, 1, 2, 3, 4]

# Available instances of resources
avail = [3, 3, 2]

# Maximum R that can be allocated
# to processes
max = [[7, 5, 3],
       [3, 2, 2],
       [9, 0, 2],
       [2, 2, 2],
       [4, 3, 3]]

# Resources allocated to processes
alloc = [[0, 1, 0],
         [2, 0, 0],
         [3, 0, 2],
         [2, 1, 1],
         [0, 0, 2]]

# Check system is in safe state or not
isSafe(processes, avail, max, alloc)
