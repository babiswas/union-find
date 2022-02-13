class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=list()

   def add_edges(self,u,v,w):
       self.graph.append((u,v,w))

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

   def krushkal(self):
       edges=list()
       parent=[i for i in range(self.vertex)]
       rank=[0]*self.vertex
       def get_item(obj):
          return obj[2]
       self.graph=sorted(self.graph,key=get_item)
       for u,v,w in self.graph:
          index1=self.find(u,parent)
          index2=self.find(v,parent)
          if index1!=index2:
             self.union(index1,index2,parent,rank)
             edges.append((u,v,w))
       print(edges)

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edges(0,1,4)
   graph.add_edges(0,7,8)
   graph.add_edges(1,7,11)
   graph.add_edges(7,6,1)
   graph.add_edges(7,8,7)
   graph.add_edges(6,8,6)
   graph.add_edges(1,2,8)
   graph.add_edges(8,2,2)
   graph.add_edges(6,5,2)
   graph.add_edges(2,5,4)
   graph.add_edges(2,3,7)
   graph.add_edges(5,3,14)
   graph.add_edges(5,4,10)
   graph.add_edges(3,4,9)
   graph.krushkal()

       
       
        
       
       