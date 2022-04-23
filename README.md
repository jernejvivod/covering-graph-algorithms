# Vertex Cover Approximation Algorithms

This project contains four implementations of algorithms for computing vertex cover of a graph — the exact algorithm that generates node subsets of incrementing sizes and three different approximation algorithms.

## How to Run

run `pip -r requirements.txt` to install the requirements.

Running `python3 vertex-cover-approximations --help` prints the instructions on how to customize the execution parameters:
```
usage: sat-reductions [-h] {all,specific} ...

positional arguments:
  {all,specific}  run all or specific
    all           run all algorithms
    specific      run specific algorithm

optional arguments:
  -h, --help      show this help message and exit
```

We can run `python3 vertex-cover-approximations all --help` or `python3 vertex-cover-approximations specific --help` to print the instructions for running the implementation for all
algorithms or for a specific algorithm respectively:

```
usage: sat-reductions all [-h] --dataset DATASET [--visualize] [--plot-path PLOT_PATH] [--exclude-exact]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET     path to the dataset/graph specification to use
  --visualize           visualize the vertex cover or not
  --plot-path PLOT_PATH
                        path to directory in which to save the visualization plots
  --exclude-exact       use only approximation algorithms (exclude the exact algorithm)
```

```
usage: sat-reductions specific [-h] --dataset DATASET [--visualize] [--plot-path PLOT_PATH] [--algorithm {exact,naive_approx,greedy_logn_approx,greedy_2_approx}]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET     path to the dataset/graph specification to use
  --visualize           visualize the vertex cover or not
  --plot-path PLOT_PATH
                        path to directory in which to save the visualization plots
  --algorithm {exact,naive_approx,greedy_logn_approx,greedy_2_approx}
                        algorithm to use
```

## The Exact Algorithm

The exact algorithm implementation generates all node subsets of incrementing sizes and simply picks the first one that is a valid vertex cover. The following is a pseudocode description of this algorithm.

```
G - graph with num_nodes nodes

proc EXACT(G)
    for subset_size in 1..num_nodes
        for node_subset in combinations(nodes, subset_size)
            if is_cover(subset, G)
                return subset
            endif
        endfor
    endfor
endproc
```

Running our implementation on the first small sample dataset and visualizing the results:
```
python3 vertex-cover-approximations exact --dataset vertex-cover-approximations/sample-data/small_01.graph --visualize --plot-path .
```

The visualizations can be used to check the results on smaller graphs:

![This is an image](./sample-visualization/small_01_exact.svg)


## The Naive Approximation Algorithm

The naive approximation algorithm iterates over the edges and on encountering an uncovered edge adds the first node of the edge to the cover set.

```
G - graph with num_nodes nodes

proc NAIVE_APPROX(G)
    C := empty_set()
    for (u, v) in edges(G)
        if u not in C and v not in C
            C := union(C, u)
        endif
    endfor
    return C
endproc
```

Running our implementation on the first large sample dataset and visualizing the results:
```
python3 vertex-cover-approximations naive_aprox --dataset vertex-cover-approximations/sample-data/large_01.graph
```

## The Greedy logn-Approximation algorithm

The greedy (logn) approximation algorithm selects nodes with the maximum number of adjacent uncovered edges and adds them to the cover set until all edges are covered.

```
G - graph with num_nodes nodes

proc GREEDY_APPROX(G)
    C := empty_set()
    while exist_uncovered_edges(G)
        u := node_max_uncovered(G)
        C := union(C, u)
    endwhile
    return C
endproc
```
Running our implementation on the first large sample dataset and visualizing the results:
```
python3 vertex-cover-approximations greedy_logn_approx --dataset vertex-cover-approximations/sample-data/large_01.graph
```

## The Greedy 2-Approximation algorithm

The naive approximation algorithm iterates over the edges and on encountering an uncovered edge adds both nodes of the edge to the cover set.

Running our implementation on the first large sample dataset and visualizing the results:
```
python3 vertex-cover-approximations greedy_2_approx --dataset vertex-cover-approximations/sample-data/large_01.graph
```
