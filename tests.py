import getopt
import json
import sys
import copy
import datetime
import os
import random
from visualization import visualize
from graph import Graph, Vertex, create_graph_from_json
from algorithms import smallest_last_coloring, largest_first_coloring, d_satur_coloring


def create_random_graph(num_vertices, num_edges):
    if num_edges > num_vertices * (num_vertices - 1) / 2:
        raise Exception("Illegal number of edges")

    graph = Graph(num_vertices)

    vertices = graph.vertices
    max_degree = num_vertices - 1

    for _ in range(num_edges):
        start_vertex = get_random_vertex(vertices, -1)
        while start_vertex.get_degree() == max_degree:
            start_vertex = get_random_vertex(vertices, -1)

        end_vertex = get_random_vertex(vertices, start_vertex.id)
        while start_vertex.contains_neighbour(end_vertex):
            end_vertex = get_random_vertex(vertices, start_vertex.id)

        graph.add_edge(start_vertex.id, end_vertex.id)

    return graph


def get_random_vertex(vertices, index_to_skip):
    len_vertices = len(vertices)

    random_index = random.randint(0, len_vertices - 1)
    while random_index == index_to_skip:
        random_index = random.randint(0, len_vertices - 1)

    return vertices[random_index]


def test_graph(graph, color_limit, save_to_file=False, filename="graph"):
    graph_lf = copy.deepcopy(graph)
    graph_lf.color_with(largest_first_coloring, color_limit)

    graph_sl = copy.deepcopy(graph)
    graph_sl.color_with(smallest_last_coloring, color_limit)

    graph_dsatur = copy.deepcopy(graph)
    graph_dsatur.color_with(d_satur_coloring, color_limit)

    visualize(
        [graph_lf, graph_sl, graph_dsatur],
        [
            f"largest first, max vertices in one color limit: {color_limit}, vertices: {len(graph_lf.vertices)}, colors used: {graph_lf.get_number_of_colors()}, is proper: {graph_lf.check_proper_coloring(color_limit)}",
            f"smallest last, max vertices in one color limit: {color_limit}, vertices: {len(graph_sl.vertices)}, colors used: {graph_sl.get_number_of_colors()}, is proper: {graph_sl.check_proper_coloring(color_limit)}",
            f"dSatur, max vertices in one color limit: {color_limit}, vertices: {len(graph_dsatur.vertices)}, colors used: {graph_dsatur.get_number_of_colors()}, is proper: {graph_dsatur.check_proper_coloring(color_limit)}",
        ],
        save_to_file=save_to_file,
        filename=filename,
    )


def run_tests(num_random_tests, max_vertices):
    if not os.path.exists("results"):
        os.mkdir("results")

    results_dir = f"results/{datetime.datetime.now()}"
    os.mkdir(results_dir)

    two_points = Graph(2)
    test_graph(
        two_points,
        color_limit=4,
        save_to_file=True,
        filename=f"{results_dir}/two-points-limit-4",
    )

    five_points = Graph(5)
    test_graph(
        five_points,
        color_limit=10,
        save_to_file=True,
        filename=f"{results_dir}/five_points-limit-5",
    )

    one_edge = Graph(2)
    one_edge.add_edge(0, 1)
    test_graph(
        one_edge,
        color_limit=4,
        save_to_file=True,
        filename=f"{results_dir}/one-edge-limit-4",
    )

    complete_graph_4 = Graph(4)
    complete_graph_4.add_edge(0, 1)
    complete_graph_4.add_edge(0, 2)
    complete_graph_4.add_edge(0, 3)
    complete_graph_4.add_edge(1, 2)
    complete_graph_4.add_edge(1, 3)
    complete_graph_4.add_edge(2, 3)
    test_graph(
        complete_graph_4,
        color_limit=5,
        save_to_file=True,
        filename=f"{results_dir}/complete-four-limit-5",
    )

    complete_graph_5 = Graph(5)
    complete_graph_5.add_edge(0, 1)
    complete_graph_5.add_edge(0, 2)
    complete_graph_5.add_edge(0, 3)
    complete_graph_5.add_edge(0, 4)
    complete_graph_5.add_edge(1, 2)
    complete_graph_5.add_edge(1, 3)
    complete_graph_5.add_edge(1, 4)
    complete_graph_5.add_edge(2, 3)
    complete_graph_5.add_edge(2, 4)
    complete_graph_5.add_edge(3, 4)
    test_graph(
        complete_graph_5,
        color_limit=5,
        save_to_file=True,
        filename=f"{results_dir}/complete-five-graph-limit-5",
    )

    bipartite_2 = Graph(4)
    bipartite_2.add_edge(0, 1)
    bipartite_2.add_edge(1, 2)
    bipartite_2.add_edge(2, 3)
    bipartite_2.add_edge(3, 0)
    test_graph(
        bipartite_2,
        color_limit=4,
        save_to_file=True,
        filename=f"{results_dir}/bipartite-two-limit-4",
    )

    cycle_3 = Graph(3)
    cycle_3.add_edge(0, 1)
    cycle_3.add_edge(1, 2)
    cycle_3.add_edge(2, 0)
    test_graph(
        cycle_3,
        color_limit=4,
        save_to_file=True,
        filename=f"{results_dir}/cycle-three-limit-4",
    )

    cycle_5 = Graph(5)
    cycle_5.add_edge(0, 1)
    cycle_5.add_edge(1, 2)
    cycle_5.add_edge(2, 3)
    cycle_5.add_edge(3, 4)
    cycle_5.add_edge(4, 0)
    test_graph(
        cycle_5,
        color_limit=2,
        save_to_file=True,
        filename=f"{results_dir}/cycle-five-limit-2",
    )

    for i in range(num_random_tests):
        num_vertices = random.randint(1, max_vertices)
        num_edges = random.randint(0, (num_vertices * (num_vertices - 1) / 2))
        color_limit = random.randint(1, num_vertices)
        graph = create_random_graph(num_vertices, num_edges)
        test_graph(
            graph,
            color_limit=color_limit,
            save_to_file=True,
            filename=f"{results_dir}/{i}-random-graph-limit-{color_limit}",
        )


if __name__ == "__main__":
    usage_str = "tests.py [-h] [-f <file_with_graph_from_creator>] [-l <color_limit_for_input_file>] [-n <num_of_random_tests>] [-v <max_vertices_for_random_tests>]"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:n:v:l:")
    except getopt.GetoptError:
        print(usage_str)
        sys.exit(2)

    input_file = ""
    max_vertices = 20
    random_tests = 10
    color_limit = 5

    for opt, arg in opts:
        if opt == "-h":
            print(usage_str)
            sys.exit()
        elif opt == "-f":
            input_file = arg
        elif opt == "-n":
            random_tests = int(arg)
        elif opt == "-v":
            max_vertices = int(arg)

    if input_file == "":
        print(
            f"Running tests with {random_tests} random tests (max {max_vertices} vertices)"
        )
        run_tests(num_random_tests=random_tests, max_vertices=max_vertices)
        print("Saved in the 'results' directory")
    else:
        print(f"Running test on {input_file} with color limit set to {color_limit}")
        file = open(input_file)
        json_data = json.load(file)
        test_graph(create_graph_from_json(json_data), color_limit, save_to_file=False)
