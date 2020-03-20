'''

Translate the problem into graph terminology
Build your graph
Traverse your graph

Suppose we have some input data describing a graph of relationships 
between parents and children over multiple generations. 

The data is formatted as a list of (parent, child) pairs, 
where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 
3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```

given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – 
the one at the farthest distance from the input individual. 

If there is more than one ancestor tied for "earliest", 
return the one with the lowest numeric ID. 

If the input individual has no parents, the function should return -1.

```
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

        self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
'''


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)
        else:
            raise IndexError("One of the vertices does not exists")

    def get_parent(self, vertex_id):
        return self.vertices[vertex_id]
    
    def take_values(self, ancestors):
        for pair in ancestors:
            if pair[1] not in self.vertices:
                self.add_vertex(pair[1])
            if pair[0] not in self.vertices:
                self.add_vertex(pair[0])
            self.add_edge(pair[0], pair[1])
    

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    g.take_values(ancestors)

    s = Stack()
    s.push([starting_node])
    visited = set()
    longest_path = 1
    min_parent = 100000

    if len(g.get_parent(starting_node)) == 0:
        return -1
    else:
        while s.size() > 0:
            path = s.pop()
            last_node = path[-1]
            if longest_path < len(path):
                longest_path = len(path)
                min_parent = last_node
            if longest_path == len(path):
                if min_parent > last_node:
                    min_parent = last_node
            for parents in g.get_parent(last_node):
                new_path = path.copy()
                new_path.append(parents)
                s.push(new_path)
        return min_parent
    




   

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3))
