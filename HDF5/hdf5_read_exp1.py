import h5py
import numpy as np

with h5py.File('exp1.hdf5','r') as f:
    print(f.keys())
    data = np.array(f.get('values'))
    print(data)
