class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = {i:None for i in range(len(graph))}
        visited = set()
        return self.allPaths(graph, 0, paths, visited)
    
    def allPaths(self, graph, i, paths, visited):
        if i in visited:
            return []
        elif i==len(graph)-1:
            return [[i]]
        elif paths[i] is not None:
            return paths[i]
        visited.add(i)
        for vals in graph[i]:
            thesePaths = self.allPaths(graph, vals, paths, visited)
            if thesePaths:
                for currentPath in thesePaths:
                    if paths[i] is not None:
                        paths[i].append([i]+currentPath)
                    else:
                        paths[i] = [[i]+currentPath]
        visited.remove(i)
        if paths[i] is None:
            paths[i] = []
        return paths[i]