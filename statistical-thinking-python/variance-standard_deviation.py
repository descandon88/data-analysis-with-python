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