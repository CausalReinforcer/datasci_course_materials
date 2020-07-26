import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: a list of friends
    friend_count = len(list_of_values)
    mr.emit((key, friend_count))

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()