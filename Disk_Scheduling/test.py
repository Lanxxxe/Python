#First Come First Serve
def FCFS(inputlist):
    total_seekcount = 0
    for index in range(0, len(inputlist) - 1):
        total_seekcount += abs(inputlist[index] - inputlist[index + 1])
            
    return inputlist, total_seekcount # very complicated function idk how to explain


#Shortest Seek Time First
def SSTF(inputlist):

    # creates two new arrays: a non-immutable const (based on inputlist) and a sorted_list containing only the head
    # pops the head (0th element) from the inputlist
    locallist = inputlist[:]
    sorted_list = [locallist.pop(0)]
    total_seekcount = 0

    # loops through the const tuple
    for item_index in range(0, len(inputlist) - 1):
            
        # creates a new list of differences with the current latest track and creates a sorted version
        differences = [abs(sorted_list[item_index] - x) for x in locallist]
        sorted_diffs = sorted(differences)

        # identifies the index of the smallest difference based on the smallest of the sorted difference list
        index_to_append = differences.index(sorted_diffs[0])

        # removes the newest value and adds it to the sorted list
        sorted_list.append(locallist.pop(index_to_append))
        total_seekcount += abs(sorted_list[item_index] - sorted_list[item_index + 1])        

    return sorted_list, total_seekcount

        
def SCAN(inputlist, mx, mn):
    # local lists enables popping without modidfying the global list
    local_list = inputlist[:]
    total_seekcount = 0
    sorted_list = [local_list.pop(0)] # appends head (index 0) to the final list

    while len(local_list) > 0:
        # identifies the head (current track)
        head = sorted_list[len(sorted_list) - 1]
                
        # creates a sorted list of tracks greater than the head; set function disables duplicates
        greater_than = [x for x in sorted(set(local_list)) if x > head]

        # removes all items in local list that is already recorded in the greater_than list; ignores duplicates
        for item in greater_than:
            if item in local_list:
                local_list.remove(item)

        # appends max track if max now already in the greater_than (unique to SCAN and C-SCAN)
        if len(local_list) > 0:
            if mx not in greater_than:
                greater_than.append(mx)
        
        sorted_list.extend(greater_than)
        head = sorted_list[len(sorted_list) - 1]

        # creates a sorted list of tracks greater than the head; set function disables duplicates
        lesser_than = [x for x in sorted(set(local_list)) if x <= sorted_list[len(sorted_list) - 1]]
        
        # removes all items in local list that is already recorded in the lesser_than list; ignores duplicates
        for item in lesser_than:
            if item in local_list:
                local_list.remove(item)

         # adds the minimum value to the beginning if the lesser than list doesn't contain it, also reverses it
        if len(local_list) > 0:
            if mn not in lesser_than:
                lesser_than.insert(0, mn)
        lesser_than.reverse() #reverses list (unique to non circular SCAN and LOOK)
        
        sorted_list.extend(lesser_than)

    for index in range(0, len(sorted_list) - 1):
        total_seekcount += abs(sorted_list[index] - sorted_list[index + 1])

    return sorted_list, total_seekcount




items = [70, 118, 59, 110, 25, 105, 63, 100, 28, 80]
maxn = 199
minn = 0

# items = []
# n = int(input("#tk >> ")) # number of tasks, head not included
# maxn = int(input("max >> ")) # max track
# minn = int(input("min >> ")) # min track
# print()
# for i in range(n):
#     while True:
#         item = int(input(f"{i} >> "))
#         if item >= minn and item <= maxn:
#             items.append(item)
#             break
# while True:
#         item = int(input(f"head >> "))
#         if item >= minn and item <= maxn:
#             items.insert(0, item)
#             break

fcfs, fcfs_cnt = FCFS(items)
print(fcfs, fcfs_cnt)

sstf, sstf_cnt = SSTF(items)
print(sstf, sstf_cnt)

scan, scan_cnt = SCAN(items, maxn, minn)
print(scan, scan_cnt)
