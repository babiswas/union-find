class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=list()

   def add_edges(self,u,v):
       self.graph.append((u,v))

   def find(self,u,parent):
     if u!=parent[u]:
        parent[u]=self.find(parent[u],parent)
     return parent[u]

   def union(self,u,v,parent,rank):
       index1=self.find(u,parent)
       index2=self.find(v,parent)
       if index1!=index2:
          if rank[index1]>rank[index2]:
             parent[index2]=index1
             rank[index1]+=1
          elif rank[index2]>rank[index1]:
             parent[index1]=index2
             rank[index2]+=1
          else:
             parent[index1]=index2
             rank[index2]+=1

   def makeset(self):
      rank=[0]*self.vertex
      parent=[i for i in range(self.vertex)]
      for u,v in self.graph:
          index1=self.find(u,parent)
          index2=self.find(v,parent)
          if index1!=index2:
             self.union(index1,index2,parent,rank)
          else:
             return True
      return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   if graph.makeset():
      print("There is a cycle in the graph")
   else:
      print("No cycle in the graph")
   graph1=Graph(6)
   graph1.add_edges(5,0)
   graph1.add_edges(4,0)
   graph1.add_edges(5,2)
   graph1.add_edges(2,3)
   graph1.add_edges(3,1)
   if graph1.makeset():
      print("There is a cycle in the graph")
   else:
      print("No cycle in the graph")
      