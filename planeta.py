from collections import defaultdict


def strony(n, visited_order):
    adj_list = defaultdict(list)
    in_degree = {chr(97+i): 0 for i in range(n)}
    for pair in visited_order:
        adj_list[pair[0]].append(pair[1])
        in_degree[pair[1]] += 1

    q = [node for node in in_degree if in_degree[node] == 0]
    count = 0
    while q:
        count += 1
        if count == n:
            return count
        node = q.pop(0)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
    return 0


print(strony(2, ["ba"]))
