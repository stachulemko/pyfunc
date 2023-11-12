class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.inf = float('inf')
        self.graph = [[self.inf] * self.V for _ in range(self.V)]
        self.next = [[-1] * self.V for _ in range(self.V)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def find_min_avg_cost_node(self):
        min_avg_cost_node = None
        min_avg_cost = float('inf')

        for node in range(self.V):
            total_cost = 0
            num_edges = 0
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph[i][j] != self.inf:
                        total_cost += self.graph[i][j]
                        num_edges += 1
            if num_edges > 0:
                avg_cost = total_cost / num_edges
                if avg_cost < min_avg_cost:
                    min_avg_cost = avg_cost
                    min_avg_cost_node = node

        return min_avg_cost_node

    def floyd_warshall(self):
        for i in range(self.V):
            for j in range(self.V):
                self.next[i][j] = j if i != j and self.graph[i][j] != self.inf else -1

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph[i][k] + self.graph[k][j] < self.graph[i][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
                        self.next[i][j] = self.next[i][k]

    def print_path(self, u, v):
        if self.next[u][v] == -1:
            return [u, v]
        path = [u]
        while u != v:
            u = self.next[u][v]
            path.append(u)
        return path


if __name__ == "__main__":
    num_nodes = 4
    num_edges = 5
    g = Graph(num_nodes)

    g.add_edge(1, 2, 3)
    g.add_edge(0, 3, -2)
    g.add_edge(3, 2, 10)
    g.add_edge(2, 0, 2)
    g.add_edge(0, 1, 2)

    g.floyd_warshall()
    min_avg_cost_node = g.find_min_avg_cost_node()

    if min_avg_cost_node is not None:
        print(
            f"Węzeł, który minimalizuje średni koszt przejścia i powrotu, to {min_avg_cost_node} z kosztem {g.graph[min_avg_cost_node][min_avg_cost_node]:.2f}.")
        path = g.print_path(min_avg_cost_node, min_avg_cost_node)
        print(path)
        print("Optymalna ścieżka:", "->".join(map(str, path)))
    else:   
        print("Nie można znaleźć węzła spełniającego warunek.")
