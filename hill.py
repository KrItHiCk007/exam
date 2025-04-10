import random


def hc_tsp(cities, dist):
    route = cities[:]
    random.shuffle(route)
    best_route = route
    best_distance = calculate_total_distance(route, dist)

    while True:
        neighbors = generate_neighbors(route)
        best_neighbor = min(neighbors, key=lambda r: calculate_total_distance(r, dist))
        neighbor_distance = calculate_total_distance(best_neighbor, dist)

        if neighbor_distance >= calculate_total_distance(route, dist):
            break

        route = best_neighbor

        if neighbor_distance < best_distance:
            best_route = best_neighbor
            best_distance = neighbor_distance

    return best_route, best_distance


def generate_neighbors(route):
    neighbors = []
    for i in range(len(route) - 1):
        neighbor = route[:]
        neighbor[i], neighbor[i + 1] = neighbor[i + 1], neighbor[i]
        neighbors.append(neighbor)
    return neighbors


def calculate_total_distance(route, dist):
    total = 0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]
    total += dist[route[-1]][route[0]]
    return total


if __name__ == "__main__":
    cities = [0, 1, 2, 3]
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_route, best_dist = hc_tsp(cities, dist)
    print("Best route:", best_route)
    print("Best distance:", best_dist)