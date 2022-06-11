# Finding missing values
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

avocados_2016.head(10)

# Check individual values for missing values
print(avocados_2016.isna().any())

# Check each column for missing values
print(avocados_2016.isna().any().sum())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()

# Removing missing values

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


# Replacing missing values
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()
