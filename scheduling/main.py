from collections import defaultdict

end = False
r, c, n = input().strip().split()
r = int(r)
c = int(c)
n = int(n)


def Ford_Fulkerson(g, source, sink):
    parent = [-1] * (len(g))
    max_flow = 0
    while BFS(g, source, sink, parent):
        path = 1000000000
        s = sink
        while s != source:
            path = min(path, graph[parent[s]][s])
            # print(path)
            s = parent[s]
        max_flow += path
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path
            graph[v][u] += path
            v = parent[v]

    return max_flow


def BFS(g, start, end, parent):
    visited = [False] * len(g)
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        for node, val in enumerate(g[vertex]):
            if not visited[node] and val > 0:
                queue.append(node)
                visited[node] = True
                parent[node] = vertex
                if node == end:
                    return True
    return False


while not end:
    if r == 0 and c == 0 and n == 0:
        break
    edge_list = []
    courses = []
    for i in range(r):
        name, course = input().strip().split()
        temp_list = [name, course]
        edge_list.append(temp_list)
    course_capacity = defaultdict(list)
    for i in range(c):
        course, capacity = input().strip().split()
        courses.append(course)
        course_capacity[course].append(capacity)
    # print(course_capacity)

    adjacency_list = defaultdict(list)
    for node in edge_list:
        adjacency_list[node[0]].append(node[1])
    # print(adjacency_list)
    course_to_node = defaultdict(list)
    student_to_node = defaultdict(list)
    num_classes = c
    num_people = int(len(adjacency_list.keys()))
    course_start_index = (num_people + num_classes + 2) - num_people
    for course in courses:
        # temp_list = [course[0], course_start_index]
        course_to_node[course].append(course_start_index)
        course_start_index = course_start_index + 1
    # print(course_to_node)

    graph = [[0 for x in range(num_people + num_classes + 2)] for y in range(num_people + num_classes + 2)]
    index_value = 1
    for i in range(num_people):
        students = list(adjacency_list.keys())
        student_to_node[students[i]].append(index_value)
        index_value = index_value + 1
    # print(student_to_node)

    for i in range(1, len(students) + 1):
        graph[0][i] = n

    # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    # for row in graph]))

    for key, value in adjacency_list.items():
        student_node = student_to_node.get(key)[0]
        # print(student_node)
        for course in value:
            course_node = course_to_node.get(course)[0]
            graph[student_node][course_node] = 1
            cap = int(course_capacity.get(course)[0])
            graph[course_node][len(graph) - 1] = cap

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in graph]))

    input()
    if Ford_Fulkerson(graph, 0, len(graph) - 1) >= n * num_people:
        print("Yes")
    else:
        print("No")

    r, c, n = input().strip().split()
    r = int(r)
    c = int(c)
    n = int(n)
