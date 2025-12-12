# Pre-In-Post order transversal

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) {
        data = value;
        left = right = NULL;
    }
};

// Preorder: Root → Left → Right
void preorder(Node* root) {
    if (root == NULL) return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

// Inorder: Left → Root → Right
void inorder(Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

// Postorder: Left → Right → Root
void postorder(Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " ";
}

int main() {

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "Preorder: ";
    preorder(root);
    cout << endl;

    cout << "Inorder: ";
    inorder(root);
    cout << endl;

    cout << "Postorder: ";
    postorder(root);
    cout << endl;

    return 0;
}

```

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
