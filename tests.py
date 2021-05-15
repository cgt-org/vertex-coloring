import copy
import datetime
import os
from visualization import visualize
from graph import Graph, Vertex
from algorithms import smallest_last_coloring, largest_first_coloring, d_satur_coloring


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
            f"largest first, max vertices in one color: {color_limit}, is proper: {graph_lf.check_proper_coloring(color_limit)}",
            f"smallest last, max vertices in one color: {color_limit}, is proper: {graph_sl.check_proper_coloring(color_limit)}",
            f"dSatur, max vertices in one color: {color_limit}, is proper: {graph_dsatur.check_proper_coloring(color_limit)}",
        ],
        save_to_file=save_to_file,
        filename=filename,
    )


def run_tests():
    if not os.path.exists("results"):
        os.mkdir("results")

    results_dir = f"results/{datetime.datetime.now()}"
    os.mkdir(results_dir)

    cycle_3 = Graph(3)
    cycle_3.add_edge(0, 1)
    cycle_3.add_edge(1, 2)
    cycle_3.add_edge(2, 0)
    test_graph(
        cycle_3,
        color_limit=4,
        save_to_file=True,
        filename=f"{results_dir}/3-cycle-limit-4",
    )

    cycle_5 = Graph(5)
    cycle_5.add_edge(0, 1)
    cycle_5.add_edge(1, 2)
    cycle_5.add_edge(2, 3)
    cycle_5.add_edge(3, 4)
    cycle_5.add_edge(4, 0)
    test_graph(
        cycle_5,
        color_limit=7,
        save_to_file=True,
        filename=f"{results_dir}/5-cycle-limit-7",
    )


if __name__ == "__main__":
    run_tests()
