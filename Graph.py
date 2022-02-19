# python code for graph implementation using dictionary and find the all the paths from source to 
#destination and then print the shortest path

graph= {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}

def find_paths(graph, start, end, path=[]):
    path= path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths=[]
    for node in graph[start]:
        if node not in path:
            new_paths= find_paths(graph, node, end, path)
            for newpath in new_paths:
                paths.append(newpath)
    return paths

# Program to find the shortest paths

def Shortest_paths(graph, start, end, path=[]):
    path= path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    shortest= None
    for node in graph[start]:
        if node not in path:
            new_path= Shortest_paths(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) <= len(shortest):
                    shortest=new_path
                    
    return shortest

def main():
    print("The possible paths from start to end", find_paths(graph, 'A', 'D'))
    print("The shortest path", Shortest_paths(graph, 'A','D'))

if __name__ == "__main__":
    main()
