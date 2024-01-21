disk = [118, 59, 110, 25, 105, 63, 100, 28, 80]


def fcfs(disk_queue, head, max_track):
    queue = []
    head_movements = {}
  
    queue.append(head)
    for req in disk_queue:
        queue.append(req)

    for request in range(len(queue) - 1):
        head_movements[f'{queue[request+1]} - {queue[request]} '] = abs(queue[request+1] - queue[request])
        
    total_tracks = sum(head_movements.values())

    return queue, head_movements, total_tracks
queue, movement, total_movement =  fcfs(disk, 70, 200)

print(queue)
print(movement)
print(total_movement)