"""
Module to save all open figures to a pdf (by default) or any format used by
matplotlib's savefig function. Running pickle on the images is also available.
"""
from matplotlib.backends.backend_pdf import PdfPages
import pickle
import time
import matplotlib.pyplot as plt
import os.path as osp

def saveFigs(fn='Plots'+time.strftime("_%Y%m%d_%H%M%S"), figs=None, dpi=200, fmt='pdf', bpickle=False):
    """
    save all open figures
    :param fn: filename string
    :param figs: user selectable figures to save
    :param dpi: dots per inch resolution
    :param fmt: format of save file
    :param bpickle: boolean pickle figure file for reopening later
    :return: none
    """
    # check filename for overlap
    if osp.exists(fn+'.'+fmt):
        i = 0
        fnnew = '%s_%i' % (fn, i)
        while osp.exists(fnnew + '.' + fmt):
            fnnew = '%s_%i' % (fn, i)
            i += 1
    else:
        fnnew = fn
    # get figure handles
    if figs is None:
        figures = [plt.figure(n) for n in plt.get_fignums()]
    else:
        figures = [plt.figure(n) for n in figs]
    print('Figs:'+str(len(figures)))
    # save formats
    if fmt == 'pdf':
        pp = PdfPages(fnnew + '.' + fmt)
        for ii, fig in enumerate(figures):
            pp.savefig(fig)
            if bpickle:
                with open('%s_F%i.pickle' % (fnnew, ii), 'wb') as f:
                    pickle.dump(fig, f)

        pp.close()
    else:
        for ii, fig in enumerate(figures):
            pp = fnnew + '_' + str(ii) + '.' + fmt
            fig.savefig(pp, format=fmt, dpi=dpi)
            if bpickle:
                with open('%s_F%i.pickle' % (fnnew, ii), 'wb') as f:
                    pickle.dump(fig, f)
