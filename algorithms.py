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
            while color_counter[candidate_color] >= color_limit:
                candidate_color += 1
            v.color_with(candidate_color)

        color_counter[candidate_color] += 1

    return vertices


def largest_first_coloring(vertices, color_limit):
    sorted_vertices = sorted(
        copy.deepcopy(vertices), key=lambda vertex: vertex.get_degree(), reverse=True
    )
    return greedy_coloring(sorted_vertices, color_limit)


def smallest_last_coloring(vertices, color_limit):
    processed = copy.deepcopy(vertices)
    sorted_vertices = []

    while len(processed) > 0:
        min_index = -1
        min_deg = 999999

        for i in range(len(processed)):
            if processed[i].get_degree() < min_deg:
                min_deg = processed[i].get_degree()
                min_index = i

        tmp = processed.pop(min_index)
        sorted_vertices.append(tmp)

    return greedy_coloring(sorted_vertices, color_limit)


def d_satur_coloring(vertices, color_limit):
    if color_limit < 1:
        print("Error: please input a valid color limit")
        return

    color_counter = Counter()
    sorted_vertices = []

    while any(v.get_color() == -1 for v in vertices):
        # find vertex with lowest satur degree
        max_satur = -1
        max_index = -1

        for i in range(len(vertices)):
            if (
                vertices[i].get_saturation_degree() > max_satur
                and vertices[i].get_color() == -1
            ):
                max_index = i
                max_satur = vertices[i].get_saturation_degree()

        candidate_color = 0
        while color_counter[candidate_color] >= color_limit:
            candidate_color += 1

        vertices[max_index].color_with(candidate_color)
        while not vertices[max_index].is_properly_colored():
            candidate_color += 1
            while color_counter[candidate_color] >= color_limit:
                candidate_color += 1

            vertices[max_index].color_with(candidate_color)

        color_counter[candidate_color] += 1
        sorted_vertices.append(vertices[max_index])

    return sorted_vertices
