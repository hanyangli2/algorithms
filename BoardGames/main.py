from collections import defaultdict
def dfs(graph, start, end, numOfIntersections):
    path = []
    visited = [False] * numOfIntersections
    dfs_recurse(graph, start, end, visited, path)
def dfs_recurse(graph, curnode, end, visited, path):
    visited[curnode] = True
    path.append(int(curnode))
    if curnode == end:
        visited[curnode] = False
        print(*path, sep="-")
        path.pop()
        return
    else:
        # adjlist = adjacency_list[curnode]
        for v in adjacency_list[curnode]:
            if visited[v] == False:
                dfs_recurse(graph, v, end, visited, path)
    path.pop()
    visited[curnode] = False
    return


numOfIntersections = int(input())
numOfRoads = int(input())
edge_list = []
i = 0

while i < numOfRoads:
    small_list = []
    x, y = input().split()
    x = int(x)
    small_list.append(x)
    y = int(y)
    small_list.append(y)
    small_list_reverse = []
    small_list_reverse.append(int(y))
    small_list_reverse.append(int(x))
    if small_list not in edge_list and small_list_reverse not in edge_list:
        edge_list.append(small_list)
    i = i + 1
adjacency_list = defaultdict(list)

for node in edge_list:
    adjacency_list[node[0]].append(node[1])
    adjacency_list[node[1]].append(node[0])
for node in adjacency_list:
    adjacency_list[node].sort()

dang_roads = []
numDangRoads = input()
numDangRoads = int(numDangRoads)
j = 0
while j < numDangRoads:
    temp = input()
    temp = int(temp)
    dang_roads.append(temp)
    j += 1
for node in adjacency_list:
    for dangNode in dang_roads:
        if dangNode in adjacency_list[node]:
            adjacency_list[node].remove(dangNode)

for key in list(adjacency_list):
    if key in dang_roads:
        del adjacency_list[key]

for node in adjacency_list:
    adjacency_list[node].sort()

dfs(adjacency_list, 0, numOfIntersections - 1, numOfIntersections)