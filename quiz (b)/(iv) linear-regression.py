import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.normal(size=100)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Plot the data and the regression line
plt.scatter(x, y, label='Data')
plt.plot(x, slope * x + intercept, label='Fitted line', color='red')
plt.legend(loc='best')
plt.show()
