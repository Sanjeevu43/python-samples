import h5py
import numpy as np

import pickle

with h5py.File('C:/NewRaFTS/python-model-api/resources/CEDAR1v4model1nocanvas30epochs.hdf5','r') as f:
    print(f.keys())
    model_weights = np.array(f.get('model_weights'))
    print(model_weights)
    print(type(model_weights[0]))
    print('=============================================================================================')
    optimizer_weights = np.array(f.get('optimizer_weights'))
    print(optimizer_weights)

# with open('C:/NewRaFTS/python-model-api/resources/SignatureDataGenerator_CEDAR1v4model1canvas.pkl', 'rb') as f:
#         datagen = pickle.load(f)
