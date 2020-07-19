import sys
import json
from collections import defaultdict

def get_content(tweet):
    return json.loads(tweet).get("text")

def get_frequency(counts_dict):
    freq_dict = defaultdict(int)
    counts_total = sum(counts_dict.values())
    for w in counts_dict:
        freq_dict[w] = counts_dict[w] / counts_total
    return freq_dict

def main():
    counts_dict = defaultdict(int)
    tweet_file = open(sys.argv[1])
    tweets = tweet_file.readlines()
    for tweet in tweets:
        content = get_content(tweet)
        if content:
            words = content.strip().split()
            for w in words:
                counts_dict[w] += 1
    freq_dict = get_frequency(counts_dict)
    for w in freq_dict:
        print("{} {:.4f}".format(w, float(freq_dict[w])))

if __name__ == '__main__':
    main()
