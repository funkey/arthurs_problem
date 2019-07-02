import numpy as np

def secret_process(num_samples, intervention=None):

    # sample x

    x = np.random.normal(size=num_samples)

    if intervention and 'x' in intervention:
        x[:] = intervention['x']

    # sample z

    biased_coin = x <= 0.25

    num_z_samples_biased = np.sum(biased_coin)
    num_z_samples_unbiased = num_samples - num_z_samples_biased

    z_biased = np.random.random(size=num_z_samples_biased) > 0.25
    z_unbiased = np.random.random(size=num_z_samples_unbiased) > 0.5

    z = np.zeros((num_samples,), dtype=np.bool)
    z[biased_coin==1] = z_biased
    z[biased_coin==0] = z_unbiased

    if intervention and 'z' in intervention:
        z[:] = intervention['z']

    # sample y

    y = np.random.randint(low=1, high=6, size=num_samples)
    y[z==1] *= 2

    if intervention and 'y' in intervention:
        y[:] = intervention['y']

    return (x, y, z)
