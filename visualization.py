import math
import networkx as nx
import matplotlib.pyplot as plt


def add_to_visualiztion(graph, ax):
    nx_graph = nx.Graph()

    highest_color_id = -1
    labels = {}
    edges = []
    for vertex in graph.vertices:
        vertex_color = vertex.get_color()

        if vertex_color > highest_color_id:
            highest_color_id = vertex_color

        nx_graph.add_node(vertex.id, attr_dict={"color_id": vertex_color})

        for neighbour in vertex.neighbours:
            edges.append((vertex.id, neighbour.id))

    nx_graph.add_edges_from(edges)

    node_colors = []
    for vertex in graph.vertices:
        node_colors.append(vertex.get_color() / highest_color_id)

    positions = nx.spring_layout(nx_graph)

    nx.draw_networkx_nodes(
        nx_graph,
        positions,
        cmap=plt.get_cmap("jet"),
        node_color=node_colors,
        node_size=150,
        ax=ax,
    )

    nx.draw_networkx_edges(
        nx_graph,
        positions,
        ax=ax,
    )

    attr_dict = nx.get_node_attributes(nx_graph, "attr_dict")
    labels = {}
    for node, attr_dict in zip(nx_graph.nodes(), attr_dict.values()):
        labels[node] = {
            "id": node,
            "color_id": attr_dict["color_id"],
        }

    nx.draw_networkx_labels(
        nx_graph,
        positions,
        font_weight="bold",
        font_size=5,
        labels=labels,
        ax=ax,
    )


def visualize(graphs, titles):
    num_graphs = len(graphs)
    n_rows = math.ceil(math.sqrt(num_graphs))
    _, axes = plt.subplots(nrows=n_rows, ncols=n_rows)
    ax = axes.flatten()

    for i in range(n_rows * n_rows):
        ax[i].set_axis_off()

    for i in range(len(graphs)):
        add_to_visualiztion(graphs[i], ax[i])
        ax[i].set_title(titles[i])

    plt.get_current_fig_manager().set_window_title("Graph coloring")
    plt.show()
