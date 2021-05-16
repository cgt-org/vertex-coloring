# About

A simple program for creating graphs and coloring them. For coloring we use the Largest First, Smallest Last and D-Satur algorithms.

# Contents
## Graph Coloring Algorithm CLI
The algorithm CLI is run using python 3.9 <br>
Required python packages: networkx, matplotlib <br/>

## Graph Creator Gui
The graph creator is built using QMake version 3.1 using Qt version 5.15.2 <br/>
In order to compile the source code and get the exec file:
```
$ qmake -makefile
$ make
```
Which will create an executable `graph_creator_GUI` in current working directory.

# Usage
In order to color a particular graph the user needs to first run the Graph Creator GUI. The application allows the user to create custom graphs and generate a JSON file containing a topological description of the graph. Once the user saves the JSON in the desired location in order to color it we need to use the python CLI.

In order to color the graph using the CLI run the following command:
```
$ python tests.py -f <path_to_file> -l <color_limit>
```
If color limit is left blank it will default to 5. Running this command will open a matplotlib rendered window containing graphs colored with different algorithms, additionally providing user with information about the execution such as in what order the vertices were colored by a given algorithm.

The user may also create a random graph from the CLI in the following way:

```
$ python tests.py -n <number_of_random_graphs> -v <max_vertices_for_test>
```

Which will result in creating the graphs with different color limits. The results are then saved in `./results` directory.
