class vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)

class graph:
    vertices = {}

    def add_vertex(self, v: vertex):
        if isinstance(v, vertex) and v.name not in self.vertices: # * isinstance(obj, class) to check if the obj belongs to the class
            self.vertices[v.name] = v
            return True
        else:
            return False

    # todo: for a directed graph we are just gonna change add_edges method
    def add_edges(self,u ,v): # * u and v are not vertex objects but names of vertices
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices)): # * map is unsorted (if we want to print in sorted order we have to convert to list)
            print(key, sorted(list(self.vertices[key].neighbors)), end = " ") # ! we cannot use map.values bcz object is not iterable


my_graph = graph()
# vertex_1 = vertex(1)
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
