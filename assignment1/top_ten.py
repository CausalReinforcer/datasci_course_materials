import sys
import json
from collections import defaultdict
from itertools import islice

def get_hashtags(tweet):
    hashtags = list()
    hashtags_objs = json.loads(tweet).get('entities', dict()).get('hashtags')
    if hashtags_objs:
        for h in hashtags_objs:
            hashtags.append(h.get('text'))
        return hashtags
    return None

def get_frequency(count_dict):
    freq_dict = defaultdict(int)
    count_total = sum(count_dict.values())
    for w in count_dict:
        freq_dict[w] = count_dict[w] / count_total
    return freq_dict

def sort_by_value(dict):
    return {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1], reverse=True
    )}

def main():
    count_hashtags = defaultdict(int)
    tweet_file = open(sys.argv[1])
    for tweet in tweet_file.readlines():
        hashtags = get_hashtags(tweet)
        if hashtags:
            for h in hashtags:
                count_hashtags[h] += 1
    count_hashtags = sort_by_value(count_hashtags)
    for hashtag in islice(count_hashtags, 10):
        print(hashtag + ' ' + str(count_hashtags[hashtag]))

if __name__ == '__main__':
    main()