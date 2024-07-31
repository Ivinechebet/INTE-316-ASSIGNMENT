import scipy.interpolate as spi
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create a spline representation of the data
tck = spi.splrep(x, y)

# Evaluate the spline at new points
x_new = np.linspace(0, 10, 200)
y_new = spi.splev(x_new, tck)

# Plot the data and the spline
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, label='Spline', color='red')
plt.legend(loc='best')
plt.show()
