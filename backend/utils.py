import heapq
from collections import defaultdict

def calculate_shortest_path(locations, roads, start_location_id, end_location_id):
    # Create a graph from roads
    graph = defaultdict(list)
    for road in roads:
        graph[road.start_location_id].append((road.end_location_id, road.distance))
        graph[road.end_location_id].append((road.start_location_id, road.distance))

    # Initialize distances and previous_nodes for all locations
    distances = {location.id: float('inf') for location in locations}
    previous_nodes = {location.id: None for location in locations}
    distances[start_location_id] = 0

    # Priority queue for Dijkstra's algorithm
    queue = [(0, start_location_id)]

    while queue:
        current_distance, current_location = heapq.heappop(queue)

        # Early exit if we reached the destination
        if current_location == end_location_id:
            break

        if current_distance > distances[current_location]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_location]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_location
                heapq.heappush(queue, (distance, neighbor))

    # Check if a path was found
    if distances[end_location_id] == float('inf'):
        return {"path": [], "total_distance": None, "estimated_time": None}

    # Reconstruct the shortest path
    path = []
    total_distance = distances[end_location_id]
    current_location = end_location_id

    while current_location is not None:
        path.insert(0, current_location)
        current_location = previous_nodes[current_location]

    # Calculate estimated time based on total distance (assuming an average speed, e.g., 40 km/h)
    estimated_time = total_distance / 40 * 60  # in minutes

    return {"path": path, "total_distance": total_distance, "estimated_time": estimated_time}