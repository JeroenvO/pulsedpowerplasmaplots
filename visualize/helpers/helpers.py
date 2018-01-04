import os
import pickle

import numpy as np

markers = ['+', 'o', '*','v','x','d','>','<', ',', '.']

def load_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

def get_values(dicts, key):
    """
    Get all values from a list of dicts with a given key
    stop if list is empty or zero

    :param dicts: the list of dicts to search
    :param key: the key to search each dict for
    :return: list of values
    """
    a = np.array([d[key] if key in d else 0 for d in dicts])
    assert any(a)
    return a

def load_pickles(dir, filename='data.pkl'):
    """
    Load pickles from all directories in a path.

    :param dir: dir with subdirs which have data.pkl
    :return: list of dicts with processed measure data
    """
    data = []
    dirs = os.listdir(dir, )
    for tdir in dirs:
        try:
            data += load_pickle(dir+'/'+tdir+'/'+filename)
        except:
            pass  # invalid dir
    return data

def save_file(fig, name='plot', path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots', **kwargs):
    fig.savefig(path+'/'+name+'.png', bbox_inches='tight', **kwargs)
    fig.savefig(path+'/'+name+'.eps', bbox_inches='tight', **kwargs)
    fig.savefig(path+'/'+name+'.pdf', bbox_inches='tight', **kwargs)