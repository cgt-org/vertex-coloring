#from visualization import visualize
from graph import *
from algorithms import *


print("Testing 3-cycle")

test = Graph(3)

# test.add_edge(0, 1)
# test.add_edge(1, 2)
# test.add_edge(2, 0)


test.color_with(d_satur_coloring, 7)

print(test.check_proper_coloring(7))

for v in test.vertices:
    print(f"{v.id} : {v.get_color()}")

print("Testing 5-cycle")

five = Graph(5)

# five.add_edge(0, 1)
# five.add_edge(1, 2)
# five.add_edge(2, 3)
# five.add_edge(3, 4)
# five.add_edge(4, 0)

five.color_with(d_satur_coloring, 7)
print(five.check_proper_coloring(7))

for v in five.vertices:
    print(f"{v.id} : {v.get_color()}")

# visualize(
#     [five, five, five],
#     [
#         f"greedy1, color limit: {7}, is proper: {five.check_proper_coloring(7)}",
#         f"greedy2, color limit: {7}, is proper: {five.check_proper_coloring(7)}",
#         f"greedy3, color limit: {7}, is proper: {five.check_proper_coloring(7)}",
#     ],
# )

ten = Graph(10);
ten.color_with(greedy_coloring, 7);
for v in ten.vertices:
    print(f"{v.id} : {v.get_color()}")


