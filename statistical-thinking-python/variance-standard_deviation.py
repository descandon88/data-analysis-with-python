# Computing the variance
# Array of differences to mean: differences
differences=versicolor_petal_length-np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq=differences**2

# Compute the mean square difference: variance_explicit
variance_explicit=np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np=np.var(versicolor_petal_length)

# Print the results
print(variance_explicit,variance_np)

# The standard deviation and the variance
# Compute the variance: variance
variance=np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))

# Scatter plots
# Make a scatter plot
_ = plt.plot(versicolor_petal_length,versicolor_petal_width, marker='.', linestyle='none')


# Label the axes
_ = plt.xlabel('versicolor_petal_length')
_ = plt.ylabel('versicolor_petal_width')

# Show the result
plt.show()

# Computing the covariance
# Compute the covariance matrix: covariance_matrix
covariance_matrix=np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov=covariance_matrix[0 ,1]

# Print the length/width covariance
print(petal_cov)

# Computing the Pearson correlation coefficient
# In this exercise, you will write a function, pearson_r(x, y) that takes in two arrays and returns the Pearson correlation coefficient.
#You will then use this function to compute it for the petal lengths and widths of I. versicolor. Again, we include the scatter plot you
#generated in a previous exercise to remind you how the petal width and length are related.

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat=np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r=pearson_r(versicolor_petal_length,versicolor_petal_width)

# Print the result
print(r)

