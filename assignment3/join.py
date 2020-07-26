import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    # key: order_id
    # value: a tuple of (record_type, record_value)
    key = record[1]
    record_type = record[0]
    value = (record_type, record)
    mr.emit_intermediate(key, value)
    
def reducer(key, list_of_values):
    # key: order_id
    # value: a list of joined records
    orders = [v[1] for v in list_of_values if v[0] == 'order']
    line_items = [v[1] for v in list_of_values if v[0] == 'line_item']
    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)

def main():
    input_data = open(sys.argv[1])
    mr.execute(input_data, mapper, reducer)

if __name__ == '__main__':
    main()
