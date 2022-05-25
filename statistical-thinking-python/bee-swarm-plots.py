# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species',y='petal length (cm)',data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
# Show the plot
plt.show()

#Plotting the ECDF
#You will now use your ecdf() function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf() function returns two arrays so you will need to unpack them. An example of such unpacking is x, y = foo(data), for some function foo()
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers,y_vers,marker=".",linestyle = 'none')

# Label the axes
_ = plt.xlabel('x_vers')
_ = plt.ylabel('y_vers')


# Display the plot
plt.show()
