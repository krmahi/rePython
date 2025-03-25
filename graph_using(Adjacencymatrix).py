from Graph_vertex import vertex_matrix

class graph:
    vertices = {} # to check if vertex in graph
    edges = []
    edge_indices = {}

    def add_vertex(self,v:vertex_matrix):
        if isinstance(v, vertex_matrix) and v.name not in self.vertices:
            self.vertices[v.name] = v
        
            # append 0 to the newly created col in edges
            for row in self.edges:
                row.append(0)
        
            # append last row in edges with 0 (last row is of the latest vertex)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[v.name] = len(self.edge_indices)
            return True
        else: return False
    
    def add_edges(self, u, v, weight = 1): #* weight's default value is 1, for weighted edges just pass a weight in the parameters
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight # for undirected graph
            return True
        else: return False

    def print_graph(self):
        for v, idx in sorted(self.edge_indices.items()):
            print(v, end = " ")
            for j in range(len(self.edges)):
                print(self.edges[idx][j], end = " ")
            print()
    
my_graph = graph()
# print(my_graph.add_vertex(vertex_matrix('A')))
# print(my_graph.add_vertex(vertex_matrix('B')))
# my_graph.add_edges('A', 'B')
# my_graph.print_graph()

for i in range(ord('A'), ord('K')):
    my_graph.add_vertex(vertex_matrix(chr(i)))
my_graph.print_graph()

print()

edges = ['AB', 'AH', 'AD', 'BG', 'DK']
for edge in edges:
    my_graph.add_edges(edge[0], edge[1])
my_graph.print_graph()
