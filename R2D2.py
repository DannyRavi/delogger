
# from numpy import exp, array, random, dot

# training_set_inputs = array([[0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1]])

# training_set_outputs = array([[0, 0, 1, 0, 1, 1, 1]]).T

# # random.seed(1)

# # synaptic_weights = 2 * random.random((3, 1)) - 1
# synaptic_weights =[[1],[1],[1]]

# for iteration in range(100):

#     output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))

#     synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))

# print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))

# import numpy as np
# class Perceptron:
    
#     def __init__(self, input_length, weights=None):
#         if weights is None:
#             self.weights = np.ones(input_length) * 0.5
#         else:
#             self.weights = weights
        
#     @staticmethod
#     def unit_step_function(x):
#         if x > 0.5:
#             return 1
#         return 0
        
#     def __call__(self, in_data):
#         weighted_input = self.weights * in_data
#         weighted_sum = weighted_input.sum()
#         return Perceptron.unit_step_function(weighted_sum)
    
# p = Perceptron(3, np.array([-1, 1,1]))
# for x in [np.array([0, 0, 0]), np.array([0, 1, 1]), 
#           np.array([1, 0, 1]), np.array([1, 1, 1])]:
#     y = p(np.array(x))
#     print(x, y)



import numpy as np


# def medfilt (x, k):
#     """Apply a length-k median filter to a 1D array x.
#     Boundaries are extended by repeating endpoints.
#     """
#     assert k % 2 == 1, "Median filter length must be odd."
#     assert x.ndim == 1, "Input must be one-dimensional."
#     k2 = (k - 1) // 2
#     y = np.zeros ((len (x), k), dtype=x.dtype)
#     y[:,k2] = x
#     for i in range (k2):
#         j = k2 - i
#         y[j:,i] = x[:-j]
#         y[:j,i] = x[0]
#         y[:-j,-(i+1)] = x[j:]
#         y[-j:,-(i+1)] = x[-1]
#     return np.median (y, axis=1)


# def test ():
#     import pylab as p
#     x = np.linspace (0, 1, 101)
#     x[3::10] = 1.5
#     p.plot (x)
#     p.plot (medfilt (x,3))
#     p.plot (medfilt (x,5))
#     p.show ()


# if __name__ == '__main__':
#     test ()    

a=range(10)
print(a)
for i in range(0, len(a)-1):
    print("i")
    print(i)
    print("a[i]")
    print(a[i])
    print("a[i+1]")
    print(a[i+1])
    



