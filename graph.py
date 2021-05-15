from collections import Counter


class Vertex:
    def __init__(self, id):
        self.color_id = -1
        self.id = id
        self.neighbours = []

    def color_with(self, color_id):
        self.color_id = color_id

    def add_neighbour(self, vertex):
        self.neighbours.append(vertex)

    def remove_neighbour(self, vertex):
        for i in range(len(self.neighbours)):
            if(self.neighbours[i].id == vertex.id):
                self.neighbours.pop(i)
                return

    def is_properly_colored(self):
        for n in self.neighbours:
            if n.get_color() == self.color_id:
                return False
        return True

    def get_degree(self):
        return len(self.neighbours)
    
    def get_saturation_degree(self):
        satur = 0;
        for v in self.neighbours:
            if v.get_color() != -1:
                satur += 1
        return satur

    def get_color(self):
        return self.color_id


class Graph:
    def __init__(self, n):
        self.vertices = []
        for i in range(n):
            self.vertices.append(Vertex(i))

    def add_edge(self, v_one_id, v_two_id):
        self.vertices[v_one_id].add_neighbour(self.vertices[v_two_id])
        self.vertices[v_two_id].add_neighbour(self.vertices[v_one_id])

    def color_with(self, algorithm_function, color_limit):
        self.vertices = algorithm_function(self.vertices, color_limit)

    def check_proper_coloring(self, color_limit):
        color_list = []

        for v in self.vertices:
            color_list.append(v.get_color())

            if not v.is_properly_colored():
                print("Error: proper coloring")
                return False

        color_counter = Counter(color_list)

        for color_count in color_counter.values():
            if color_count > color_limit:
                print("Error: color count")
                return False

        return True
