class Node:
    def __init__(self, id, label):
        self.id = id
        self.label = label
        self.neighbours = []

    def __str__(self):
        return "(%s: %s)" % (self.id, self.label)

    def add_neighbour(self, neighbour, label):
        """
        Add a neighbour to this node with
        a given edge label
        e.g. x.add_neighbour(y, "brother")
        """
        self.neighbours.append((neighbour, label))

    def get_neighbours(self, label):
        """
        Returns a list of node objects that are
        neighbours of this node with a given edge label
        Return an empty list if there are no neighbours
        with the given label
        Return all neighbours if label is None
        e.g. x.get_neighbours("brother")
        """
        neighs = []
        if (not label):
            for node,lbl in self.neighbours: neighs.append(node)
        else:
            for node,lbl in self.neighbours:
                if (lbl == label): neighs.append(node)
        return neighs

    def degree(self, label):
        """
        Returns the number of neighbours with a given
        edge label
        Return total number of neighbours
        if label is None
        """
        if (not label): return len(self.neighbours)
        count = 0
        for node,lbl in self.neighbours:
            if (lbl == label): count += 1
        return count

    def has_neighbour(self, node, label):
        """
        Returns True if this node has 'node' as a
        neighbour with a given label, False otherwise
        Returns True if this node has 'node' as a
        neighbour if label is None, False otherwise
        """
        if (not label):
            for currentNode,lbl in self.neighbours:
                if (currentNode == node): return True
            return False
        else:
            for currentNode,lbl in self.neighbours:
                if (currentNode == node and lbl == label) : return True
            else: return False
