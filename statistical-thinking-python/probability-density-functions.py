#The normal PDF
# In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF of a known distribution using hacker statistics. Specifically, you will plot a Normal PDF for various values of the variance.
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1=np.random.normal(20,1,size=100000)
samples_std3=np.random.normal(20,3,size=100000)
samples_std10=np.random.normal(20,10,size=100000)

# Make histograms
plt.hist(samples_std1,normed=True, bins=100,histtype='step')
plt.hist(samples_std3,normed=True, bins=100,histtype='step')
plt.hist(samples_std10,normed=True, bins=100,histtype='step')




# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()

# Generate CDFs
x_std1,y_std1=ecdf(samples_std1)
x_std3,y_std3=ecdf(samples_std3)
x_std10,y_std10=ecdf(samples_std10)



# Plot CDFs
plt.plot(x_std1,y_std1,marker=".",linestyle="none")
plt.plot(x_std3,y_std3,marker=".",linestyle="none")
plt.plot(x_std10,y_std10,marker=".",linestyle="none")


# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
