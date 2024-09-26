import h5py
import numpy as np

values = np.random.randn(20)
print(values)

with h5py.File('exp1.hdf5','w') as f:
    data_set = f.create_dataset("values", data = values)