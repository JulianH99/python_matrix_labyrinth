class Node:
    def __init__(self, location, children=[]):
        """

        :param location:
        :type location: (int, int)
        :param children:
        :type children: List[Node]
        """
        self.location = location
        self.children = children

    def __str__(self):
        return "{} - {}".format(self.location, self.get_children())

    def get_children(self):
        return [node.__str__() for node in self.children]


def get_mat():
    return [line.split() for line in open('matrix').readlines()]


def search_in_mat(mat, elem):
    return [(mat.index(line), line.index(elem))
            for line in mat
            for l in line
            if l == elem][0]


def build_road(mat):
    return Node(search_in_mat(mat, 'x'), [Node(search_in_mat(mat, 'y'))])


print(build_road(get_mat()))
