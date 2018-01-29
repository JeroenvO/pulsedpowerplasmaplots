import numpy as np
from scipy.interpolate import interp1d

markers = ['o','d', '*', '+', 'v', 'x', 'D', '>', '<', ',', '.']


def save_file(fig, name='plot', path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots', **kwargs):
    """
    Save a file as png, eps and pdf

    :param fig: figure to save
    :param name: filename to save as, without extension
    :param path: path to save the file, default to /plots/
    :param kwargs: extra kwargs to send to savefig, for instance bbox_extra_artists
    :return: None
    """
    if path[0:2] != 'G:':
        path = 'G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/' + path
    fig.savefig(path + '/' + name + '.png', bbox_inches='tight', **kwargs)
    # fig.savefig(path + '/' + name + '.eps', bbox_inches='tight', **kwargs)
    fig.savefig(path + '/' + name + '.pdf', bbox_inches='tight', **kwargs)


def move_sn_y(ax, offs=0, dig=0, side='left', omit_last=False, lower_limit=1e-3, upper_limit=1e3):
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
    # Get the ticks
    locs = ax.get_yticks()

    # Put the last entry into a string, ensuring it is in scientific notation
    # E.g: 123456789 => '1.235e+08'
    # only if it is already in powers
    if locs[-1] > upper_limit or locs[-1] < lower_limit:
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


def set_plot(fig, plot_height=1, pulse=False, subplot=True):
    """
    Set plot settings for IEEE paper, combined with /plots_final_v1/matplotlibrc
    https://www.bastibl.net/publication-quality-plots/

    :param fig: fig to set
    :param plot_height: number of subplots in height
    :param pulse: Whether a pulse is shown (cuts the plot to 1us pulse time)
    :return:
    """
    width = 3.7
    height = width / 1.618 * plot_height
    if not subplot:
        fig.axes[0].grid(True, z_index=-1)  # only one ax has grid
    for ax in fig.axes:
        if pulse:
            ax.set_xlim([-0.2, 2])
            ax.set_xlabel('time [$\mu$s]')
        if subplot:
            ax.grid(True)
        # locs = move_sn_y(ax, offs=0.03, side='left', dig=1)
    fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)
    fig.set_size_inches(width, height, forward=True)
    fig.tight_layout()


def align_y_axis(ax1, ax2, minresax1, minresax2, ticks=7):
    """ Sets tick marks of twinx axes to line up with 7 total tick marks
    https://stackoverflow.com/questions/26752464/how-do-i-align-gridlines-for-two-y-axis-scales-using-matplotlib

    ax1 and ax2 are matplotlib axes
    Spacing between tick marks will be a factor of minresax1 and minresax2
    """

    ax1ylims = ax1.get_ybound()
    ax2ylims = ax2.get_ybound()
    ax1factor = minresax1 * ticks-1
    ax2factor = minresax2 * ticks-1
    ax1.set_yticks(np.linspace(ax1ylims[0],
                               ax1ylims[1]+(ax1factor -
                               (ax1ylims[1]-ax1ylims[0]) % ax1factor) %
                               ax1factor,
                               ticks))
    ax2.set_yticks(np.linspace(ax2ylims[0],
                               ax2ylims[1]+(ax2factor -
                               (ax2ylims[1]-ax2ylims[0]) % ax2factor) %
                               ax2factor,
                               ticks))


def interpolate(x, y, num=1000, kind='linear'):
    """
    Interpolate a line for all points [x, y] and return a x,y line of num length

    :param x: array of x points
    :param y: array of y points
    :param num: number of points in the interpolated line
    :param kind: type of interpolation
    :return:
    """
    assert any(x)
    assert any(y)
    assert len(x) > 2
    assert len(y) > 2
    x_i = np.linspace(min(x), max(x), num)
    f = interp1d(x, y, kind=kind)
    y_i = f(x_i)
    return (x_i, y_i)


def interpolate_plot(ax, x, y, **kwargs):
    """
    Plot an interpolated line on ax for x,y

    :param ax: ax to plot interpolated line
    :param x: xpoints to interpolate
    :param y: ypoints to interpolate
    :param kwargs:
    :return: None
    """
    x, y = interpolate(x, y, **kwargs)
    assert any(x)
    assert any(y)
    ax.plot(x, y, c='grey', zorder=-1, lw=0.9)


def set_unique_legend(ax, **kwargs):
    """
    Given an axis with points with labels, make a legend without duplicate labels.

    :param ax:
    :param kwargs:
    :return:
    """
    from collections import OrderedDict
    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), **kwargs)
