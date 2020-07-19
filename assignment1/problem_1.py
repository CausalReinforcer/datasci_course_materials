# Read the first 20 records in `three_minutes_tweets.json`
# Then write it into `problem_1_submission.txt`

import json

output = []

with open('three_minutes_tweets.json', 'r') as f:
    for i in range(20):
        line = f.readline()
        record = json.loads(line)
        output.append(record)

with open('problem_1_submission.txt', 'w') as output_file:
    for i in output:
        json.dump(i, output_file)
        output_file.write('\n')