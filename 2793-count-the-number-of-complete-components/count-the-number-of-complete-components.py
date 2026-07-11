class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph=[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=[False]*n
        ans=0

        def dfs(node):
            visited[node]=True
            nodes=1
            edgesum=len(graph[node])
            
            for nei in graph[node]:
                if not visited[nei]:
                    nNodes, nEdge=dfs(nei)
                    nodes += nNodes
                    edgesum += nEdge

            return nodes, edgesum
        for i in range(n):
            if not visited[i]:
                nodes, edgesum=dfs(i)
                actualEdges = edgesum // 2

                if actualEdges == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans


