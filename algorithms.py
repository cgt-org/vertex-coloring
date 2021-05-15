from collections import Counter
import copy


def greedy_coloring(vertices, color_limit):
    if color_limit < 1:
        print("Error: please input a valid color limit")
        return

    color_counter = Counter()

    for v in vertices:
        candidate_color = 0

        while color_counter[candidate_color] >= color_limit:
            candidate_color += 1

        v.color_with(candidate_color)
        while not v.is_properly_colored():
            candidate_color += 1
            v.color_with(candidate_color)

        color_counter[candidate_color] += 1


def largest_first_coloring(vertices, color_limit):
    sorted_vertices = sorted(
        copy.deepcopy(vertices), key=lambda vertex: vertex.get_degree()
    )
    greedy_coloring(sorted_vertices, color_limit)
