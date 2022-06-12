#import scipy.io
#file='file'
#mat=scipy.io.loadmat(file)

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Import package
import scipy.io

# Load MATLAB file: mat
mat=scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
