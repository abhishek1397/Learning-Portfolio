# DFS

```cpp
#include <iostream>
using namespace std;

#define V 5

void DFS(int graph[][V], int node, bool visited[]) {
    visited[node] = true;
    cout << node << " ";

    for (int i = 0; i < V; i++) {
        if (graph[node][i] == 1 && !visited[i]) {
            DFS(graph, i, visited);
        }
    }
}

int main() {

    int graph[V][V] = {
        {0, 0, 1, 0, 1},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0},
        {1, 0, 1, 1, 1},
        {0, 1, 0, 0, 0}
    };

    bool visited[V] = {false};

    cout << "DFS Traversal: ";
    DFS(graph, 0, visited);

    return 0;
}
```


# BFS

```cpp
#include <iostream>
#include <queue>
using namespace std;

#define V 5

void BFS(int graph[][V], int start) {
    bool visited[V] = {false};
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "BFS Traversal: ";

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        cout << node << " ";

        for (int i = 0; i < V; i++) {
            if (graph[node][i] == 1 && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main() {

    int graph[V][V] = {
        {0, 0, 1, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 1, 0, 0, 1},
        {1, 0, 1, 0, 1},
        {1, 0, 1, 0, 0}
    };

    BFS(graph, 0);

    return 0;
}

```
