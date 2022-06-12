#IMPORTING HDG5 FILES
# Hierarchical Data Format version5
# Standard for storing large quantities of numerical data
# HDF5 can scale exabytes

# Import packages
import numpy as np
import h5py

# Assign filename: file
file='LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
    
#Extracting data from your HDF5 file
#In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.
#To do so, you'll need to first explore the HDF5 group 'strain'

# Get the HDF5 group: group
group=data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain=np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
num_samples=10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

