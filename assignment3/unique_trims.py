import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1][:-10]
    mr.emit_intermediate(key, None)

def reducer(key, list_of_values):
    mr.emit(key)

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()