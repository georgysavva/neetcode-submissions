class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        status = [None] * numCourses
        for (a, b) in prerequisites:
            graph[a].append(b)
        for node in range(numCourses):
            cycle=self.traverse(graph,node,status)
            if cycle:
                return False
        return True
    def traverse(self, graph, node, status):
        if status[node] == 'visited':
            return False
        if status[node] == 'visiting':
            return True
            
        status[node]='visiting'
        for child in graph[node]:
            cycle=self.traverse(graph, child, status)
            if cycle:
                return True
        status[node]='visited'
        return False