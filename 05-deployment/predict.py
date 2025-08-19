import pickle

input_file = 'model_C=1.0.bin'

with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)