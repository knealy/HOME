class Edge:
   def __init__(self, src, tgt):
     self.source = src
     self.target = tgt

class DirectedAdjList:
   def __init__(self, num_vertices):
      self.adj = [[] for _ in range(0,num_vertices)]

   def add_edge(self, u, v):
    # approach 1
      self.adj[u].append(v)   
    # approach 2 (less complex, but takes more space)
      # self.adj[u].append(Edge(u,v)) 

   def out_edges(self, u):
     # return the list of edges whose source is vertex u
      return [Edge(u,v) for v in self.adj[u]]
