class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=None


   def find_minm_weight_tree(self,path,visited):
       minm=float("Inf")
       index=0
       for i in range(self.vertex):
          if (not visited[i]) and path[i]<minm:
             minm=path[i]
             index=i
       return index


   def display(self,parent):
       for i in range(self.vertex):
         print(f"{parent[i]}-->{i}={self.graph[parent[i]][i]}")
 
          
   def prims_algo(self,src):
       path=[float("Inf") for i in range(self.vertex)]
       path[src]=0
       parent=[-1]*self.vertex
       visited=[False]*self.vertex
       for i in range(self.vertex-1):
           index=self.find_minm_weight_tree(path,visited)
           visited[index]=True
           for i in range(self.vertex):
               if visited[i]==False and self.graph[index][i]!=0 and self.graph[index][i]<path[i]:
                  path[i]=self.graph[index][i]
                  parent[i]=index
       self.display(parent)

if __name__=="__main__":
   graph=Graph(5)
   graph.graph=[[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
   graph.prims_algo(0)
   
                  
           
       
       
       