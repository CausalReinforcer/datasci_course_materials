import sys
import MapReduce

mr = MapReduce.MapReduce()
matrix_size_limit = 10

def mapper(record):
    matrix = record[0]
    n_row = record[1]
    n_col = record[2]
    v = record[3]
    for i in range(matrix_size_limit):
        if matrix == 'a':
            mr.emit_intermediate((n_row, i), (n_col, v, 'a'))
        if matrix == 'b':
            mr.emit_intermediate((i, n_col), (n_row, v, 'b'))

def reducer(key, list_of_values):
    # key: index of the result matrix
    # value: elements from the two matrices to be multiplied
    matrices = set([v[2] for v in list_of_values])
    if len(matrices) != 2:
        return None
    result = 0
    for i in range(matrix_size_limit):
        sublist = [v[1] for v in list_of_values if v[0] == i]
        if len(sublist) == 2:
            result += sublist[0] * sublist[1]
    mr.emit((key[0], key[1], result))

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()
