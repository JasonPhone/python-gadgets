import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def func(x, A, B):
    return A * x + B


plt.figure()
data_x = [5.196, 5.490, 6.879, 7.408, 8.214]
data_y = [0.446, 0.544, 1.147, 1.347, 1.720]
figure_lt = 0
figure_rt = 10
plt.scatter(data_x[:], data_y[:], 3, marker="x")

fit_A, fit_B = optimize.curve_fit(func, data_x, data_y)[0]
fit_x = np.arange(figure_lt, figure_rt, (figure_rt - figure_lt) / 50)
fit_y = fit_A * fit_x + fit_B
plt.plot(fit_x, fit_y, "blue")
print("{} {}".format(fit_A, fit_B))

plt.show()
