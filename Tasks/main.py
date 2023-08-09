from collections import defaultdict


def top_sort_recurse(v, visited, stack, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            top_sort_recurse(i, visited, stack, graph)
    stack.append(activities[v])


def top_sort(graph):
    visited = [False] * t
    stack = []

    for i in range(t):
        if not visited[i]:
            top_sort_recurse(i, visited, stack, graph)

    return stack[::-1]


activities = []

t, d = input().split()
t = int(t)
d = int(d)

for i in range(t):
    element = input()
    activities.append(element)

edge_list = []

for j in range(d):
    parent, depend = input().split()
    parent = activities.index(parent)
    depend = activities.index(depend)
    edge_list.append([parent, depend])

adjacency_list = defaultdict(list)
for node in edge_list:
    adjacency_list[node[0]].append(node[1])

stack = top_sort(adjacency_list)

for i in range(t):
    print(stack[i] + " ", end='')
