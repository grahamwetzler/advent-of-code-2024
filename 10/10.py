from pathlib import Path

import networkx as nx  # type: ignore


def neighbors(grid, pos):
    x, y = pos
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(point, grid[point]) for point in candidates if point in grid]


def make_graph(grid):
    queue = [(point, height) for point, height in grid.items() if height == 0]
    graph = nx.DiGraph()
    while queue:
        point, height = queue.pop()
        for neighbor, neighbor_height in neighbors(grid, point):
            graph.add_nodes_from(
                [
                    (point, dict(height=height)),
                    (neighbor, dict(height=neighbor_height)),
                ]
            )
            if height + 1 != neighbor_height:
                continue
            graph.add_edge(point, neighbor)
            queue.append((neighbor, neighbor_height))

    return graph


def part_1(graph, ends):
    result = sum(
        [
            sum(nx.has_path(graph, point, end) for end in ends)
            for point, height in graph.nodes("height")
            if height == 0
        ]
    )
    print("part 1:", result)


def part_2(graph, ends):
    result = sum(
        [
            sum(len(list(nx.all_simple_paths(graph, point, end))) for end in ends)
            for point, height in graph.nodes("height")
            if height == 0
        ]
    )
    print("part 2:", result)


input_text = (Path(__file__).parent / Path("input.txt")).read_text()

grid = {
    (x, y): int(value)
    for y, line in enumerate(input_text.splitlines())
    for x, value in enumerate(line)
}

graph = make_graph(grid)
ends = [node for node, height in graph.nodes("height") if height == 9]
part_1(graph, ends)
part_2(graph, ends)
