requests = [118, 59, 110, 25, 105, 63, 100, 28, 80]
max_request = 199
request_head = 70


def Look(head, request):
    sorted_requests = sorted(request)
    request_order = []
    tracks = 0

    greater = [request for request in sorted_requests if request >= head]
    less = [request for request in sorted_requests if request < head]
    less = sorted(less, reverse=True)
    request_order.append(head)

    for great_items in range(len(greater)):
        request_order.append(greater[great_items])

    for less_item in range(len(less)):
        request_order.append(less[less_item])

    for req in range(len(request_order) - 1):
        count = abs(request_order[req+1] - request_order[req])
        tracks += count

    return request_order, tracks