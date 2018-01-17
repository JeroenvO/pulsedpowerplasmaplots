import operator
import os
import pickle

import numpy as np


def load_pickle(path):
    if path[-4:] != '.pkl':
        if path[-5] == '.' or path[-4] == '.':
            # random file with extension
            return None
        elif path[-8:] != 'data.pkl':
            path = path + '/data.pkl'
        else:
            path = path + '.pkl'

    if not os.path.exists(path):
        path = 'G:/Prive/MIJN-Documenten/TU/62-Stage/' + path  # try full path.

    assert os.path.exists(path)

    with open(path, 'rb') as f:
        d = pickle.load(f)
        assert any(d)
        return d


def get_values(dicts, key):
    """
    Get all values from a list of dicts with a given key
    stop if list is empty or zero

    :param dicts: the list of dicts to search
    :param key: the key to search each dict for
    :return: list of values
    """
    # assert key in dicts[0]
    a = np.array([d[key] if key in d else 0 for d in dicts])
    # assert any(a)
    return a


def load_pickles(dir, filename='data.pkl'):
    """
    Load pickles from all directories in a path.

    :param dir: dir with subdirs which have data.pkl
    :return: list of dicts with processed measure data
    """
    data = []
    if not os.path.exists(dir):
        dir = 'G:/Prive/MIJN-Documenten/TU/62-Stage/' + dir  # try full path.

    dirs = os.listdir(dir, )

    for tdir in dirs:
        if os.path.isdir(dir+'/'+tdir):
            try:
                data += load_pickle(dir + '/' + tdir + '/' + filename)
            except:
                pass  # invalid dir
    assert any(data)
    return data


def filter_data(data, **kwargs):
    """
    Filter a list of dicts for given key=value in the dict
    append '__<operator>' at key to choose custom operator from operator module.

    :param data: data to filter, array of dicts from pickle file
    :param kwargs: key=value, where key is key of dict and value is value to filter.
    :return: filtered data
    """
    assert any(data)
    for key, value in kwargs.items():
        key = key.split('__')
        op = key[1] if len(key) == 2 else 'eq'
        f = getattr(operator, op)
        # only check data[0], assume all dicts have the same keys
        assert key[0] in data[0], 'Key is not found in dictionary!'
        if op in ['contains']:  # reverse order of arguments for these ops.
            data = [d for d in data if f(value, d[key[0]])]
        else:
            data = [d for d in data if f(d[key[0]], value)]
    return data


def sort_data(data, key):
    """
    Sort a list of dicts by a given key

    :param data: input list of dicts
    :param key: key to sort
    :return: sorted list of dicts
    """
    return sorted(data, key=lambda k: k[key])

