# https://pypi.org/project/plotext/

import plotext as plt
import numpy as np

l = 1000
n = 2
f = n * np.pi / l
x = np.arange(0, l)
xticks = np.linspace(0, l - 1, 5)
xlabels = [str(i) + "π" for i in range(5)]
frames = 500

for i in range(frames):
    y = np.sin(n * f * x + 2 * np.pi / frames * i)

    plt.clp()
    plt.clt()
    plt.scatter(x, y)
    plt.ylim(-1, 1)
    plt.xticks(xticks, xlabels)
    plt.yticks([-1, 0, 1])
    plt.title("plotext - streaming data")
    plt.nocolor()
    plt.sleep(0.001)
    plt.show()
