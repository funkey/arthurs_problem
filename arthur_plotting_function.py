import numpy as np
import matplotlib.pyplot as pl
import time
from secret import secret_process
from scipy.stats import entropy

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

    ############## marginals ##############
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

    ############## p(z|x) ##############

    fig = pl.figure(figsize = (15,15))
    title = 'z conditioned on x'
    pl.suptitle(title)
    intervals = np.array([-1,-.5,0,.5,1])
    for ind, i in enumerate(intervals[:-1]):
        print('x in interval %f' % i)
        fig.add_subplot(intervals.shape[0]//2, 2, ind + 1)
        pl.title('from {0} to {1}'.format(i, intervals[ind+1]))
        tmp = z[np.logical_and(x>i, x<=intervals[ind+1])]
        nn = tmp.shape[0]
        pl.bar(x = [0,1], height = [tmp.sum()/nn, (nn-tmp.sum())/nn] )
        pl.ylim([0,1])
    pl.show()

    ############## p(x|z) ##############

    fig = pl.figure(figsize = (10,15))
    title = 'x conditioned on z'

    for z_value in [0, 1]:
        pl.suptitle(title)
        fig.add_subplot(2, 2, 1 + 2*z_value)
        pl.title('x')
        pl.hist(x[z==z_value], bins = 100)
        fig.add_subplot(2, 2, 2 + 2*z_value)
        pl.title('y')
        values, counts = np.unique(y[z==z_value], return_counts = True)
        pl.bar(x = values, height=counts/np.sum(z==z_value))

    pl.show()

    ############## p(x|y) ##############

    fig = pl.figure(figsize = (15,15))
    title = 'x conditioned on y'
    pl.suptitle(title)
    values, counts = np.unique(y, return_counts = True)
    for ind, y_value in enumerate(values):
        print('y = %d' % y_value)
        fig.add_subplot(3, 3, ind + 1)
        pl.title(y_value)
        pl.hist(x[y == y_value], bins = 100)

    pl.show()



    ############## p(x|y, z) ##############
    for z_value in [0, 1]:
        values, counts = np.unique(y[z==z_value], return_counts = True)
        fig = pl.figure(figsize = (10,15))
        title = ('conditioned on z = %d and y' % z_value)

        # # compute binned probability vector
        # x_cond_yz = []
        # for ind, y_value in enumerate(values):
        #     tmp = x[np.logical_and(z==z_value,y == y_value)]
        #     x_cond_yz.append(np.hist(tmp, bins = 50, range = (-4,4))/tmp.shape[0])
        # for indi, y_valuei in enumerate(values):
        #     for indj, y_valuej in enumerate(values)


        pl.suptitle(title)
        for ind, y_value in enumerate(values):
            print('y = %d' % y_value)
            fig.add_subplot(3, 2, ind + 1)
            pl.title(y_value)
            pl.hist(x[np.logical_and(z==z_value,y == y_value)], bins = 100)

    pl.show()



if __name__ == "__main__":

    n = 10000
    intervention = {}
    x, y, z = secret_process(n, intervention)
    display_dataset(x,y,z)
