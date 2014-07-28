from node import Node

class Graph:
    def __init__(self, label, filename):
        """
        Initialise a graph with a given label.
        If filename is not None, load the graph from the file
        """
        self.nodes = []
        self.label = label
        self.relationships = []
        self.paths = 0
        if (filename): self.load(filename)

    def size(self):
        """
        Return the number of nodes in the graph
        """
        return len(self.nodes)

    def _getNode(self, id):
        for node in self.nodes:
            if (node.id == id): return node
        else: return None

    def _readNode(self, line):
        line = line.split(": ")
        if (not self._getNode(line[0])):
            self.nodes.append(Node(line[0], line[1]))
        else: raise ValueError("Node with this ID already exists")

    def _readRelationship(self, line):
        line = line.split(":")
        try:
            self._getNode(line[0]).add_neighbour(self._getNode(line[2]),line[1])
        except AttributeError:
            raise ValueError("Node does not exist")

    def load(self, filename):
        """
        Load the graph from the given filename.
        Raise ValueError if a node with a duplicate
        id is added or if a relationship between
        nonexisting nodes is created
        """
        readingRelationships = False
        for line in open(filename,'r').readlines():
            line = line.strip()
            if (line == ""):
                readingRelationships = True
                continue
            if (readingRelationships):
                self._readRelationship(line)
            else: self._readNode(line)
        self.nodes.sort(key = lambda x: x.id)

    def output(self):
        """
        Prints the graph with nodes listed in sorted order
        of ids with their neighbours and neighbour labels
        If neighbour labels are None, print the empty
        string.
        Print empty brackets if a node has no neighbours
        e.g.
        (0: Bob) [1:son, 2:wife]
        (1: John) [0:father, 2:mother]
        (2: Jane) [0:husband, 1:son]
        (3: Greg) [1:friend]
        """
        for node in self.nodes:
            nodeStr = str(node)
            neighbours = []
            for label in node.neighbours:
                nodeSet = node.neighbours[label]
                for outNode in nodeSet:
                    neighbours.append((label, outNode.id))
            neighbours.sort(key = lambda x: x[1])
            outStr = "["
            for label,id in neighbours: outStr += "%s:%s, " % (id, label)
            if (len(outStr) > 1): outStr = outStr[:-2]
            outStr += "]"
            print (node, outStr)

    def degrees_of_separation(self, n1, n2):
        """
        Returns the minimum degrees of separation from
        n1 to n2, where n1 and n2 are ids.
        Each x on the path between n1
        and n2 fulfills the has_neighbour relationship.
        Return -1 if n1 and n2 are not connected.
        Raise ValueError if either n1 or n2 is not in
        this graph
        If n1 is a neighbour of n2, then there is
        1 degree of separation.
        e.g. graph.degrees_of_separation(x, y)
        """
        self.get_node(n1)
        self.get_node(n2)
        todo = [[n1]]
        while (len(todo) >0):
            path = todo.pop(0)
            if (self._getNode(path[-1]).id == n2):
                return len(path)-1
            latestNode = self._getNode(path[-1])
            for node in latestNode.get_neighbours(None):
                if (node.id not in path):
                    p = path.copy()
                    p.append(node.id)
                    todo.append(p)
        return -1

    def get_node(self, id):
        """
        Returns the node with the given id
        Raise ValueError if no node with the id exists
        """
        for node in self.nodes:
            if node.id == id:
                return node
        else: raise ValueError()
