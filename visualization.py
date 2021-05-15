import math
import networkx as nx
import matplotlib.pyplot as plt


def add_to_visualiztion(graph, ax):
    nx_graph = nx.Graph()

    highest_color_id = -1
    coloring_order = -1
    labels = {}
    edges = []
    for vertex in graph.vertices:
        vertex_color = vertex.get_color()

        if vertex_color > highest_color_id:
            highest_color_id = vertex_color

        coloring_order += 1
        nx_graph.add_node(
            vertex.id,
            attr_dict={"color_id": vertex_color, "coloring_order": coloring_order},
        )

        for neighbour in vertex.neighbours:
            edges.append((vertex.id, neighbour.id))

    nx_graph.add_edges_from(edges)

    node_colors = []
    for vertex in graph.vertices:
        try:
            node_colors.append(vertex.get_color() / highest_color_id)
        except ZeroDivisionError:
            node_colors.append(1)

    positions = nx.spring_layout(nx_graph)

    nx.draw_networkx_nodes(
        nx_graph,
        positions,
        cmap=plt.get_cmap("jet"),
        node_color=node_colors,
        node_size=300,
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
            "coloring_order": attr_dict["coloring_order"],
        }

    nx.draw_networkx_labels(
        nx_graph,
        positions,
        font_weight="bold",
        font_size=9,
        labels=labels,
        ax=ax,
    )


def visualize(graphs, titles, save_to_file, filename):
    num_graphs = len(graphs)
    n_rows = math.ceil(math.sqrt(num_graphs))
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_rows)
    ax = axes.flatten()

    for i in range(n_rows * n_rows):
        ax[i].set_axis_off()

    for i in range(num_graphs):
        add_to_visualiztion(graphs[i], ax[i])
        ax[i].set_title(titles[i])

    if save_to_file:
        fig.set_size_inches(30, 30)
        plt.savefig(filename)
    else:
        plt.get_current_fig_manager().set_window_title("Graph coloring")
        plt.show()
