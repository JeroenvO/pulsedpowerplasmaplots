import pickle
import functools
import operator

def load_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

def get_values(dicts, key):
    return [d[key] if key in d else 0 for d in dicts]
