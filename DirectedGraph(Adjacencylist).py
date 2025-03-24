from Graph_vertex import vertex

class graph:
    vertices = {}
    
    def add_vertex(self, v:vertex):
        if isinstance(v, vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else: 
            return False
    
    def add_edges(self, u, v): # * u -> from and v -> to : so u --> v
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices)):
            print(key, sorted(list(self.vertices[key].neighbors)), end = " " ) # neighbors contains the set from vertex class

my_graph = graph()
# my_graph.add_vertex(vertex_1)
# print(my_graph.add_vertex(vertex(21)))
# my_graph.print_graph() # 1 [] ,21 []
# print(my_graph.add_edges(1, 21)) # True
print(my_graph.add_edges(2, 3)) # False
my_graph.print_graph() # 1 [21] ,21 [1]

for i in range(ord('A'), ord('Z')):
    my_graph.add_vertex(vertex(chr(i)))
edges = ['AB', 'AH', 'AD', 'BG', 'DK']
for edge in edges:
    my_graph.add_edges(edge[0], edge[1])
my_graph.print_graph()