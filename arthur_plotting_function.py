import numpy as np
import matplotlib.pyplot as pl
import time
from secret import secret_process



def display_dataset(x,y,z):

    n = x.shape[0]
    # compute marginals

    # marginal of z
    z_pos = np.sum(z)
    z_neg = n-z_pos
    print("marginal of z: %f/%f" % (z_pos/n, z_neg/n))

    # marginal of y
    values, counts = np.unique(y, return_counts = True)
    for v, c in zip(values, counts):
        print('marginal of y=%d, c = %f' % (v, c/n))

    fig = pl.figure(figsize = (10,15))
    title = 'marginals'
    pl.suptitle(title)
    fig.add_subplot(3,1,1)
    pl.title('x')
    pl.hist(x, bins = 100)

    fig.add_subplot(3,1,2)
    pl.title('y')
    pl.bar(x = values, height=counts/n)

    fig.add_subplot(3,1,3)
    pl.title('z')
    pl.bar(x = [0,1], height=[z_pos, z_neg])
    pl.show()


if __name__ == "__main__":

    n = 10000
    intervention = {}
    x, y, z = secret_process(n, intervention)
    display_dataset(x,y,z)
