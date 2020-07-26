import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: a set of two people
    # value: the friendship relation
    key = (min(record), max(record))
    value = tuple(record)
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: a set of two people
    # value: friendship relations
    if len(list_of_values) == 1:
        relation = list_of_values[0]
        mr.emit((relation[1], relation[0]))

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()