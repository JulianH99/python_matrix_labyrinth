from enum import Enum, auto

visited = []


def search_tree(tree, value):
    if tree is None:
        return False
    elif tree.location == value:
        return True
    else:
        return search_children(tree.children, value)

def search_children(children, value):
    if not children:
        return False
    else:
        return search_tree(children[0], value) or search_children(children[1:], value)


class Direction:
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


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
        return [node.__str__() for node in self.children if node]


def get_mat():
    return [line.split() for line in open('matrix').readlines()]


def search_in_mat(mat, elem):
    try:
        return [(mat.index(line), line.index(elem))
                for line in mat
                for l in line
                if l == elem][0]
    except IndexError:
        return None



def get_x_pos(mat):
    return search_in_mat(mat, 'x')


def build_road(mat):

    return run_through(mat, get_x_pos(mat))


def run_through(mat, position):

    global visited

    if out_of_bound(position, mat) or position in visited:
        return None
    else:
        visited.append(position)
        if mat[position[0]][position[1]] == '1':
            return None
        if mat[position[0]][position[1]] == 'y':

            return Node(position)

        return Node(position, [run_through(mat, move(position, Direction.RIGHT)),
                               run_through(mat, move(position, Direction.LEFT)),
                               run_through(mat, move(position, Direction.UP)),
                               run_through(mat, move(position, Direction.DOWN))])


def move(position, direction):
    if direction == Direction.RIGHT:
        return position[0], position[1] + 1
    if direction == Direction.LEFT:
        return position[0], position[1] - 1
    if direction == Direction.DOWN:
        return position[0] + 1, position[1]
    if direction == Direction.UP:
        return position[0] - 1, position[1]


def out_of_bound(position, mat):
    return (position[0] < 0 or position[0] >= len(mat)) or \
           (position[1] < 0 or position[1] >= len(mat[1]))


if __name__ == '__main__':
    if search_tree(build_road(get_mat()), search_in_mat(get_mat(), 'y')):
        print("El laberinto es resolvible")
    else:
        print("El laberinto no es resolvible")


