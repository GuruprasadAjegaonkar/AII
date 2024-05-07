def dfs(graph,start_node):
    visited=set()
    def dfs_util(node):
        if node not in visited:
            print(node)
            visited().add(node)
            for neighbour in graph[node]:
                dfs_util(neighbour)
    dfs_util(start_node)

def bfs(graph,start_node):
    visited=set()
    queue=[]
    visited.add(start_node)
    queue.append(start_node)
    while queue:
        current_node=queue.pop(0)
        print(current node,end="")
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

graph={}

num_edges=int(input("enter nu of edges"))
print("number of edges source and destination")
for _ in range(num_edges):
    edge=input().split()
    source,destination=edge
    if source not in graph:
        graph[source]=[]
    if destination not in graph:
        graph[destination]=[]
    graph[source].append(destination)

start_node_dfs=input("enter starting node of dfs")
print("depth first search")
dfs(graph,start_node)

start_node_bfs=input("enter start node of bfs")
prind("best first search")
bfs(graph,start_node)
