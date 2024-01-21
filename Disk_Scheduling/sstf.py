# disk = [118, 59, 110, 25, 105, 63, 100, 28, 80]

# def sstf(disk_queue, head, max_track):
#     queue = []
#     movements = {}
#     shortest = []

#     queue.append(head)
#     print(queue)
#     for request in range(len(disk_queue)):
#         res = disk_queue[request] - head
#         shortest.append([disk_queue[request], abs(res)])
    
#     shortest = sorted(shortest, key=lambda result : result[1])
#     print(shortest)
#     movements[f'{head} - {shortest[0][0]}'] = head - shortest[0][0]
#     for req in range(len(disk_queue) - 1):
#         movements[f'{shortest[req][0]} - {shortest[req+1][0]}'] = abs(shortest[req][0] - shortest[req+1][0])

#     print(movements)

# sstf(disk, 70, 200)
def sstf_disk_scheduling(requests, initial_head_position):
    # Copy the list of requests to avoid modifying the original list
    requests = list(requests)

    # Initialize the total seek count and head movement list
    total_seek_count = 0
    head_movement = []

    # Set the current head position
    current_head_position = initial_head_position

    while requests:
        # Find the request with the shortest seek time
        nearest_request = min(requests, key=lambda x: abs(x - current_head_position))

        # Calculate the seek time for the selected request
        seek_distance = abs(nearest_request - current_head_position)

        # Update the total seek count
        total_seek_count += seek_distance

        # Record the head movement
        head_movement.append(current_head_position)

        # Move the head to the selected request
        current_head_position = nearest_request

        # Remove the processed request from the list
        requests.remove(nearest_request)

    # Record the final head position
    head_movement.append(current_head_position)

    return total_seek_count, head_movement


# Example usage:
requests_sequence = [118, 59, 110, 25, 105, 63, 100, 28, 80]
initial_head_position = 70

total_seek_count, head_movement = sstf_disk_scheduling(requests_sequence, initial_head_position)

print("Total Seek Count using SSTF:", total_seek_count)
print("Head Movement:", head_movement)
