import os
import pickle
import operator
import numpy as np

markers = ['+', 'o', '*', 'v', 'x', 'd', '>', '<', ',', '.']


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


def save_file(fig, name='plot', path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots', **kwargs):
    """
    Save a file as png, eps and pdf

    :param fig: figure to save
    :param name: filename to save as, without extension
    :param path: path to save the file, default to /plots/
    :param kwargs: extra kwargs to send to savefig, for instance bbox_extra_artists
    :return: None
    """

    fig.savefig(path + '/' + name + '.png', bbox_inches='tight', **kwargs)
    # fig.savefig(path + '/' + name + '.eps', bbox_inches='tight', **kwargs)
    fig.savefig(path + '/' + name + '.pdf', bbox_inches='tight', **kwargs)


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
        assert key[0] in data[0], 'Key is not found in dictionary!'  # only check data[0], assume all dicts have the same keys
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


def move_sn_y(ax, offs=0, dig=0, side='left', omit_last=False):
    """
    Copied from https://github.com/prisae/blog-notebooks/blob/master/MoveSciNot.ipynb
    https://werthmuller.org/blog/2014/move-scientific-notation/

    Move scientific notation exponent from top to the side.

    Additionally, one can set the number of digits after the comma
    for the y-ticks, hence if it should state 1, 1.0, 1.00 and so forth.

    Parameters
    ----------
    offs : float, optional; <0>
        Horizontal movement additional to default.
    dig : int, optional; <0>
        Number of decimals after the comma.
    side : string, optional; {<'left'>, 'right'}
        To choose the side of the y-axis notation.
    omit_last : bool, optional; <False>
        If True, the top y-axis-label is omitted.

    Returns
    -------
    locs : list
        List of y-tick locations.

    Note
    ----
    This is kind of a non-satisfying hack, which should be handled more
    properly. But it works. Functions to look at for a better implementation:
    ax.ticklabel_format
    ax.yaxis.major.formatter.set_offset_string
    """
    import matplotlib.pyplot as plt
    # Get the ticks
    locs = ax.get_yticks()

    # Put the last entry into a string, ensuring it is in scientific notation
    # E.g: 123456789 => '1.235e+08'
    # only if it is already in powers
    if 1e3 > locs[0] > 1000:
        llocs = '%.3e' % locs[-1]

        # Get the magnitude, hence the number after the 'e'
        # E.g: '1.235e+08' => 8
        yoff = int(str(llocs).split('e')[1])

        # If omit_last, remove last entry
        if omit_last:
            slocs = locs[:-1]
        else:
            slocs = locs

        # Set ticks to the requested precision
        form = r'$%.' + str(dig) + 'f$'
        # ax.set_yticks(locs, )
        locs = ax.set_yticks(locs)
        labels = ax.set_yticklabels(list(map(lambda x: form % x, slocs / (10 ** yoff))))
        # plt.yticks(locs, list(map(lambda x: form % x, slocs / (10 ** yoff))))

        # Define offset depending on the side
        if side == 'left':
            offs = -.18 - offs  # Default left: -0.18
        elif side == 'right':
            offs = 1 + offs  # Default right: 1.0

        # Plot the exponent
        ax.text(offs, .98, r'$\times10^{%i}$' % yoff, transform=
        ax.transAxes, verticalalignment='top')

        # Return the locs
        return locs


def set_plot(fig, plot_height=1, pulse=False):
    """
    Set plot settings for IEEE paper, combined with /plots_final/matplotlibrc
    https://www.bastibl.net/publication-quality-plots/

    :param fig: fig to set
    :param plot_height: number of subplots in height
    :param pulse: Whether a pulse is shown (cuts the plot to 1us pulse time)
    :return:
    """
    width = 3.487
    height = width / 1.618 * plot_height

    for ax in fig.axes:
        ax.grid(True)
        if pulse:
            ax.set_xlim([-0.2, 2])
            ax.set_xlabel('time [$\mu$s]')
        locs = move_sn_y(ax, offs=0.03, side='left', dig=1)
    fig.set_size_inches(width, height)
    fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)
