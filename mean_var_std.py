import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    np_array = np.array(list)
    matrix = np_array.reshape((3,3))
    
    mean_0 = np.mean(matrix, axis = 0).tolist()
    mean_1 = np.mean(matrix, axis =1).tolist()
    mean_flat = np.mean(np_array)
    
    var_0 = np.var(matrix, axis = 0).tolist()
    var_1 = np.var(matrix, axis = 1).tolist()
    var_flat = np.var(np_array)
    
    std_0 = np.std(matrix, axis = 0).tolist()
    std_1 = np.std(matrix, axis = 1).tolist()
    std_flat = np.std(np_array)
    
    max_0 = np.max(matrix, axis = 0).tolist()
    max_1 = np.max(matrix, axis = 1).tolist()
    max_flat = np.max(np_array)
    
    min_0 = np.min(matrix, axis = 0).tolist()
    min_1 = np.min(matrix, axis = 1).tolist()
    min_flat = np.min(np_array)
    
    sum_0 = np.sum(matrix, axis = 0).tolist()
    sum_1 = np.sum(matrix, axis = 1).tolist()
    sum_flat = np.sum(np_array)
    
    mean = [mean_0, mean_1, mean_flat]
    var = [var_0, var_1, var_flat]
    std = [std_0, std_1, std_flat]
    max = [max_0, max_1, max_flat]
    min = [min_0, min_1, min_flat]
    sum = [sum_0, sum_1, sum_flat]
    
    calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
    }
    return calculations