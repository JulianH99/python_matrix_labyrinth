def get_mat():
    return [line.split() for line in open('matrix').readlines()]


def search_elem(lst, elem):
    try:
        return lst.index(elem)
    except ValueError:
        return -1


def search_in_mat(mat, elem):
    return [(mat.index(line), line.index(elem)) for line in mat for l in line if l == elem][0]


print(search_in_mat(get_mat(), 'y'), search_in_mat(get_mat(), 'x'))
