# Prim’s Algorithm (Adjacency Matrix)

```cpp

#include <iostream>
using namespace std;

#define V 5
#define INF 999999

int minKey(int key[], bool mstSet[]) {
    int min = INF, index = -1;
    for (int i = 0; i < V; i++)
        if (!mstSet[i] && key[i] < min) {
            min = key[i];
            index = i;
        }
    return index;
}

void primMST(int graph[V][V]) {
    int parent[V], key[V];
    bool mstSet[V] = {false};

    for (int i = 0; i < V; i++)
        key[i] = INF;

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet);
        mstSet[u] = true;

        for (int v = 0; v < V; v++)
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
    }

    cout << "Prim's MST:\n";
    for (int i = 1; i < V; i++)
        cout << parent[i] << " - " << i << "  weight: " << graph[i][parent[i]] << endl;
}

int main() {
    int graph[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    primMST(graph);
    return 0;
}

```


# Kruskal’s Algorithm (Using Disjoint Set / Union-Find)

```cpp
#include <iostream>
using namespace std;

#define V 5
#define INF 999999

int minKey(int key[], bool mstSet[]) {
    int min = INF, index = -1;
    for (int i = 0; i < V; i++)
        if (!mstSet[i] && key[i] < min) {
            min = key[i];
            index = i;
        }
    return index;
}

void primMST(int graph[V][V]) {
    int parent[V], key[V];
    bool mstSet[V] = {false};

    for (int i = 0; i < V; i++)
        key[i] = INF;

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet);
        mstSet[u] = true;

        for (int v = 0; v < V; v++)
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
    }

    cout << "Prim's MST:\n";
    for (int i = 1; i < V; i++)
        cout << parent[i] << " - " << i << "  weight: " << graph[i][parent[i]] << endl;
}

int main() {
    int graph[V][V] = {
        {0, 2, 0, 6, 0},
        {2, 0, 3, 8, 5},
        {0, 3, 0, 0, 7},
        {6, 8, 0, 0, 9},
        {0, 5, 7, 9, 0}
    };

    primMST(graph);
    return 0;
}


```
