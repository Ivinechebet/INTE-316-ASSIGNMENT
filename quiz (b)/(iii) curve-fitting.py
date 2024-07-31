import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Define the model function
def model(x, a, b, c):
    return a * np.exp(b * x) + c

# Generate some data
xdata = np.linspace(0, 4, 50)
ydata = model(xdata, 2.5, -1.3, 0.5) + 0.2 * np.random.normal(size=len(xdata))

# Fit the curve
params, params_covariance = opt.curve_fit(model, xdata, ydata, p0=[2, -1, 0.5])

# Plot the data and the fitted curve
plt.scatter(xdata, ydata, label='Data')
plt.plot(xdata, model(xdata, *params), label='Fitted function')
plt.legend(loc='best')
plt.show()
