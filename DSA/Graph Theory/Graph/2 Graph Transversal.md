# **Breadth-First Search (BFS)**

## **Introduction**

Breadth-First Search (BFS) is a systematic graph traversal algorithm that explores a graph **level by level**. Starting from a given **source vertex**, BFS visits all immediate neighbors first, then proceeds outward to their neighbors, continuing until all reachable nodes are explored.

BFS uses a **queue** to ensure nodes are visited in the correct order and a **visited structure** to prevent revisiting nodes, especially in graphs with cycles.


## **Key Characteristics**

| Feature                  | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Traversal Order          | Level-by-level (breadth-first)                               |
| Data Structure Used      | **Queue (FIFO)**                                             |
| Works On                 | Directed, Undirected, Weighted, Unweighted (weights ignored) |
| Avoiding Repeated Visits | Uses a **visited array/list**                                |
| Traversal Pattern        | Explores the closest vertices before distant ones            |


## **Example (Conceptual)**

Given the adjacency representation:

![frame_3148](https://github.com/user-attachments/assets/2e18ee44-9cc8-432f-8672-65b477292575)

```
0 → 1, 2  
1 → 0, 2  
2 → 0, 1, 3, 4  
3 → 2  
4 → 2
```

BFS starting from **0** produces:

```
0 → 1 → 2 → 3 → 4
```

Traversal order reflects node distance from the source.


## **BFS on Connected Graphs**

When the graph is connected, BFS starting from a single source will reach **all vertices**. The traversal maintains a growing queue of discovered but unprocessed vertices.

### **Traversal Phases**

1. Select a source vertex and mark it visited
2. Enqueue the source
3. Repeatedly remove a vertex from the queue
4. Visit each of its unvisited neighbors
5. Mark neighbors visited and enqueue them

BFS continues until the queue is empty.

|||
|-|-|
|![bfs_on_graph_9](https://github.com/user-attachments/assets/4a881445-4d15-4369-9e39-00aac1494475)  | |
| ![bfs_on_graph_10](https://github.com/user-attachments/assets/80a8b96a-1b76-4742-b2ab-4371e0122544) | ![bfs_on_graph_2](https://github.com/user-attachments/assets/70e369e9-dc56-4a68-8826-154149c5c148) |
| ![bfs_on_graph_3](https://github.com/user-attachments/assets/f78ffec9-8612-4568-bc16-749c9da79a57) | ![bfs_on_graph_4](https://github.com/user-attachments/assets/7819b5ef-3a17-44b9-aa97-f7a9a4500779) |
| ![bfs_on_graph_11](https://github.com/user-attachments/assets/ccdbb7d2-8e99-4c3d-838d-01525dcc63b8) | ![bfs_on_graph_5](https://github.com/user-attachments/assets/9b642d0f-a713-4d45-bea3-1e4facf991c4) |
| ![bfs_on_graph_6](https://github.com/user-attachments/assets/50166c0a-4fb2-4a11-a73b-4fb35ee21cb5) | ![bfs_on_graph_7](https://github.com/user-attachments/assets/2ee37d71-418c-4df1-8408-01d8d9d3cab7) |



## **BFS on Disconnected Graphs**

In disconnected graphs, a BFS starting at one vertex may not reach all vertices. To ensure complete traversal:

* Iterate over all vertices
* If a vertex is **not visited**, perform a BFS from it
* This ensures BFS covers **all connected components**


## **Time and Space Complexity**

| Complexity Type      | Value        | Explanation                            |
| -------------------- | ------------ | -------------------------------------- |
| **Time Complexity**  | **O(V + E)** | Each vertex and edge is processed once |
| **Space Complexity** | **O(V)**     | Queue + visited array storage          |

Where:

* **V = number of vertices**
* **E = number of edges**



## **Applications of BFS**

| Application Area         | Usage                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **Shortest Path**        | Finds shortest path in **unweighted graphs**                                                 |
| **Cycle Detection**      | Detects cycles in both directed and undirected graphs                                        |
| **Connected Components** | Identifies separate components in a disconnected graph                                       |
| **Network Routing**      | Used in routing algorithms (e.g., message broadcasting)                                      |
| **Topological Concepts** | Basis for **Kahn’s Algorithm**, **Prim’s Algorithm**, and BFS-based spanning tree generation |
| **Maze & Game Maps**     | Pathfinding in grids and puzzles                                                             |



## **Comparison with DFS**

| Feature        | BFS                                     | DFS                           |
| -------------- | --------------------------------------- | ----------------------------- |
| Strategy       | Level order                             | Depth-first                   |
| Data Structure | Queue                                   | Stack                         |
| Best For       | Shortest path, layered exploration      | Backtracking, cycle detection |
| Memory Usage   | Higher (stores multiple nodes in queue) | Lower (stack-based)           |



## **Output Format**

The BFS traversal always outputs a sequence representing the order in which nodes are visited, e.g.:

```
[0, 1, 2, 3, 4]
```

---


# **Depth-First Search (DFS) – Graph Traversal**


## **Introduction**

Depth-First Search (DFS) is a graph traversal algorithm that explores a graph by following one path as deeply as possible before backtracking. It uses recursion or an explicit **stack** to keep track of traversal order. A **visited structure** ensures nodes are not processed more than once, especially in graphs with cycles.

DFS traversal order depends on the order in which adjacent vertices are selected — therefore, multiple DFS orders are possible for the same graph.


## **Key Characteristics**

| Feature             | Description                                         |
| ------------------- | --------------------------------------------------- |
| Traversal Approach  | Deep path exploration before backtracking           |
| Data Structure Used | **Stack** (implicit via recursion or explicit)      |
| Works On            | Directed and undirected graphs                      |
| Handling Cycles     | Uses a visited array to avoid infinite loops        |
| Order Variations    | Different adjacency order → different DFS sequences |


## **Conceptual Example**

![frame_3148](https://github.com/user-attachments/assets/41e0aa7f-8d07-4680-ab52-c8c3db12d664)

Given adjacency structure:

```
0 → 1, 2
1 → 0, 2
2 → 0, 1, 3, 4
3 → 2
4 → 2
```

DFS starting from vertex **0** produces:

```
0 → 1 → 2 → 3 → backtrack → 4
```

Final traversal sequence:

```
[0, 1, 2, 3, 4]
```

Different traversal orders are possible depending on how adjacency is processed.


## **DFS on Connected Graphs**

DFS begins from a designated **source vertex** and follows a complete path until no unvisited neighbor remains. Then, backtracking occurs to explore remaining unexplored branches.

### **Traversal Flow**

1. Choose starting node and mark it visited
2. Move to an unvisited neighbor
3. Continue until reaching a dead-end (no unvisited neighbors)
4. Backtrack and continue exploring remaining vertices
5. Stop when no reachable vertices remain

|||
|-|-|
| ![dfs_for_a_graph_11](https://github.com/user-attachments/assets/1c568e13-739d-4b7d-8505-75a25832469b) ||
| ![dfs_for_a_graph_1](https://github.com/user-attachments/assets/d0d42ebc-b940-4da5-9da7-9cf760643ee5) | ![dfs_for_a_graph_2](https://github.com/user-attachments/assets/5d569d48-14e9-4b4c-831b-759961498568)  |
| ![dfs_for_a_graph_3](https://github.com/user-attachments/assets/6f4dcf50-180f-40dd-8972-fba57c8c2b03) | ![dfs_for_a_graph_4](https://github.com/user-attachments/assets/f0568edb-d573-4469-9421-3860e8d10137) |
| ![dfs_for_a_graph_5](https://github.com/user-attachments/assets/389364e4-d26b-4050-abc4-ff603c81de22) |![dfs_for_a_graph_12](https://github.com/user-attachments/assets/fd1f8687-d47c-447d-ba9d-d84bfed8e963)  |
| ![dfs_for_a_graph_6](https://github.com/user-attachments/assets/30e153fe-b922-46a6-9de9-551dfc30841b) | ![dfs_for_a_graph_7](https://github.com/user-attachments/assets/e7ed34b9-15dd-4029-9c66-671ff545cbf1) |

## **DFS on Disconnected Graphs**

In disconnected graphs, a single DFS run from one source may not reach all vertices. To ensure full coverage:

* Iterate through all vertices
* If a vertex is unvisited, initiate DFS from that vertex
* This visits every connected component in the graph

This produces a DFS traversal covering the entire graph, not just one component.


## **Time and Space Complexity**

| Complexity Type      | Value        | Reason                                   |
| -------------------- | ------------ | ---------------------------------------- |
| **Time Complexity**  | **O(V + E)** | Each vertex and edge is processed once   |
| **Space Complexity** | **O(V + E)** | Includes recursion stack + visited array |

Where:

* `V = number of vertices`
* `E = number of edges`


## **Applications of DFS**

| Application                     | Purpose                                               |
| ------------------------------- | ----------------------------------------------------- |
| Path and Reachability Detection | Determines if a path exists between two nodes         |
| Detecting Cycles                | Detects cycles in both directed and undirected graphs |
| Topological Sorting             | Fundamental for ordering nodes in DAGs                |
| Strongly Connected Components   | Used in algorithms like Kosaraju and Tarjan           |
| Maze and Puzzle Solving         | Follows a depth-oriented solution pattern             |
| Tree Construction               | Useful in generating DFS spanning trees               |


## **DFS vs BFS (Conceptual)**

| Feature          | DFS                                | BFS                                             |
| ---------------- | ---------------------------------- | ----------------------------------------------- |
| Strategy         | Depth exploration                  | Level-by-level exploration                      |
| Data Structure   | Stack / Recursion                  | Queue                                           |
| Best Use Case    | Backtracking, SCC, cycle detection | Shortest path (unweighted), layered exploration |
| Memory Footprint | Lower on wide graphs               | Higher due to queue storage                     |


## **Output Format Example**

DFS traversal output generally appears as a sequence representing visit order:

```
[0, 2, 1, 3, 4, 5]
```

Exact order depends on adjacency ordering.

---



