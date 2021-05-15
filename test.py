from visualization import visualize
from graph import *
from algorithms import *
import copy


cycle_3 = Graph(3)
cycle_3.add_edge(0, 1)
cycle_3.add_edge(1, 2)
cycle_3.add_edge(2, 0)
cycle_3.color_with(d_satur_coloring, 7)


cycle_5 = Graph(5)
cycle_5.add_edge(0, 1)
cycle_5.add_edge(1, 2)
cycle_5.add_edge(2, 3)
cycle_5.add_edge(3, 4)
cycle_5.add_edge(4, 0)
cycle_5.color_with(d_satur_coloring, 7)


visualize(
    [cycle_5, cycle_5, cycle_5],
    [
        f"dSatur, vertices in one color limit: {7}, is proper: {cycle_5.check_proper_coloring(7)}",
        f"dSatur, vertices in one color limit: {7}, is proper: {cycle_5.check_proper_coloring(7)}",
        f"dSatur, vertices in one color limit: {7}, is proper: {cycle_5.check_proper_coloring(7)}",
    ],
)
