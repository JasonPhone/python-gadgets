import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def func(x, A, B):
    return A * x + B


plt.figure()
data_x = [-0.201, -0.0585, 0.04844, 0.1345, 0.2063, 0.2679]
data_y = [-0.1838, -0.1257, -0.06905, -0.01341, 0.02366, 0.05690]
figure_lt = -0.2
figure_rt = 0.3
plt.scatter(data_x[:], data_y[:], 3, marker="x")

fit_A, fit_B = optimize.curve_fit(func, data_x, data_y)[0]
fit_x = np.arange(figure_lt, figure_rt, (figure_rt - figure_lt) / 50)
fit_y = fit_A * fit_x + fit_B
plt.plot(fit_x, fit_y, "blue")
print("{} {}".format(fit_A, fit_B))

plt.show()
