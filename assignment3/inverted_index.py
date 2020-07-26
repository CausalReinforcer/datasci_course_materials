import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of appearing documents
    docs = set()
    for v in list_of_values:
        docs.add(v)
    mr.emit((key, list(docs)))

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()
