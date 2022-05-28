# Plotting the Binomial PMF

# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults,normed=True,bins=bins)

# Label axes
_ = plt.xlabel('')
_ = plt.ylabel('')

# Show the plot
plt.show()
