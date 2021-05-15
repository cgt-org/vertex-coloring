from graph import Graph, Vertex
from algorithms import greedy_coloring, largest_first_coloring


print("Testing 3-cycle")

test = Graph(3)

test.add_edge(0, 1)
test.add_edge(1, 2)
test.add_edge(2, 0)


test.color_with(greedy_coloring, 7)

print(test.check_proper_coloring(7))

for v in test.vertices:
    print(f"{v.id} : {v.get_color()}")

print("Testing 5-cycle")

five = Graph(5)

five.add_edge(0, 1)
five.add_edge(1, 2)
five.add_edge(2, 3)
five.add_edge(3, 4)
five.add_edge(4, 0)

five.color_with(greedy_coloring, 7)
print(five.check_proper_coloring(7))

for v in five.vertices:
    print(f"{v.id} : {v.get_color()}")
