import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    list = np.array(list)
    l = list.reshape((3,3))
    calculations = dict()
    calculations['mean'] = [np.mean(l, axis=0).tolist(), np.mean(l, axis=1).tolist(), np.mean(l)]
    calculations['variance'] = [np.var(l,axis=0).tolist(), np.var(l, axis=1).tolist(), np.var(l)]
    calculations['standard deviation'] = [np.std(l, axis=0).tolist(), np.std(l, axis=1).tolist(), np.std(l)]
    calculations['max'] = [np.max(l, axis=0).tolist(), np.max(l, axis=1).tolist(), np.max(l)]
    calculations['min'] = [np.min(l, axis=0).tolist(), np.min(l, axis=1).tolist(), np.min(l)]
    calculations['sum'] = [np.sum(l, axis=0).tolist(), np.sum(l, axis=1).tolist(), np.sum(l)]
    return calculations
