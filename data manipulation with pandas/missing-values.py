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
