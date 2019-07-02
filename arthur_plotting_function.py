import numpy as np
import matplotlib.pyplot as pl
import time




def display_dataset(x,y,z):

    n = x.shape[0]
    # compute marginals

    # marginal of y
    y_pos = np.sum(y)
    y_neg = n-y_pos
    print("marginal of y: %f/%f" % (y_pos/n, y_neg/n))

    # marginal of z
    values, counts = np.unique(z, return_counts = True)
    for v, c in zip(values, counts):
        print('marginal of z=%d, c = %f' % (v, c/n))

    fig = pl.figure(figsize = (10,15))
    title = 'marginals'
    pl.suptitle(title)
    fig.add_subplot(3,1,1)
    pl.title('x')
    pl.hist(x, bins = 100)

    fig.add_subplot(3,1,2)
    pl.title('z')
    pl.bar(x = values, height=counts/n)

    fig.add_subplot(3,1,3)
    pl.title('y')
    pl.bar(x = [0,1], height=[y_pos, y_neg])
    pl.show()


if __name__ == "__main__":

    n = 500
    intervention = {}
    x, y, z = secret_process(n, intervention)
    display_dataset(x,y,z)
