import sys
import json
from collections import defaultdict
from itertools import islice

def get_content(tweet):
    return json.loads(tweet).get("text")

def load_sent_dict(sent_file):
    scores = {}
    lines = sent_file.readlines()
    for line in lines:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def get_score(content, sent_dict):
    score = 0
    if content is None:
        return score
    else:
        words = content.split(' ')
        for w in words:
            score += sent_dict.get(w, 0)
        return score

def get_state(tweet):
    t = json.loads(tweet)
    if t.get('place'):
        country = t.get('place', {}).get('country')
        place_full_name = t.get('place', {}).get('full_name')
        if len(place_full_name.split(', ')) == 2:
            state = place_full_name.split(', ')[1]
            return country, state
    return None, None

def mean(list):
    return sum(list) / len(list)

def sort_by_value(dict):
    return {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1], reverse=True
    )}

def main():
    state_sents_dict = defaultdict(list)
    state_avg_sent_dict = defaultdict(int)
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = load_sent_dict(sent_file)
    for tweet in tweet_file.readlines():
        country, state = get_state(tweet)
        if country == 'United States':
            content = get_content(tweet)
            score = get_score(content, sent_dict)
            state_sents_dict[state].append(score)
    for state in state_sents_dict:
        state_avg_sent_dict[state] = mean(state_sents_dict[state])
    state_avg_sent_dict = sort_by_value(state_avg_sent_dict)
    for state in islice(state_avg_sent_dict, 1):
        print(state)
    

if __name__ == '__main__':
    main()
