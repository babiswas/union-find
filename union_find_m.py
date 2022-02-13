class Graph:
  def __init__(self,vertex):
      self.vertex=vertex
      self.graph=list()

  def add_edges(self,u,v):
      self.graph.append((u,v))

  def find(self,u,parent):
     while parent[u]!=-1:
         u=parent[u]
     return u

  def union(self,u,v,parent):
     index1=self.find(u,parent)
     index2=self.find(v,parent)
     if index1!=index2:
        parent[index1]=index2

  def union_find(self):
     parent=[-1]*self.vertex
     for u,v in self.graph:
         print(parent)
         index1=self.find(u,parent)
         index2=self.find(v,parent)
         if index1!=index2:
            self.union(index1,index2,parent) 
     return parent

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   print(graph.union_find())
       