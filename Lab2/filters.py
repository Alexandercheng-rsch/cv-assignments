import numpy as np

sobel_x = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])

sobel_y = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
])

difference_gradient_filter_x = np.array([
    [-1,1],
    [-1,1]
])

difference_gradient_filter_y = np.array([
    [1,1],
    [-1,-1]
])

first_order_gaussian_filter_1d_length5 = np.array([
    [0.1897,0.1741,0,-0.1741,-0.1897]
])

gaussian_filter_1d_length5 = np.array([
    [0.0545,0.2442,0.4026,0.2442,0.0545]
])

gaussian_filter_3x3 = np.array([
    [0.0113,0.0838,0.0113],
    [0.0838,0.6193,0.0838],
    [0.0113,0.0838,0.0113]
])

gaussian_filter_5x5 = np.array([
 [0.00297025, 0.0133089,  0.0219417,  0.0133089,  0.00297025],
 [0.0133089,  0.05963364, 0.09831492, 0.05963364, 0.0133089 ],
 [0.0219417,  0.09831492, 0.16208676, 0.09831492, 0.0219417 ],
 [0.0133089,  0.05963364, 0.09831492, 0.05963364, 0.0133089 ],
 [0.00297025, 0.0133089,  0.0219417,  0.0133089 , 0.00297025]
])

